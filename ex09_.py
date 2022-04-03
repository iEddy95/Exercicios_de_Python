salarios = [200, 210, 290, 350, 370, 480, 520, 550, 600, 700, 790, 800, 820, 850, 870, 900, 999, 1000, 1150, 1500, 2000, 2500, 3000]
x = [0] * 9

for salario in salarios:
    i = salario // 100 - 2
    iM = len(x) - 1
    i = min(i, iM)
    x[i] += 1
    print(i)

print(x)