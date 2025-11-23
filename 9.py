""" class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name}, {self.age} years old.")

    def greet_user(self):
        print(f"Oh, fucking {self.first_name.title()} {self.last_name}, I want to fuck you!")

Alice = User('alice', 'green', 20)
Alice.describe_user()
Alice.greet_user()

Bob = User('bob', 'blue', 21)
Bob.describe_user()
Bob.greet_user()
        
Clinton = User('clinton', 'white', 22)
Clinton.describe_user()
Clinton.greet_user() """


""" input_n = input("Please input some numbers: ")
n = input_n.split()
l = []
for i in n:
    if n.count(i) == 1:
        l.append(int(i))
print(l) """


""" def judge(n):
    if n <= 1 or not isinstance(n, int):
        return "Error!"
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True """

""" s = 0
for n in range(101, 201):
    if judge(n) == True:
        s += 1
        print(n)
print(s) """


""" s = 0
total = int(input("Please input the total amount: "))
for a in range(1, total//5+1):
    for b in range(1, total//2+1):
        for c in range(1, total//1+1):
            if a*5+b*2+c == total:
                s += 1
                print(f"fen5:{a}, fen2:{b}, fen1:{c}, total:{a+b+c}")
print(f"Count = {s}") """


""" def sum(i):
    s = 0
    for i in range(1, i+1):
        s += i/(i+1)
    return s
print(sum(1)) """


""" for p in range(1, 32):
    if judge(2**p-1) == True:
        print(2**p-1) """


""" def sum(a, n):
    s = 0
    for i in range(1, n+1):
        s += a*10**(i-1)
    if n >= 2:
        s += sum(a, n-1)
    return s
print(sum(2, 3)) """


""" x = input("Please enter a string: ")
def func(x):
    a, b, c, d = 0, 0, 0, 0
    for i in x:
        if i >= 'A' and i <= 'Z':
            a += 1
        elif i >= 'a' and i <= 'z':
            b += 1
        elif i >= '0' and i <= '9':
            c += 1
        else:
            d += 1
    print(f"Uppercase letters: {a}, Lowercase letters: {b}, Digits: {c}, Others: {d}")
    return
func(x) """


""" l = [1, 1, 2, 3, 4, 9, 5, 0, 3]
for i in l:
    if l.count(i) > 1:
        continue
    else:
        if l.index(i) == i:
           print(i) """


""" for n in range(10000, 100000):
    n_str = str(n)
    if len(set(n_str)) != 5:
        continue
    reverse_str = n_str[::-1]
    for G in range(1, 10):
        if n * G == int(reverse_str):
            A, B, C, D, E = n_str
            print(f"A: {A}, B: {B}, C: {C}, D: {D}, E: {E}, G: {G}")
            break """


""" import string
input_str = input("Please input a string: ")
translator = str.maketrans('', '', string.punctuation)
input_str = input_str.translate(translator)
u_str = input_str.split()
def func(u_str):
    keys = sorted(list(set(u_str)))
    values = [u_str.count(i) for i in keys]
    d = dict(zip(keys, values))
    return d
print(func(u_str)) """


""" def count(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 4
    if n == 4:
        return 5
    if n >= 5:
        return count(n-1) + count(n-4)
print(count(9)) """   