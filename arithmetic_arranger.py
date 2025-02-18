def arithmetic_arranger(problems, display_answer=False):
    # Error check: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems"
    
    first_operands = []
    second_operands = []
    operators = []
    max_widths = []
    
    # Process each 
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
        