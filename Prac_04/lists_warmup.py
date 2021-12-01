numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])

if "3" in numbers:
    print("Yes")
else:
    print("no")
print(numbers + [6, 5, 3])
# Change the first element of numbers to "ten" (the string, not the number 10)

numbers[0] = "ten"
print(numbers)

# Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# Get all the elements from numbers except the first two (slice)
sliced_numbers = numbers[2:]
print(sliced_numbers)

# Check if 9 is an element of numbers
if 9 in numbers:
    print("Yes")
else:
    print("No")


