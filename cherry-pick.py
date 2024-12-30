#!/usr/bin/env python3
import subprocess
import sys
import re

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

def cherry_pick_commits(commits):
    """Cherry-pick each commit in order until we hit a conflict"""
    for commit in commits:
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
