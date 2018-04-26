#Example of for loops and range

print ('My name is')
for i in range (5):
    print ('Jimmy Five Times ' + str(i))

print ('My name is')
i = 0
while i < 5:
    print ('Jimmy Five Times ' + str(i))
    i = i + 1

print ('My name is')
for i in range (0, 10, 2): # The third argument: how many steps of range function.
    # In this case, count to 0 a 10, jump 2 on 2, whitout count the 10th
    print ('Jimmy Five Times ' + str(i))

print ('My name is')
for i in range (5, -1, -1):
    print ('Jimmy Five Times ' + str(i))

