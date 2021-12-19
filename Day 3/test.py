with open('test_input.txt') as f:
    lines = f.readlines()


length = len(lines[0].strip('\n'))

gamma = list()
epsilon = list()
ones_count = list()

for k in range(0, length):
    gamma.append(0)
    epsilon.append(0)
    ones_count.append(0)

ones_count = [0, 0, 0, 0, 0]

for l in lines:
    l = list(l.strip('\n'))
    for i in range(0, len(l)):
        if l[i] == '1':
            ones_count[i] += 1
    print(l)

print(ones_count)
print(len(lines))

for j in range(0, len(l)):
    if ones_count[j] > (len(lines)/2):
        gamma[j] = 1
        epsilon[j] = 0
    if ones_count[j] < (len(lines)/2):
        gamma[j] = 0
        epsilon[j] = 1

print(gamma)
print(epsilon)

gamma_dec = int("".join(str(x) for x in gamma), 2)
epsilon_dec = int("".join(str(x) for x in epsilon), 2)

print(gamma_dec)
print(epsilon_dec)

print("Answer: ", gamma_dec*epsilon_dec)
