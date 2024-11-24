def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(2, 3, 4)
print_params(b=25)
print_params(c=[1, 2, 3])
#Распаковка параметров списков и словарей
values_list = [2, [2, "ok"], "Dog"]
print(values_list)
print(type(values_list))
print(*values_list)

values_dict = {'a': 2, 'b': [2, "ok"], 'c': "Dog"}
print_params(**values_dict)
print(type(values_dict))
#Распаковка + отдельные параметры

values_list_2 = ["Cat", 33]
print_params(*values_list_2, 55)


