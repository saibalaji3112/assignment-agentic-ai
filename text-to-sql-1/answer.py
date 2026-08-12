def generate_answer(question, result):

    if isinstance(result, str):
        return result

    if not result:
        return "No results found."

    # Single result
    if len(result) == 1:

        row = result[0]

        if "name" in row and "salary" in row:
            return (
                f"The employee with the highest salary is "
                f"{row['name']}, with a salary of "
                f"{row['salary']}."
            )

        if "name" in row:
            return f"The answer is {row['name']}."

    # Multiple results
    if len(result) > 1:

        answers = []

        for row in result:
            answers.append(str(row))

        return "The results are: " + ", ".join(answers)

    return str(result)
