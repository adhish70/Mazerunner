from board import *
from find_neighbours import *
from queue import Queue


def get_path(parent, src, dest, path, win):
    while parent[dest] != src:
        x, y = parent[dest]
        rec = Rectangle(Point(x, y), Point(x + 10, y + 10))
        rec.setFill("yellow")
        rec.draw(win)
        path.append(parent[dest])
        dest = parent[dest]
    path.reverse()
    return path


def print_path(parent, src, dest, win):
    print(get_path(parent, src, dest, [], win))


def get_tot_steps(parent, src, dest, win):
    tot_steps = len(get_path(parent, src, dest, [], win))
    return tot_steps + 1


def breadth_first_search(visited_copy, window, padding, px_size, win):
    visited = visited_copy.copy()
    iteration = 0
    max_fringe_size = 0
    parent = dict()
    dest_reachable = False
    q = Queue()
    source = (padding, padding)
    dest = (window - px_size, window - px_size)
    q.put(source)
    visited[source] = True
    # win = GraphWin('Mazerunner', window + padding, window + padding)

    while not q.empty():
        iteration = iteration + 1
        temp = q.get()

        if temp != source and temp != dest:
            rec = Rectangle(Point(temp[0], temp[1]), Point(temp[0] + px_size, temp[1] + px_size))
            rec.setFill("blue")
            rec.draw(win)

        if temp == dest:
            dest_reachable = True
            break

        nbours = return_neighbours(temp, window, padding, px_size)
        for element in nbours:
            if visited[element] is False:
                q.put(element)
                visited[element] = True
                parent[element] = temp

        if q.qsize() > max_fringe_size:
            max_fringe_size = q.qsize()

    if dest_reachable:
        # print('The destination is reachable.')
        return [True, get_tot_steps(parent, source, dest, win), iteration - 1, max_fringe_size, visited_copy]
    else:
        # print('The destination is not reachable.')
        return [False, None, None, None, None]

    # print('Number of nodes expanded: ', iteration - 1)
    #
    # print('Total steps from source to destination: ', get_tot_steps(parent, source, dest))
    #
    # print('Max fringe size: ', max_fringe_size)
    # print_path(parent, source, dest)


def bfs_main(visited, window, padding, px_size, win):
    dest_status = breadth_first_search(visited, window, padding, px_size, win)
    time.sleep(2)
    return dest_status
