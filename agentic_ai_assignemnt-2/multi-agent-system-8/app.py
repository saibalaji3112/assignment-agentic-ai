from agents import (
    research_agent,
    analyst_agent,
    report_agent
)


def main():

    print("\n========================================")
    print("       MULTI-AGENT COLLABORATION SYSTEM")
    print("========================================")

    task = input(
        "\nEnter the task you want the agents to complete: "
    ).strip()

    if not task:

        print("\nPlease enter a task.")

        return

    # --------------------------------------------------------
    # AGENT 1
    # --------------------------------------------------------

    research_results = research_agent(task)

    if not research_results:

        print("\nNo research results were found.")

        return

    print("\nResearch results collected successfully.")

    # --------------------------------------------------------
    # AGENT 2
    # --------------------------------------------------------

    analysis = analyst_agent(
        task,
        research_results
    )

    print("\nAnalysis completed successfully.")

    # --------------------------------------------------------
    # AGENT 3
    # --------------------------------------------------------

    final_report = report_agent(
        task,
        research_results,
        analysis
    )

    # --------------------------------------------------------
    # FINAL OUTPUT
    # --------------------------------------------------------

    print("\n========================================")
    print("             FINAL REPORT")
    print("========================================\n")

    print(final_report)

    print("\n========================================")
    print("        MULTI-AGENT PROCESS COMPLETE")
    print("========================================")


if __name__ == "__main__":
    main()