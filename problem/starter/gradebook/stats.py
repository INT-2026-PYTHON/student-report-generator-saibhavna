"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass
"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    
    scores = {}

    for record in records:
        name = record["name"]

        if name not in scores:
            scores[name] = []

        scores[name].append(record["score"])
        
        
    averages_of_students = {}

    for name, marks in scores.items():
        averages_of_students[name] = round(sum(marks) / len(marks), 2)

    return averages_of_students


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    
    subjects = set()

    for record in records:
        subjects.add(record["subject"])

    return subjects


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    
    averages = average_per_student(records)

    top_name = ""
    top_avg = 0

    for name, avg in averages.items():
        if avg > top_avg:
            top_avg = avg
            top_name = name

    return (top_name, top_avg)


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    
    averages = average_per_student(records)

    passed = []

    for name, avg in averages.items():
        if avg >= threshold:
            passed.append(name)

    passed.sort()
    
    return passed