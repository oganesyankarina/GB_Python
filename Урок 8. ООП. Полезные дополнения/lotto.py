from random import randint, choice

min_value = 1
max_value = 90


def generate_unique_keg(keg_list):
    """
    Функция для генерации боченка со случайным числом.
    :param keg_list: список доступных боченков
    :return: боченок со случайным числом из доступных
    """
    random_keg = choice(keg_list)
    keg_list.remove(random_keg)
    return random_keg


def generate_unique_number(count):
    """
    Функция для генерации случайных чисел для карточки.
    Все числа в карточке должны быть уникальными.
    :param count: необходимое количество случайных чисел
    :return: список случайных чисел
    """
    numbers_list = [x for x in range(min_value, max_value + 1)]
    numbers = []
    while len(numbers) < count:
        random_num = choice(numbers_list)
        numbers.append(random_num)
        numbers_list.remove(random_num)
    return numbers


class Card:
    lines = 3
    cells_in_line = 9
    num_in_line = 5

    def __init__(self):
        numbers = generate_unique_number(self.lines * self.num_in_line)
        self.data = []
        for line in range(self.lines):
            tmp = sorted(numbers[self.num_in_line * line: self.num_in_line * (line + 1)])
            empty_nums_count = self.cells_in_line - self.num_in_line
            for el in range(empty_nums_count):
                tmp.insert(randint(0, len(tmp)), '  ')
            self.data += tmp

    def __str__(self):
        border = '--------------------------'
        data = border + '\n'
        for index, num in enumerate(self.data):
            data += str(num)
            if (index + 1) % self.cells_in_line == 0:
                data += '\n'
            else:
                data += ' '
        return data + border

    def cross_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = ' -'

    def __contains__(self, item):
        return item in self.data


class Keg:
    keg_list = [x for x in range(min_value, max_value + 1)]

    def __init__(self):
        self.__num = randint(min_value, max_value + 1)
        self.keg_list.remove(self.__num)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.num)

    def generate_unique_keg(self):
        random_keg = choice(self.keg_list)
        self.keg_list.remove(random_keg)
        self.__num = random_keg
        return random_keg


class Game:
    def __init__(self):
        self.user_card = Card()
        self.comp_card = Card()
        self.keg = Keg()

    def start_play(self):
        print(f'Бочонок {self.keg}')
        print(f'Карточка игрока:\n{self.user_card}')
        print(f'Карточка компьютера:\n{self.comp_card}')

        user_answer = input(f'У вас есть цифра {self.keg}? (y/n)').lower()
        if user_answer == 'y' and self.keg.num not in self.user_card or \
                user_answer != 'y' and self.keg.num in self.user_card:
            print('Вы проиграли! Игра окончена!')
            return 3

        if self.keg.num in self.user_card:
            self.user_card.cross_num(self.keg.num)
            if self.user_card.data.count(' -') == self.user_card.lines * self.user_card.num_in_line:
                print('Вы победили! Поздравляем!')
                return 1
        if self.keg.num in self.comp_card:
            self.comp_card.cross_num(self.keg.num)
            if self.comp_card.data.count(' -') == self.comp_card.lines * self.comp_card.num_in_line:
                print('Победил компьютер! Игра окончена!')
                return 2
        self.keg.generate_unique_keg()
        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.start_play()
        if score != 0:
            break
    pass
