# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Olá Python!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

n1 = int (input('Digite um valor: '))
n2 = int (input('Digite outro valor: '))
p = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma entre {} e {} vale {}'.format(n1, n2, p))
print('O produto é: {}, a divisão é: {}, a divisão inteira é: {}, e a exponenciação é: {}'.format(m, d, di, e))