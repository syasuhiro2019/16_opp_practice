class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def profile(self):
        return f'Name: {self.name}, Age: {self.age}'


if __name__ == '__main__':
    # クラスを使うイメージ
    bob = Person('Bob', 15)

    print(bob.profile())  # 'name:Bob, Age: 15'と出力されて欲しい

    tom = Person('Tom', 24)
    print(tom.profile())  # 'Name: Tom, Age: 24' と出力されて欲しい

    ken = Person('Ken', 42)
    print(ken.profile())
