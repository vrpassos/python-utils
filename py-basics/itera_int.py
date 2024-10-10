def iterate(n):
    for i in range(n):
        print(i+1, end=' ')
    else:
        print()

def input_int():
    while True:
        val = input('Repetições: ')    
        if val.isnumeric():
            iterate(int(val))
            break
        else:
            print("Não é um número.")

input_int()    