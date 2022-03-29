num = int(input('Deseja ver a tabuada de qual número? '))
mult = 0
for count in range (10):
    mult = mult + 1
    res = num*mult
    print(f'{num} X {mult} = {res}')