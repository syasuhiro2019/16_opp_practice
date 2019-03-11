class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * 3.14

    def circumference(self):
        return 2 * self.radius * 3.14


if __name__ == '__main__':
    # 半径が1の円
    circle = Circle(radius=1)

    # circle1の面積を求める
    print(circle.area())

    # circle2の面積を求める
    circle2 = Circle(20)
    print(circle2.area())

    len = int(input('半径の長さは? >'))
    circle3 = Circle(len)
    print(f'面積は:{circle3.area()}')

    # 直径を求める

    print(f'直径は:{circle.circumference()}')

    print(circle.radius)
