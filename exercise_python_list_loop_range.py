"""
Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
"""
for num in range(1, 21):
    print(f"My number is {num}")


"""
One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.)
"""
1, 2, 3, 4, 5
range(1, 6)

my_large_list = list(range(1, 1000000 + 1))
print(my_large_list)
for num in my_large_list:
    print(num)


"""
Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
"""
my_super_large_list = []
for num in range(1, 1000000 + 1):
    my_super_large_list.append(num)


print(min(my_super_large_list))
print(max(my_super_large_list))
print(sum(my_super_large_list))
