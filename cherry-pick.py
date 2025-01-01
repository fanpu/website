import subprocess
import sys

def run_command(command, capture_output=False):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=capture_output)
        return result.stdout.strip() if capture_output else None
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{command}' failed with error: {e}")
        sys.exit(1)

def list_new_commits(upstream_branch):
    print("Fetching upstream changes...")
    run_command("git fetch upstream")

    print(f"Listing commits in {upstream_branch} not in the current branch...")
    commits = run_command(f"git log --oneline HEAD..{upstream_branch}", capture_output=True)

    if not commits:
        print("No new commits to cherry-pick.")
        sys.exit(0)

    commit_list = [line.split()[0] for line in commits.splitlines()]
    print(f"Found {len(commit_list)} new commits.")
    return commit_list

def cherry_pick_commits(commits):
    for commit in commits:
        print(f"Cherry-picking commit: {commit}")
        try:
            run_command(f"git cherry-pick {commit}")
        except SystemExit:
            print("Conflict detected. Please resolve the conflict, then run:")
            print("  git cherry-pick --continue")
            print("Or abort the cherry-pick with:")
            print("  git cherry-pick --abort")
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python cherry_pick.py <upstream-branch>")
        sys.exit(1)

    upstream_branch = sys.argv[1]
    commits = list_new_commits(upstream_branch)
    cherry_pick_commits(commits)
    print("All commits cherry-picked successfully.")

if __name__ == "__main__":
    main()
