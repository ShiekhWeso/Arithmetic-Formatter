def arithmetic_arranger(problems, display_answers=False):
    # Error check: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems"
    
    first_operands = []
    second_operands = []
    operators = []
    max_widths = []
    
    # Process each problem
    for problem in problems:
        parts = problem.split()
        if parts [1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_operands.append(parts[0])
        operators.append(parts[1])
        second_operands.append(parts[2])
        max_widths.append(max(len(parts[0]), len(parts[2])) + 2)  # +2 for operator and space
    
    # Arrange problems
    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""
    
    for i in range(len(problems)):
        first_line += first_operands[i].rjust(max_widths[i]) + "    "
        second_line += operators[i] + " " + second_operands[i].rjust(max_widths[i] - 2) + "    "
        dashes += "-" * max_widths[i] + "    "
        if display_answers:
            if operators[i] == "+":
                answer = str(int(first_operands[i]) + int(second_operands[i]))
            else:
                answer = str(int(first_operands[i]) - int(second_operands[i]))
            answers += answer.rjust(max_widths[i]) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    if display_answers:
        arranged_problems += "\n" + answers.rstrip()

    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True))