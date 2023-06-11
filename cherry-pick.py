#!/usr/bin/env python3
import subprocess
import sys
import re
import os
import json

# File to store skipped commits
SKIPPED_COMMITS_FILE = os.path.join(os.path.dirname(__file__), '.cherry-pick-skipped.json')

def load_skipped_commits():
    """Load previously skipped commits from disk"""
    try:
        if os.path.exists(SKIPPED_COMMITS_FILE):
            with open(SKIPPED_COMMITS_FILE, 'r') as f:
                skipped = json.load(f)
                return set(skipped)
    except Exception as e:
        print(f"Warning: Could not load skipped commits: {e}")
    return set()

def save_skipped_commits(skipped_commits):
    """Save skipped commits to disk"""
    try:
        with open(SKIPPED_COMMITS_FILE, 'w') as f:
            json.dump(list(skipped_commits), f)
    except Exception as e:
        print(f"Warning: Could not save skipped commits: {e}")

def get_unique_commits():
    """Get commits that exist in upstream/main but not in the current branch"""
    try:
        # Get the list of commits that are in upstream/main but not in HEAD
        cmd = ["git", "log", "HEAD..upstream/main", "--pretty=format:%H"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Return commits in chronological order (oldest first)
        commits = result.stdout.strip().split('\n')
        return list(reversed(commits)) if commits and commits[0] else []
    
    except subprocess.CalledProcessError as e:
        print(f"Error getting commit list: {e}")
        sys.exit(1)

def get_conflicted_files():
    """Get list of files with merge conflicts"""
    try:
        result = subprocess.run(["git", "diff", "--name-only", "--diff-filter=U"], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return []

def auto_resolve_conflicts():
    """Automatically resolve conflicts for specific files based on rules"""
    conflicted_files = get_conflicted_files()
    
    for file in conflicted_files:
        if file == "README.md":
            # Keep our version for README.md
            subprocess.run(["git", "checkout", "--ours", file], check=True)
            subprocess.run(["git", "add", file], check=True)
            print(f"Auto-resolved {file} (kept our version)")
        elif file in ["Dockerfile", "docker-compose.yml"]:
            # Keep upstream version for Docker files
            subprocess.run(["git", "checkout", "--theirs", file], check=True)
            subprocess.run(["git", "add", file], check=True)
            print(f"Auto-resolved {file} (kept upstream version)")

def is_commit_empty():
    """Check if there are any changes staged for commit"""
    try:
        result = subprocess.run(["git", "diff", "--cached", "--quiet"])
        # Return True if there are no changes (exit code 0)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def cherry_pick_commits(commits):
    """Cherry-pick each commit in order until we hit a conflict"""
    skipped_commits = load_skipped_commits()  # Load previously skipped commits
    
    for commit in commits:
        if commit in skipped_commits:
            print(f"Skipping previously empty commit: {commit}")
            continue
            
        try:
            print(f"Cherry-picking commit: {commit}")
            subprocess.run(["git", "cherry-pick", commit], check=True)
            print("Successfully cherry-picked commit")
            
        except subprocess.CalledProcessError:
            print("\nMerge conflict encountered!")
            
            # Get and display conflicted files
            conflicted_files = get_conflicted_files()
            print("\nFiles with conflicts:")
            for file in conflicted_files:
                print(f"- {file}")
            
            # Try to auto-resolve conflicts based on rules
            auto_resolve_conflicts()
            
            # Check if there are still unresolved conflicts
            remaining_conflicts = get_conflicted_files()
            if remaining_conflicts:
                print("\nRemaining conflicts to resolve manually:")
                for file in remaining_conflicts:
                    print(f"- {file}")
                print("\nTo resolve:")
                print("1. Resolve the conflicts in the affected files")
                print("2. Git add the resolved files")
                print("3. Git cherry-pick --continue")
                print("   (or git cherry-pick --abort to stop)")
                print("\nOnce resolved, run this script again to continue with remaining commits")
                sys.exit(0)
            else:
                # Check if the commit would be empty after resolution
                if is_commit_empty():
                    print(f"Commit {commit} would be empty after conflict resolution - skipping")
                    subprocess.run(["git", "cherry-pick", "--skip"], check=True)
                    skipped_commits.add(commit)  # Remember this commit was skipped
                    save_skipped_commits(skipped_commits)  # Save to disk
                else:
                    # All conflicts were auto-resolved, continue cherry-picking
                    subprocess.run(["git", "cherry-pick", "--continue"], check=True)
                    print("All conflicts auto-resolved, continuing...")
                continue

def main():
    # Ensure we have the latest upstream information
    try:
        subprocess.run(["git", "fetch", "upstream"], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to fetch from upstream. Please ensure upstream remote is configured.")
        sys.exit(1)

    # Get commits to cherry-pick
    commits = get_unique_commits()
    
    if not commits:
        print("No new commits to cherry-pick from upstream/main")
        sys.exit(0)
    
    print(f"Found {len(commits)} commits to cherry-pick")
    cherry_pick_commits(commits)
    print("\nAll commits successfully cherry-picked!")

if __name__ == "__main__":
    main()
