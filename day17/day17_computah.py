if __name__ == "__main__":
    out = []

    with open(r"day17\input") as f:
        lines = f.readlines()

    reg_a = int(lines[0].strip().split(" ")[-1])
    reg_b = int(lines[1].strip().split(" ")[-1])
    reg_c = int(lines[2].strip().split(" ")[-1])

    str_program = lines[4].strip().split(" ")[-1]
    list_program = list(map(int, lines[4].strip().split(" ")[-1].split(",")))

    # Part 1
    id = 0
    while True:
        if id >= len(list_program):
            break

        opcode = list_program[id]
        operand = list_program[id+1]

        if operand < 4:
            pass
        elif operand == 4:
            operand = reg_a
        elif operand == 5:
            operand = reg_b
        elif operand == 6:
            operand = reg_c

        if opcode == 0:
            reg_a = int(reg_a/2**operand)
        if opcode == 1:
            reg_b = reg_b ^ operand
        if opcode == 2:
            reg_b = operand % 8
        if opcode == 3:
            if reg_a > 0:
                id = operand
                continue
        if opcode == 4:
            reg_b = reg_b ^ reg_c
        if opcode == 5:
            out.append(operand % 8)
        if opcode == 6:
            reg_b = int(reg_a/2**operand)
        if opcode == 7:
            reg_c = int(reg_a/2**operand)

        id += 2

        str_out = ','.join(map(str, out))

    print("Part 1:")
    print(f"Register A: {reg_a}")
    print(f"Register B: {reg_b}")
    print(f"Register C: {reg_c}")
    print(f"Out: {str_out}")
    print()

    # Part 2
    reg_a_idx = 3890735
    while True:
        reg_a_idx += 1
        reg_a = reg_a_idx
        id = 0
        reg_b = 0
        reg_c = 0
        while True:
            if id >= len(list_program):
                break

            opcode = list_program[id]
            operand = list_program[id+1]
            # print(opcode, operand, reg_a, reg_b, reg_c)

            if operand < 4:
                pass
            elif operand == 4:
                operand = reg_a
            elif operand == 5:
                operand = reg_b
            elif operand == 6:
                operand = reg_c

            if opcode == 0:
                reg_a = int(reg_a/2**operand)
            if opcode == 1:
                reg_b = reg_b ^ operand
            if opcode == 2:
                reg_b = operand % 8
            if opcode == 3:
                if reg_a > 0:
                    id = operand
                    continue
            if opcode == 4:
                reg_b = reg_b ^ reg_c
            if opcode == 5:
                out.append(operand % 8)
            if opcode == 6:
                reg_b = int(reg_a/2**operand)
            if opcode == 7:
                reg_c = int(reg_a/2**operand)

            id += 2

        str_out = ','.join(map(str, out))
        print(f"Out: {str_out}")
        out = []
        if str_out == str_program:
            print(f"Register A original value: {reg_a_idx}")
            break

    print("Part 2:")
    print(f"Register A: {reg_a}")
    print(f"Register B: {reg_b}")
    print(f"Register C: {reg_c}")
    # print(f"Out: {','.join(map(str, out))}")
    print(f"Out: {str_out}")
