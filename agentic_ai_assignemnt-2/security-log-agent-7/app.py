from analyzer import analyze_security_logs


LOG_FILE = "security_logs.txt"


def load_logs():
    """
    Load security logs from the log file.
    """

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            return file.read().strip()

    except FileNotFoundError:
        print(f"\nError: {LOG_FILE} was not found.")
        return ""


def main():

    print("\n========================================")
    print("     SECURITY LOG ANALYSIS AGENT")
    print("========================================")

    logs = load_logs()

    if not logs:
        print("\nNo security logs found.")
        return

    print("\nSecurity logs loaded successfully.")

    print("\nAnalyzing security events...")
    print("Please wait...\n")

    try:
        report = analyze_security_logs(logs)

    except Exception as e:
        print("\nGemini Error:")
        print(e)
        return

    print("\n========================================")
    print("       SECURITY ANALYSIS REPORT")
    print("========================================\n")

    print(report)

    print("\n========================================")
    print("             END OF REPORT")
    print("========================================")


if __name__ == "__main__":
    main()