import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Unbeatable Tic Tac Toe ')

running = True

game_grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
turn = 1
gameover = False

""" draw the game lines """
def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (200,0 ), (200,600))
    pygame.draw.line(screen, (255, 0, 0), (400, 0), (400, 600))
    pygame.draw.line(screen, (255, 0, 0), (0, 200), (600, 200))
    pygame.draw.line(screen, (255, 0, 0), (0, 400), (600, 400))
    pygame.display.update()

def findpos(pos):
    x = pos[0] // 200
    y = pos[1] // 200
    a = (x,y)
    return a

def mumkun(game_grid):
    moves = []
    for i in range(len(game_grid)):
        for j in range(len(game_grid[0])):
            if game_grid[i][j] == None:
                moves.append((i, j))
    return moves

def check_win(game_grid):
    for i in range(len(game_grid)):
        if game_grid[i][0] == game_grid[i][1] == game_grid[i][2]  and game_grid[i][1] != None:
            return game_grid[i][1]

    for i in range(len(game_grid)):
        if game_grid[0][i] == game_grid[1][i] == game_grid[2][i]  and game_grid[1][i] != None:
            return game_grid[1][i]

    if game_grid[0][0] == game_grid[1][1] == game_grid[2][2] and game_grid[1][1] != None:
        return game_grid[0][0]

    if game_grid[0][2] == game_grid[1][1] == game_grid[2][0] and game_grid[1][1] != None:
        return game_grid[0][2]

    return None

def cizici(game_grid,screen):
    for i in range(len(game_grid)):
        for j in range(len(game_grid[0])):
            if game_grid[i][j] == 'X':
                pygame.draw.line(screen, (255, 0, 0), (i*200,j*200), (i*200 + 200,j*200 + 200),10)
                pygame.draw.line(screen, (255, 0, 0), (i * 200+200, j * 200), (i * 200, j * 200 + 200),10)
            elif game_grid[i][j] == 'O':
                pygame.draw.circle(screen,(255, 0, 0),((i*200)+100,(j*200)+100),100,5)

            pygame.display.update()


def minimax(game_grid, depth,ismaximizing):
    winner = check_win(game_grid)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif len(mumkun(game_grid)) == 0:
        return 0

    if ismaximizing:
        bestscore = -float('inf')
        for i,j in mumkun(game_grid):
            game_grid[i][j] = 'X'
            """ Recursively find the best move """
            score = minimax(game_grid, depth + 1, False)
            """ take the move back """
            game_grid[i][j] = None
            bestscore = max(bestscore, score)
        return bestscore
    else:
        bestscore = float('inf')
        for i,j in mumkun(game_grid):
            game_grid[i][j] = 'O'
            score = minimax(game_grid, depth + 1, True)
            game_grid[i][j] = None
            bestscore = min(bestscore, score)
    return bestscore



""" Find best move and return the coordinates of the best move """
def findbestmove(game_grid):
    best_score = float('inf')
    bestmove = None
    if check_win(game_grid) is not None:
        return None
    for i,j in mumkun(game_grid):
        game_grid[i][j] = 'O'
        score = minimax(game_grid,0,True)
        game_grid[i][j] = None
        if score < best_score:
            best_score = score
            bestmove = (i,j)
    return bestmove


draw(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if not gameover:

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 1:
                hamle = mumkun(game_grid)
                pos = pygame.mouse.get_pos()
                a = findpos(pos)
                if a not in hamle:
                    print("oyuncu tıklanılan bir yere tıklamaya çalıştı")
                else:
                    game_grid[a[0]][a[1]] = 'X'
                    turn *= -1
                    cizici(game_grid, screen)
                    check = check_win(game_grid)
                    if check != None:
                        print(check)
                        gameover = True


                """ ai turn"""
            elif turn == -1:

                move = findbestmove(game_grid)
                if move is not None:
                    a, b = findbestmove(game_grid)
                    game_grid[a][b] = 'O'

                    turn *= -1

                    cizici(game_grid, screen)
                    check = check_win(game_grid)
                    if check != None:
                        print(check)
                        gameover = True
                    print(game_grid)









