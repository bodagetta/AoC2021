with open('test_input_2.txt') as f:
    lines = f.readlines()

# 3 Window Average

averaged_array = list()

for i in range(2,len(lines)):
    sum = 0
    for j in range(0,3):
        sum += int(lines[i-j].strip('\n'))
    averaged_array.append(sum)

increase_count = 0
decrease_count = 0

for i in range(1,len(averaged_array)):
    cur_line = int(averaged_array[i])
    prev_line = int(averaged_array[i-1])
    if (cur_line < prev_line):
        decrease_count += 1
        print(cur_line," Descrease")
    elif (cur_line > prev_line):
        increase_count += 1
        print(cur_line," Increase")
    else:
        print(cur_line," No Change")

print("Increase Count: ",increase_count)
print("Decrease Count: ",decrease_count)