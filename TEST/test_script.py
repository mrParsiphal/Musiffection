import random

n = input()
ord_input = ''
for i in n:
    print(ord(i))
    ord_input = ord_input + str(ord(i))
print('ord_input: ', ord_input)
rand_bias = ''
len_ord_input = len(ord_input)
for i in range(len_ord_input):
    t = len_ord_input - i
    if t < 5:
        rand_bias = rand_bias + str(random.randint(1, 5 - t))
    else:
        rand_bias = rand_bias + str(random.randint(1, 5))
print('rand_bias: ', rand_bias)
t = 0
new_ord_password = int(ord_input[:int(rand_bias[t])])
print('new_ord_password[0]: ', new_ord_password)
ord_input = ord_input[1:]
while ord_input != '':
    t += 1
    first_term = new_ord_password * (10 ** (int(rand_bias[t]) - 1))
    second_term = int(ord_input[:int(rand_bias[t])])
    addition_rule = first_term % 10 + second_term // (10 ** (len(str(second_term)) - 1))
    if addition_rule > 9:
        new_ord_password = (first_term + 1) * 10 + addition_rule % 10
    else:
        new_ord_password = first_term + second_term
    ord_input = ord_input[1:]
    print(f'new_ord_password[{t}]: ', new_ord_password)
print('new_ord_password: ', new_ord_password)
