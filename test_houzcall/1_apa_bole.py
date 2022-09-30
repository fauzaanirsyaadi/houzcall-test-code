# looping 1 until 100
# 1. if the number is divisible by 3, print "apa"
# 2. if the number is divisible by 5, print "bole"
# 3. if the number is divisible by 3 and 5, print "apabole"
# 4. if the number is not divisible by 3 or 5, print the number
# 5. print the result in one line

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('ApaBole', end=' ')
    elif i % 3 == 0:
        print('Apa', end=' ')
    elif i % 5 == 0:
        print('Bole', end=' ')
    else:
        print(i, end=' ')