import fileinput

n_line, s = 0, 0

for line in fileinput.input():
    n_line += 1
    s += len(line)

print(n_line, s)

