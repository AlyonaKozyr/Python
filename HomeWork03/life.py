import pygame
from pygame.locals import *
import random


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        # Создание списка клеток
        self.cell_list(randomize=True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_cell_list(self.clist)
            self.update_cell_list(self.clist)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        if randomize:
            self.clist = [[random.randint(0, 1)
                           for i in range(self.cell_width)]
                          for i in range(self.cell_height)]
        else:
            self.clist = [[0 for i in range(self.cell_width)]
                          for i in range(self.cell_height)]
        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for r in range(self.cell_height):
            for c in range(self.cell_width):
                if clist[r][c]:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, cell):
        neighbours = []
        row, col = cell
        positions = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [1, -1], [1, 0], [1, 1], [0, -1]]
        for i in positions:
            if 0 <= row + i[0] < self.cell_height \
                    and 0 <= col + i[1] < self.cell_width:
                neighbours.append(self.clist[row + i[0]][col + i[1]])
        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = [[0 for i in range(self.cell_width)]
                     for i in range(self.height)]
        for r in range(self.cell_height):
            for c in range(self.cell_width):
                if cell_list[r][c]:
                    if 1 < self.get_neighbours((r, c)).count(1) < 4:
                        new_clist[r][c] = 1
                    else:
                        new_clist[r][c] = 0
                else:
                    if (self.get_neighbours((r, c)).count(1)) == 3:
                        new_clist[r][c] = 1
        self.clist = new_clist
        return self.clist


if __name__ == '__main__':
    game = GameOfLife(320, 240, 10)
    game.run()
