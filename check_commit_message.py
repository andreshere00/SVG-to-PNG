import sys


def main():
    """
    Validate a Git commit message to ensure it starts with an allowed prefix.

    Allowed prefixes:
        - add: Use for adding new features or functionality.
        - fix: Use for fixing bugs or issues.
        - refactor: Use for improving the structure or performance of the code without changing functionality.
        - hotfix:  Use for urgent, critical fixes.
    """
    # Read the commit message from the file passed as an argument
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file, "r") as file:
        commit_msg = file.read().strip()

    # Define the allowed prefixes
    allowed_prefixes = ["add:", "fix:", "refactor:", "hotfix:"]

    # Check if the commit message starts with one of the allowed prefixes
    if not any(commit_msg.startswith(prefix) for prefix in allowed_prefixes):
        print(
            "ERROR: Commit message must start with one of the following prefixes:\n"
            " - add:\n"
            " - fix:\n"
            " - refactor:\n"
            " - hotfix:"
        )
        sys.exit(1)

    print("Commit message validation passed!")
    sys.exit(0)


if __name__ == "__main__":
    main()
