"""
Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print statements to see the results. You should create four lines that look
like this:

print(5 + 3)

Your output should simply be four lines with the number 8 appearing once
on each line.
"""

import logging

logger = logging.getLogger(__name__)

print(5 + 3)
print(2 * 4)
print(float(10 - 2))
print(int(16 / 2))

divisor = 0

try:
    print(5 / divisor)
except ZeroDivisionError as e:
    logger.error("messgee %s" % e)
    divisor = 1


"""
Favorite Number: Store your favorite number in a variable. Then, using
that variable, create a message that reveals your favorite number. Print that
message.
"""

my_lucky_number = 99

my_message = f"Hey my lucky number is {my_lucky_number}"

print(my_message)
