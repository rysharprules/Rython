import math

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ^ y,
}

def navigate(goto) -> int:
    if(goto[1] == 'calc'):
        return math.floor(ops[goto[2]](int(goto[3]), int(goto[4])))
    else:
        return goto[1]

def remove(statement, current_line, file_by_lines) -> int:
    line_to_remove = int(statement[1])
    if line_to_remove <= current_line:
        line_to_process_next = current_line
    else:
        line_to_process_next = current_line + 1
    file_by_lines.pop(line_to_remove)
    return line_to_process_next

def replace(statement, current_line, file_by_lines) -> int:
    line_number_to_replace = int(statement[1])
    line_number_to_copy = int(statement[2])
    copied_line = file_by_lines[line_number_to_copy - 1]
    file_by_lines.pop(line_number_to_replace - 1)
    file_by_lines.insert(line_number_to_replace - 1, copied_line)
    return current_line + 1

def process(statement, current_line, file_by_lines):
    if statement[0] == 'goto':
        return navigate(statement)
    elif statement[0] == 'remove':
        return remove(statement, current_line, file_by_lines)
    else: # 'replace':
        return replace(statement, current_line, file_by_lines)

with open("file/step_4.txt", 'r') as f:
    file_by_lines = f.read().splitlines()
    lines_hit = set()
    line_num = 1
    while True:
        current_line = file_by_lines[int(line_num) - 1]
        if current_line in lines_hit:
            break
        new_line_num = process(current_line.split(), int(line_num), file_by_lines)
        lines_hit.add(current_line)
        line_num = new_line_num

print(f"Answer: Line {line_num} {current_line}")