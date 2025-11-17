""" car = input("Please choose a car you want to rent: ")
print(f"Let me see if I can find a {car} for you.") """

""" guests = int(input("Please tell me how many people are in your dinner group: "))
if guests > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.") """

""" number = int(input("Please enter a number: "))
if number % 10 == 0:
    print("Yes!")
else:
    print("No!") """

""" prompt = "\nPlease choose a topping on your pizza: "
prompt += "\n(Enter 'quit when you are finished.)"
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza.") """

""" age = int(input("Please enter your age: "))
if age < 3:
        print("Your ticket is free.")
elif age <= 12:
        print("Your ticket is $10.")
else:
        print("Your ticket is $15.") """


""" print(2)
for n in range(3, 101, 2):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
         break
    else:
        print(n)  """

""" for n in range(1000, 0, -1):
    if n % 5 == 0 and n % 7 == 0:
        print(n)
        break  """

""" from collections import Counter
lst = list(input("Please enter some numbers").split()) 
n = [x for x, c in Counter(lst).items() if c == 1]
for e in n:
    print(int(e))  """

""" import random
lst = [random.randint(1,50) for _ in range(20)]
print(lst)
lst_1 = lst[:5]
lst = lst[5:20]
lst = lst + lst_1
print(lst) """

""" x = int(input("Please enter a number: "))
if x < 0:
    print(-1)
elif x == 0:
    print(0)
else:
    print(1) """

""" print("The pastrami has sold out.")
finished_sandwiches = []
sandwich_orders = ['pastrami', 'turkey', 'ham', 'pastrami', 'roast beef', 'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches) """


""" rezorts = {}
flag = True
while flag:
    name = input("\nPlease enter your name: ")
    rezort = input("Which rezort would you like to go to? ")
    rezorts[name] = rezort
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        flag = False
for name, rezort in rezorts.items():
    print(f"{name.title()} wants to go to {rezort.title()}.") """