# Калькулятор V1 GitHub \\ Termux

what = input("Что делаем (+, -. *, /): ") # Блок действий

a = float(input("Введите первое число: ")) # Блок 
b = float(input("Введите второе число: ")) #    переменых
#  Блок вычислений
if what == "+":
    c = a + b
    print("Результат: +str(c)")
elif what == "-":
    c = a - b
    print("Результат: +str(c)")
elif what == "*":
    c = a * b
    print("Результат: +str(c)")
elif what == "/":
    c = a / b
    print("Результат: +str(c)")
else:
    print("Выбрана неверная операция!")
