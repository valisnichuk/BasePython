a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("id of a:", id(a))
print("id of b:", id(b))
print("id of c:", id(c))

print("a == b:", a == b)
print("a is b:", a is b)

print("a == c:", a == c)
print("a is c:", a is c)

print(a, b, c)
a.append(4)
b.append(9)
c.append(5)
print(a, b, c)

num_a = 1
num_b = 1

print("num_a == num_b", num_a == num_b)
print("num_a is num_b", num_a is num_b)

exists = True
print("a is list type?", isinstance(a, list))
print("a is list-like type?", isinstance(a, (list, tuple)), type(a))

t = ()
print("t is list-like type?", isinstance(t, (list, tuple)), type(t))

exists = True

print("type of exists:", type(exists))
print("'exists' is type of int?", isinstance(exists, int))
print("exists to int:", int(exists))
print("exists == 1?", exists == 1)

print("id of exists:", id(exists))
print("id of int 1:", id(int(1)))

def get_list(input_list=None):
    if input_list is None:
        input_list = []

    return input_list

empty_list = []
res = get_list()
print("empty list is res?", empty_list is res)
print("empty list == res?", empty_list == res)
print("empty list is res?", empty_list is get_list(empty_list))

print("type(a)", type(a))
print("type(a) is type(b)", type(a) is type(b))
print("type(a) is type(c)", type(a) is type(c))

print('test')



