with open('input_1.txt') as f:
    lines = f.readlines()

horizontal = 0
vertical = 0

for l in lines:
    l = l.strip('\n').split(' ')
    if l[0] == 'forward':
        horizontal += int(l[1])
    if l[0] == 'down':
        vertical += int(l[1])
    if l[0] == 'up':
        vertical -= int(l[1])

print("Horizontal: ", horizontal)
print("Vertical: ", vertical)

print("Answers: ", horizontal*vertical)
