count = 1
total = 0

# BUG: Missing colon at end of while line, added : to fix SyntaxError
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Original condition was count < 5 so it only summed 1-4 = 10, changed to count <= 5 to include 5
# BUG: Can't concatenate string + int with +, changed to str(total) to fix TypeError
print("Sum of 1 to 5 is: " + str(total))