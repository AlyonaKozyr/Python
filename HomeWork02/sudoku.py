import random

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def display(values):
   """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
       print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
       if str(row) in '25':
            print(line)
            print()

def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    n = int(input())
    a = []
    b = 1
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(b)
            b += 1
    print(a)


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos
    return values[row]

def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos
    for i in range(len(values)):
        return values[[i][col]]


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    r = 3 * (row // 3)
    c = 3 * (col // 3)
    for i in range(3):
        return [values[r + i]]
    for j in range(3):
        return [values[c + j]]


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        if (grid[i].count('.') != 0):
            return (i, grid[i].index("."))
    return ()


def find_possible_values(grid, pos):
    """ Вернуть множество всех возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzles/puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """
    numb = set('123456789')
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    for i in range(9):
        if i in row:
            numb.remove(i)
            continue
        if i in col:
            numb.remove(i)
            continue
        for k in range(3):
            if i in block[k]:
                numb.remove(i)
        return numb


def solve(grid):
    """ Решение пазла, заданного в grid

    Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    pos = find_empty_positions(grid)
    row, col = pos
    if pos == ():
        return grid
    else:
        values = find_possible_values(grid, pos)
        if values == []:
            return None
        for i in values:
            grid[row][col] = i
            s = solve(grid)
            if s is not None:
                return grid
    grid[row][col] = '.'
    return None


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    s = set([i for i in range(1, 10)])
    for j in range(9):
        row = set(get_row(grid, (j, 0)))
        col = set(get_col(grid, (0, j)))
        if row != s:
            return False
        if col != s:
            return False
        for j in range(3):
            for k in range(3):
                block = set(get_block(grid, (j * 3, k * 3))[0] + get_block(grid, (j * 3, k * 3))[1] + get_block(grid, (j * 3, k * 3))[2])
                if block != s:
                    return False
        return True

def generate_sudoku(n):
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    n = 81 - n
    grid = [['.' for i in range(9)] for j in range(9)]
    grid = solve(grid)
    for elem in range(n):
        row = random.randrange(0, 9)
        col = random.randrange(0, 9)
        while grid[row][col] == '.':
            row = random.randrange(0, 9)
            col = random.randrange(0, 9)
        grid[row][col] = '.'
    return grid

if __name__ == '__main__':
    for fname in ('puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt'):
        grid = read_sudoku(fname)
        start = time.time()
        solve(grid)
        end = time.time()
        print(f'{fname}: {end-start}')