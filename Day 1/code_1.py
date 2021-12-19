with open('input_1.txt') as f:
    lines = f.readlines()

print(lines[0].strip('\n')," - ")
increase_count = 0
decrease_count = 0

for i in range(1,len(lines)):
    cur_line = int(lines[i].strip('\n'))
    prev_line = int(lines[i-1].strip('\n'))
    if (cur_line < prev_line):
        decrease_count += 1
        print(cur_line," Descrease")
    else:
        increase_count += 1
        print(cur_line," Increase")

print("Increase Count: ",increase_count)
print("Decrease Count: ",decrease_count)