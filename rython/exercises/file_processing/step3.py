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

with open("file/step_3.txt", 'r') as f:
    file_by_lines = f.read().splitlines()
    lines_hit = set()
    line_num = 1
    while True:
        current_line = file_by_lines[int(line_num) - 1]
        if current_line in lines_hit:
            break
        new_line_num = navigate(current_line.split())
        lines_hit.add(current_line)
        line_num = new_line_num
    print(f"Answer: Line {line_num} {current_line}")