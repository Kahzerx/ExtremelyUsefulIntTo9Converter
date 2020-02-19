
try:
    inp = int(input('Type a number with more than 1 digit: '))

    if inp < 10:
        print('That number is not bigger than 9 :(')
        
    else:
        while len(list(str(inp))) > 1:
            add = 0
            for num in list(str(inp)):
                add += int(num)
            inp -= add
            print(inp)

except:
    print('Thats not an integer ;(')
