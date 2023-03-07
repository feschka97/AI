class Car:
    def __init__(self, engine, interior, x, y, started):
        self._engine = engine
        self._interior = interior
        self._x = x
        self._y = y
        self._started = 0
    def __str__(self): return f"Я машина, у меня координаты: {self._x},{self._y}"
    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, v):
        if v.horsepower < 0 or v.litrage < 0:
            return ValueError
        else:
            self = v

    def move(self, x, y):
        self._x += x
        self._y += y

    def start(self):
        if self._started:
            self._started = False
        else:
            self._started = True

    @property
    def interior(self):
        return self._interior

    @interior.setter
    def interior(self, v):
        if v.shift < 2:
            return ValueError
        else:
            self = v


class Engine:
    def __init__(self, horsepower, volume):
        self._horsepower = horsepower
        self._volume = volume

    def get_horsepower(self):
        return self._horsepower

    def get_volume(self):
        return self._volume
    def __str__(self): return f"Я движок, у меня {self._horsepower} лс и {self._volume} л"


class Interior:
    def __init__(self, material, passengers):
        self._material = material
        self._passengers = passengers

    def get_material(self):
        return self._material

    def get_passengers(self):
        return self._passengers

    def __str__(self): return f"Я интерьер, у меня обивка из {self._material}, пассажиров - {self._passengers}"
