name = "Наталья"
age = 25
print(f"{name} , {age}")
print(age)

second_name = input("Фамилия? ")
place = input("Где? ")
hight = int(input("Рост? "))
weight = int(input("Вес? "))
print(f"{second_name}, {place}, {hight}, {weight}")

user_time = int(input("Время в секундах? "))
user_hours = user_time // 3600
user_minutes = user_time % 3600 // 60
user_seconds = user_time % 3600 % 60
print(f"{user_hours}:{user_minutes}:{user_seconds}")

n = int(input("Введите число от 1 до 9: "))
result = n + (n*10 + n) + (n*100 + n*10 + n)
print(result)

n = int(input("Введите число: "))
m = 0

while (n):
    if (n % 10 > m):
        m = n % 10
    n //= 10

print(m)

company_revenue = int(input("Выручка? "))
company_costs = int(input("Издержки? "))
if company_revenue > company_costs:
    print("Прибыль")
    company_profit = (company_revenue - company_costs) / company_revenue
    staff_quantity = int(input("Количество работников? "))
    revenue_per_capital = company_revenue / staff_quantity
    print (f"Рентабельность =  {company_profit}")
    print(f"Прибыль на сотрудника = {revenue_per_capital}")
else:
    print("Убыток")

a = int(input("Результат в первый день? "))
b = int(input("Требуемый результат? "))
n = 1

while a < b:
    a = a + a*0.1
    n += 1
print(f"{n} - {b}")
