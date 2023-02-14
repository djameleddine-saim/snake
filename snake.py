import pygame
import sys
import random


pygame.init()
FPS = 15
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
VELOCITY = 10
SNAKE_WIDTH = 15
APPLE_SIZE = 20
TOP_WIDTH = 40
small_font = pygame.font.SysFont('forte', 25)
medium_font = pygame.font.SysFont('showcard gothic', 30, True)
large_font = pygame.font.SysFont('chiller', 50, True, True)
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('jeu de snake')
snake_img = pygame.image.load('snake2.png')
apple_img = pygame.image.load('apple2.png')
tail_img = pygame.image.load('tail1.png')
apple_img_rect = apple_img.get_rect()

pygame.mixer.music.load('snake_theme.mp3')


def start_game():
    canvas.fill(BLACK)
    start_font1 = large_font.render("Bienvenue au jeu de snake", True, GREEN)
    start_font2 = medium_font.render("Nouveau jeu", True, RED, YELLOW)
    start_font3 = medium_font.render("Quit", True, RED, YELLOW)
    start_font4 = medium_font.render("score", True, RED, YELLOW)

    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()

    start_font1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
    start_font2_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 50)
    start_font3_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 150)
    start_font4_rect.center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2 + 100)


    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        score()
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        pygame.quit()
                        sys.exit()


        pygame.display.update()


def gameover(show_score):
    canvas.fill(BLACK)

    font_gameover1 = large_font.render('GAME OVER', True, GREEN)
    font_gameover2 = medium_font.render("MENU", True, RED, YELLOW)
    font_gameover3 = medium_font.render("Quit", True, RED, YELLOW)
    font_gameover4 = medium_font.render('Enregistre votre score', True, RED, YELLOW)

    font_gameover1_rect = font_gameover1.get_rect()
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover3_rect = font_gameover3.get_rect()
    font_gameover4_rect = font_gameover4.get_rect()


    font_gameover1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
    font_gameover2_rect.center = (WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 20)
    font_gameover3_rect.center = (WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 70)
    font_gameover4_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 150)


    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)
    canvas.blit(font_gameover4, font_gameover4_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > font_gameover2_rect.left and x < font_gameover2_rect.right:
                    if y > font_gameover2_rect.top and y < font_gameover2_rect.bottom:
                        start_game()
                if x > font_gameover4_rect.left and x < font_gameover4_rect.right:
                    if y > font_gameover4_rect.top and y < font_gameover4_rect.bottom:
                        add_name_score(show_score)
                if x > font_gameover3_rect.left and x < font_gameover3_rect.right:
                    if y > font_gameover3_rect.top and y < font_gameover3_rect.bottom:
                        pygame.quit()
                        sys.exit()


        pygame.display.update()



def add_name_score(score):
    canvas.fill(BLACK)

    font_gameover2 = medium_font.render("Tapez votre nom puis sur ENTER : ", True, RED, YELLOW)
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover2_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    canvas.blit(font_gameover2, font_gameover2_rect)


    font = pygame.font.Font(None, 32)

    nom = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    nom += event.unicode
                elif event.key == pygame.K_RETURN:
                    with open("score_nom.txt", "a") as f:
                        f.write(f"{nom} : {score - 3}\n")
                    start_game()

        text = font.render(nom, True, (255, 255, 255))
        canvas.blit(text, (WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2 + 100))


        pygame.display.update()


def snake(snakelist, direction):

    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        tail = pygame.transform.rotate(tail_img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
        tail = pygame.transform.rotate(tail_img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        tail = pygame.transform.rotate(tail_img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    canvas.blit(tail, snakelist[0])

    for XnY in snakelist[1:-1]:
        pygame.draw.rect(canvas, BLUE, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))


def score():
    canvas.fill(BLACK)

    with open("score_nom.txt", "r") as file:
        lines = file.readlines()

        y = 50

        for line in lines:
            score_text = medium_font.render(line.strip(), True, (255, 255, 255))
            score_rect = score_text.get_rect()
            score_rect.center = (WINDOW_WIDTH / 2, y)
            canvas.blit(score_text, score_rect)

            y += 50

    start_inst5 = medium_font.render("<<BACK", True, RED, YELLOW)
    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (WINDOW_WIDTH - start_inst5_rect.width / 2, WINDOW_HEIGHT - start_inst5_rect.height / 2)
    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()


def game_paused():
    paused_font1 = large_font.render("Jeu en pause", True, RED)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(paused_font1, paused_font_rect1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        return
        pygame.display.update()


def gameloop():

    while True:

        pygame.mixer.music.play(-1, 0.0)

        LEAD_X = 0
        LEAD_Y = 100
        direction = 'right'
        score = small_font.render("Score:0", True, YELLOW)
        APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
        APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
        snakelist = []
        snakelength = 3
        pause_font = medium_font.render('II', True, RED)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                            pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            game_paused()
            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    gameover(snakelength)
            if direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > WINDOW_HEIGHT - SNAKE_WIDTH:
                    gameover(snakelength)
            if direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > WINDOW_WIDTH - SNAKE_WIDTH:
                    gameover(snakelength)
            if direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    gameover(snakelength)

            snakehead = []
            snakehead.append(LEAD_X)
            snakehead.append(LEAD_Y)
            snakelist.append(snakehead)

            snake_head_rect = pygame.Rect(LEAD_X, LEAD_Y, SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)


            if len(snakelist) > snakelength:
                del snakelist[0]
            for point in snakelist[:-1]:
                if point == snakehead:
                    gameover(snakelength)

            canvas.fill(BLACK)

            snake(snakelist, direction)
            if snake_head_rect.colliderect(apple_rect):
                APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
                APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
                snakelength += 1
                score = small_font.render("Score:" + str(snakelength - 3), True, YELLOW)



            canvas.blit(score, (20, 10))
            pygame.draw.line(canvas, GREEN, (0, TOP_WIDTH), (WINDOW_WIDTH, TOP_WIDTH))
            pygame.draw.line(canvas, YELLOW, (WINDOW_WIDTH - 60, 0), (WINDOW_WIDTH - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, YELLOW, (WINDOW_WIDTH - 60, 0, 60, TOP_WIDTH))
            canvas.blit(pause_font, (WINDOW_WIDTH - 45, 10))
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            pygame.display.update()

            clock.tick(FPS)



start_game()
gameloop()
