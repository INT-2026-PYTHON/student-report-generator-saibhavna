"""gradebook.reports — build a printable report from grade records."""

from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass

def format_report(records: list[dict]) -> str:

    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))

    top_name, top_avg = top_scorer(records)

    passed = passing_students(records)

    report = ""

    report += "=== Gradebook Report ===\n"
    report += f"Total records: {len(records)}\n"

    report += "Subjects offered: "

    for i in range(len(subjects)):
        report += subjects[i]

        if i != len(subjects) - 1:
            report += ", "

    report += "\n\n"

    report += "Averages:\n"

    for name in sorted(averages):
        report += f"  {name}: {averages[name]}\n"

    report += "\n"

    report += f"Top scorer: {top_name} ({top_avg})\n"

    report += "Passing students (>= 60.0): "

    for i in range(len(passed)):
        report += passed[i]

        if i != len(passed) - 1:
            report += ", "

    return report
