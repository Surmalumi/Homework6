# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).

class Stationery :

    def __init__(self, title):
        self.title = title

    def draw (self):
        return f'Draw {self.title} go!'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Draw {self.title} pen!'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Draw {self.title} pencil!'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Draw {self.title} handle!'

pen = Pen("parker")
pencil = Pencil("bic")
handle = Handle("stabilo")

print(pen.draw())
print(pencil.draw())
print(handle.draw())