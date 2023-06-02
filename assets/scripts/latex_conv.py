import os
LEFT = 0
RIGHT = 1
CNT = 0
DELIM = '$'
with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        state = LEFT
        for line in f:
            output_line = ""
            for c in line:
                if c == DELIM:
                    if CNT == 0:
                        if state == LEFT:
                            output_line += '\\'
                        elif state == RIGHT:
                            output_line += ' \\'
                    elif CNT == 1:
                        if state == LEFT:
                            output_line += '( '
                        elif state == RIGHT:
                            output_line += ')'
                    CNT += 1
                    if CNT == 2:
                        state = 1 - state
                    CNT %= 2
                else:
                    output_line += c
            print(output_line)

with open("input.txt", "w") as f:
    f.write("")
