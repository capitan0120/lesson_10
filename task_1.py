class Descriptor:
    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} string bo'lishi kerak")

        if len(value) == 0:
            raise ValueError(f'{self.property_name} bo\'sh bo\'lmasligi kerak')
        instance.__dict__[self.property_name] = value
class Car:
    # model = Descriptor()
    # mamlakat = Descriptor()
    # yil = Descriptor()

    def __init__(self, model, mamlakat, yil):
        self.model = model
        self.mamlakat = mamlakat
        self.yil = yil

    def __str__(self):
        return f"Mashina modeli: {self.model}\nIshlab chiqarilgan mamlakati: {self.mamlakat}\nIshlab chiqilgan yili: {self.yil}"

car = Car("Cobalt", "O'zbekiston", "2016")
print(car)