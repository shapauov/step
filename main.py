a=1

while a<3:
    print("Hello")
    a += 1
else:
    print("Bye")


a = 0

while a < 20:
    a += 1
    if a == 10:
        continue # break
    print("Значение переменной А = ", a)

power = 0
while power <= 20:
    print(2**power)
    power += 1

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

print("Добро пожаловать в Додо пиццу!")

print("1. Пицца\n2. Напитки\n3. Выйти")

choice = int(input('Выберите пункт меню: '))

while choice != 3:
    if choice == 1:
        print("Вы выбрали пиццу")
    elif choice == 2:
        print("Вы выбрали напиток")
    else:
        print("Такого пункта нет")
    print("1. Пицца\n2. Напитки\n3. Выйти")
    choice = int(input('Выберите пункт меню: '))


languages = {'Python': 1, 'C++': 1, 'C': 1,
             'JS': 1, 'Java': 1, 'Php': 1, 'Rust': 1}
i = 1

for language in languages:
    print(f"{i}) {language}")
    i += 1
numbers = [0,1,2,3,4,5,6,7,8,9]

for i in numbers:
    print(i)

for i in range(10):
    print(i)


for i in range(2,20,2):
    print(i)
    
    
index = 2
while index < 20:
    print(index)
    index += 2