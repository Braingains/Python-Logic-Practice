numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

for value in numbers:
    if (value % 2) == 0:
        print(value)
#for loop iterates through list, if there is no remainder when divided by 2 it must be even, print.

print(max(numbers) - min(numbers))
#prints the largest int in list - smallest int in list.

for left in numbers:
    for right in numbers:
        if (left == 2) and (right == 2):
            print(True)
# I think this wrong but it's almost midnight. It's a bubble sort algorithm. Don't know why it outputs four trues

