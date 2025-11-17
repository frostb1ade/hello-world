class User:
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
Clinton.greet_user()