arr = []
M = 50
N = 0
diff = (M-N)+2
for x in range(diff):
    y = x
    x = x + N 
    if x != 0:
        if  x%3+x%5 == 0:
            if y == diff-1:
                arr.append('FizzBuzz.')
            else:
                arr.append('FizzBuzz,')
        else:
            if  x%3 == 0:
                if y == diff-1:
                    arr.append('Fizz.')
                else:
                    arr.append('Fizz,')
            elif x%5 == 0:
                if y == diff-1:
                    arr.append('Buzz.')
                else:
                    arr.append('Buzz,')
            else:
                if y == diff-1:
                    arr.append(x)
                else:
                    arr.append(x)
                    arr.append(",")
string = ''.join(str(z) for z in arr)
print(string)
