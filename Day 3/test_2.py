with open('test_input.txt') as f:
    lines = f.readlines()

length = len(lines[0].strip('\n'))

oxygen_generator_rating = lines
scrubber_rating = lines

# Find and return most common bit in position for lines array
# If numbers are equal, return default value


def mostCommonBit(lines, position, default):
    first_bit_one_count = 0
    first_bit_zero_count = 0
    for line in lines:
        line = list(line.strip('\n'))
        if line[position] == '0':
            first_bit_zero_count += 1
        else:
            first_bit_one_count += 1

    if first_bit_one_count > first_bit_zero_count:
        return 1
    elif first_bit_one_count < first_bit_zero_count:
        return 0
    else:
        return default


def leastCommonBit(lines, position, default):
    first_bit_one_count = 0
    first_bit_zero_count = 0
    for line in lines:
        line = list(line.strip('\n'))
        if line[position] == '0':
            first_bit_zero_count += 1
        else:
            first_bit_one_count += 1

    if first_bit_one_count < first_bit_zero_count:
        return 1
    elif first_bit_one_count > first_bit_zero_count:
        return 0
    else:
        return default


# Build Array of Only Most Common Bits

def downSelectArray(oxygen_generator_rating_local, scrubber_rating_local, position):
    oxygen_generator_rating_new = []
    scrubber_rating_new = []

    mc_bit_oxygen = mostCommonBit(oxygen_generator_rating_local, position, 1)
    mc_bit_scrubber = leastCommonBit(scrubber_rating_local, position, 0)

    for line in oxygen_generator_rating_local:
        if line[position] == str(mc_bit_oxygen):
            oxygen_generator_rating_new.append(line)

    for line in scrubber_rating_local:
        if line[position] == str(mc_bit_scrubber):
            scrubber_rating_new.append(line)

    if len(oxygen_generator_rating_local) > 1:
        oxygen_generator_rating_local = oxygen_generator_rating_new

    if len(scrubber_rating_local) > 1:
        scrubber_rating_local = scrubber_rating_new

    return[oxygen_generator_rating_local, scrubber_rating_local]


for i in range(0, length):
    [oxygen_generator_rating, scrubber_rating] = downSelectArray(
        oxygen_generator_rating, scrubber_rating, i)

oxygen_generator_rating_dec = int(
    "".join(str(x) for x in oxygen_generator_rating[0].strip('\n')), 2)

scrubber_rating_dec = int(
    "".join(str(x) for x in scrubber_rating[0].strip('\n')), 2)

answer = oxygen_generator_rating_dec * scrubber_rating_dec

print("Answer: ", answer)
