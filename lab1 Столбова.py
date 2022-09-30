import math

# Ex. 1 (S2.1)
print("\033[32mEx. 1 Составить программу:\nа) вычисления значения функции y=7x2+3x+6 при любом значении x;\n"
      "б) вычисления значения функции x=12a2+7a+12 при любом значении а.\033[0m")


def calculate_func_1(x, y):
    print(f"x = {x}, y=7x2+3x+6={y}")


x = float(input("Enter x: "))
y = 7*(x**2)+3*x+6
calculate_func_1(x, y)


def calculate_func_2(a, b):
    print(f"a = {a}, b=x=12a2+7a+12={b}")


a = float(input("Enter a: "))
b = 12*(a**2)+7*a+12
calculate_func_2(a, b)


# Ex. 2 (S2.22)
print("\n\033[32mEx. 2 Известна стоимость 1 кг конфет, печенья и яблок."
      "\nНайти стоимость всей покупки, если купили x кг конфет, у кг печенья и z кг яблок.\033[0m")


def cost(x_cost, x_w, y_cost, y_w, z_cost, z_w):
    print(f"Whole cost for {x_w} kg of candies, "
          f"{y_w} kg of cookies and "
          f"{z_w} kg of apples is {x_cost*x_w+y_cost*y_w+z_cost*z_w}")


x_cost, x_weight = (25, 2)
y_cost, y_weight = (16, 3)
z_cost, z_weight = (50, 5)
cost(x_cost, x_weight, y_cost, y_weight, z_cost, z_weight)


# Ex. 3 (S2.24)

print("\n\033[32mEx. 3 Возраст Тани — Xлет, а возраст Мити —Yлет.\n"
      "Найти их средний возраст, а также определить, "
      "на сколько отличается возраст каждого ребенка от среднего значения.\033[0m")


def age(girl, boy):
    avg = (girl + boy) / 2
    print(f"Average age = {avg},\n"
          f"Girl`s difference {math.fabs(girl-avg)}\n"
          f"Boy`s difference {math.fabs(boy-avg)}")


girl = int(input("Enter girl`s age: "))
boy = int(input("Enter boy`s age: "))
age(girl, boy)


# Ex. 4 (S2.27)
print("\n\033[32mEx. 4 Известно значение температуры по шкале Цельсия.\n"
      "Найти соответствующеезначение температуры по шкале: а)Фаренгейта; б)Кельвина.\033[0m")


def temperature(celcius, fahrenheit, kelvin):
    print(f"Temperature in Celsius: {celcius}\n"
          f"Temperature in Fahrenheit: {fahrenheit}\n"
          f"Temperature in Kelvin: {kelvin}")


celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = celcius*1.8 + 32
kelvin = celcius + 273.15
temperature(celcius, fahrenheit, kelvin)


# Ex. 5 (S3.3)
print("\n\033[32mEx. 5 Дано вещественное число а.\nПользуясь только операцией умножения, получить:\n"
      "а)a4 за две операции;\nб)a6 за три операции;\nв)a7 за четыре операции;\n"
      "г)a8 за три операции;\nд)a9 за четыре операции;\nе)a10 за четыре операции.\033[0m\n")

d=25
d2 = d*d
d4 = d2*d2
print(f"a) d2 = d*d = {d2}\n   d4 = d2*d2 = {d4}\n")

d6 = d2*d4
print(f"б) d2 = d*d = {d2}\n   d4 = d2*d2 = {d4}\n   d6 = d2*d4 = {d6}\n")

d7 = d6*d
print(f"в) d2 = d*d = {d2}\n   d4 = d2*d2 = {d4}\n   d6 = d2*d4 = {d6}\n   d7 = d6*d = {d7}\n")

d8 = d4*d4
print(f"г) d2 = d*d = {d2}\n   d4 = d2*d2 = {d4}\n   d8 = d4*d4 = {d8}\n")

d9 = d8*d
print(f"д) d2 = d*d = {d2}\n   d4 = d2*d2 = {d4}\n   d8 = d4*d4 = {d8}\n   d9 = d8*d = {d9}\n")

d10 = d8*d2
print(f"е) d2 = d*d = {d2}\n   d4 = d2*d2 = {d4}\n   d8 = d4*d4 = {d8}\n   d10 = d8*d2 = {d10}\n")


