def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []

    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 2

        top_row.append(num1.rjust(width))
        bottom_row.append(operator + num2.rjust(width - 1))
        dash_row.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_row.append(answer.rjust(width))

    arranged = '    '.join(top_row) + '\n'
    arranged += '    '.join(bottom_row) + '\n'
    arranged += '    '.join(dash_row)

    if show_answers:
        arranged += '\n' + '    '.join(answer_row)

    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')