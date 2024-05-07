def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params('строка', 2, False)
print_params(c=False)
print_params(b='число', c=False)
print_params(a=[1, 2, 3])
values_list = [1, 'список', False]
values_dict = {'a': 'словарь', 'b': 2, 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'Список']
print_params(*values_list_2, 42)