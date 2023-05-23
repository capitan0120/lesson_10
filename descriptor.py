class Car:
    def __init__(self, model, mamlakat, yil):
        self._model = model
        self._mamlakat = mamlakat
        self._yil = yil

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def mamlakat(self):
        return self._mamlakat

    @mamlakat.setter
    def mamlakat(self, value):
        self._mamlakat = value

    @property
    def yil(self):
        return self._yil

    @yil.setter
    def yil(self, value):
        self._yil = value

car = Car("Cobalt", "O'zbekiston", 2016)
print(car.model, car.mamlakat, car.yil)