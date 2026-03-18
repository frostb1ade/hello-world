""" class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 100000

    def describe_restaurant(self):
        print(f"这家餐馆的名字是{self.restaurant_name}, 它的菜谱为{self.cuisine_type}。")

    def open_restaurant(self):
        print("这家餐馆正在营业哦，走过路过不要错过！")

    def set_number_served(self, number):
        if number >= 0:
            self.number_serverd = number
        else:
            print("哈哈弱智，还想坑老子")

    def increment_number_served(self, number):
        if number >= 0:
            self.number_serverd += number
        else:
            print("不要白费力气了，你阴不了我") """   

""" restaurant = Restaurant('ZZY', [1, 2, 3, 4])
restaurant.describe_restaurant() """

""" a = Restaurant('FYC', ['1', '2', '3'])
b = Restaurant("CK", ["吃大粪吧你"])
c = Restaurant("HJX", ["如果人生能重来，我一定不会让你坐在我旁边，一定如此，说到做到"])
a.describe_restaurant()
b.describe_restaurant()
c.describe_restaurant()  """

""" class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"Welcome, {self.first_name}·{self.last_name}!")

    def greet_user(self):
        print(f"Hello, {self.first_name}·{self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0 """

""" a = User('清雪', '林')
b = User('正阳', '张')
a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()   """       

""" restaurant = Restaurant('张氏菜馆', ['红烧大粪', '清蒸阴茎'])
restaurant.set_number_served(500)
print(restaurant.number_serverd)
restaurant.set_number_served(0)
print(restaurant.number_serverd)
restaurant.increment_number_served(6000)
print(restaurant.number_serverd) """

""" Zzy = User('正阳', '张')
Zzy.increment_login_attempts()
Zzy.increment_login_attempts()
Zzy.increment_login_attempts()
Zzy.increment_login_attempts()
print(Zzy.login_attempts)
Zzy.reset_login_attempts()
print(Zzy.login_attempts) """

""" class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['grape', 'milk', 'strawberry', 'chocolate']

    def show_flavours(self):
        print(f"我们的小店有{self.flavors}口味的冰淇淋，快来选购吧")

a = IceCreamStand('张氏冰淇淋', ['雪糕', '冰棍儿', '蛋筒'])
a.show_flavours()  """

""" class Admin(User):

    def __init__(self, first_name, last_name):
      super().__init__(first_name, last_name)
      self.privileges = Privileges() """

""" Zhang = Admin("正阳", "张")
Zhang.show_privileges() """

""" class Privileges:

    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
         print(f"管理员sama驾到！愚蠢的凡人啊，见识一下他的权能吧！{self.privileges}")

张 = Admin('正阳', '张')
张.privileges.show_privileges() """

 