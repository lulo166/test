def haven(n, r, g):
    grid = []
    for i in range(n**2):
        grid.append('empty')
    b = 1
    grid[0] = 'r'
    place = 0
    while b != n**2:
        for i in range(g):
            d = 0
            while d == 0:
                if place == n**2:
                    place = 0
                if grid[place] == 'empty':
                    d = 1
                    place += 1
                else:
                    place += 1
        grid[place] = 'g'
        b += 1
        if b != n**2:
            break
        for i in range(r):
            d = 0
            while d == 0:
                if place == n**2:
                    place = 0
                if grid[place] == 'empty':
                    d = 1
                    place += 1
                else:
                    place += 1
        grid[place] = 'r'
        b += 1
    return grid, 'Luca Lowenbach', 'Lycee International de Londres'



            


