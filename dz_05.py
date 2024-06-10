fruits = {
    "Яблоко": {"цвет": "красный", "доступность": "да"},
    "Банан": {"цвет": "желтый", "доступность": "нет"}
}
print("Исходный словарь:")
print(fruits)
fruits["Киви"] = {"цвет": "зеленый", "доступность": "да"}
print(fruits)
fruits["Банан"]["доступность"] = "да"
print(fruits)
del fruits["Яблоко"]
print(fruits)


tuple_data = ("яблоко", "банан", "киви", "апельсин")

second_element = tuple_data[1]

tuple_data[0] = "груша"  # TypeError: 'tuple' object does not support item assignment

set_data = set(tuple_data)  
set_data.add("груша")  
set_data.discard("банан")  

# Операции с множествами
another_set = {"апельсин", "мандарин", "грейпфрут"}
intersection = set_data.intersection(another_set)  
union = set_data.union(another_set) 
difference = set_data.difference(another_set) 

print("Исходный кортеж:", tuple_data)
print("Второй элемент кортежа:", second_element)
print("Множество после добавления и удаления:", set_data)
print("Пересечение множеств:", intersection)
print("Объединение множеств:", union)
print("Разница между множествами:", difference)


