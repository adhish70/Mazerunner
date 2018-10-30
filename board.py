from collections import OrderedDict
from graphics import *
from random import randint


def path_tiles(position, path_prob, window, px_size, padding, maze_prob, win):
    """
    Generate tiles for the maze
    :param position: coordinate of tile
    :param path_prob: probability if path or obstacle
    :param window: size of window
    :param px_size: tile size
    :param maze_prob: probability for obstacles
    """
    x, y = position
    rect = Rectangle(Point(x, y), Point(x + px_size, y + px_size))
    if (x == padding and y == padding) or (x == window-px_size and y == window-px_size):
        rect.setFill("red")
        prob_value = False
    else:
        if path_prob >= maze_prob:
            rect.setFill("white")
            prob_value = False
        else:
            rect.setFill("black")
            prob_value = True
    rect.draw(win)
    return prob_value


def build_maze(maze_prob, size):
    """
    Get the maze size and generate maze
    :param size: dimension of the maze
    :param maze_prob: probability for obstacles
    """
    board_tiles = OrderedDict()
    px_size = 10
    padding = 5
    window = (px_size * size) + padding
    win = GraphWin('Mazerunner', window + padding, window + padding)

    for xpos in range(padding, window, px_size):
        for ypos in range(padding, window, px_size):
            path_prob = randint(0, 101) / 100
            position = (xpos, ypos)
            board_tiles[position] = path_tiles(position, path_prob, window, px_size, padding, maze_prob, win)

    visited_cells = board_tiles.copy()
    return visited_cells, window, padding, px_size, win
