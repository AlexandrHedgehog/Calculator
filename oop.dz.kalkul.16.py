# Калькулятор
# Создайте класс, где реализованы функции(методы)
# математических операцций.
# А также функция для ввода динамич данных.


class Matematic:
    def __init__(self):
        self.funkobsch()
    def funcplys(self):
        return self.a + self.c
    def funcminus(self):
        return self.a - self.c
    def funcumnozh(self):
        return self.a * self.c
    def funcdelen(self):
        if self.c == 0:
            return 'na nol nelzja'
        else:
            return self.a / self.c

    def funkobsch(self):
        self.a = int(input('vvedite chislo: '))
        self.c = int(input('vvedite chislo: '))

while True:
    print('Vvedite znak +, -, *, /')
    d = input('-- ')
    kalc = Matematic()
    if d == '0':
        print('Viberi znak a ne cifru')
        break
    if d == '+':
        print('Vash otvet: ', kalc.funcplys())
    if d == '*':
        print('Vash otvet: ', kalc.funcumnozh())
    if d == '-':
        print('Vash otvet: ', kalc.funcminus())
    if d == '/':
        print('Vash otvet: ', kalc.funcdelen())
