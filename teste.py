def iterate(n):
    for i in range(n):
        print(i+1)

while True:
    val = input('Repetições: ')
    
    if val.isnumeric():
        iterate(int(val))
        break
    else:
        print("Não é um número.")