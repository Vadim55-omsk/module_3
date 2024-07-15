#1. Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(1, 'строка', True)
print_params()

#2. Распаковка параметров:

values_list = [67, ['tu', 'rt'], "string"]
def print_params (*values_list):
    print(*values_list)
print_params(*values_list)

values_dict = {'Piotr':28, 'Oleg':82, 'Jon':48}
def print_params (**values_dict):
    print(values_dict)
print_params(**values_dict)

#3. Распаковка + отдельные параметры:

values_list2  = [65.87, 'String']
def print_params (*values_list2):
    print(*values_list2)
print_params(*values_list2, 42)


