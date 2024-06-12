import time

import pygame as pg
import random

#pyinstaller --noconsole --onefile Snake.py

def Start():
    try:
        pg.init()

        block_size = 25

        screen = pg.display.set_mode((block_size * 35, block_size * 25))  # создание окошка

        fps = 5
        clock = pg.time.Clock()

        start_x = 3 * block_size
        start_y = 4 * block_size

        snake = []

        mo = 0

        for i in range(1, 2):
            new_block = [start_x + block_size * i, start_y]
            snake.append(new_block)

        direction = "right"

        image_mode = True

        if image_mode == True:

            body = pg.image.load("body.png")
            body = pg.transform.scale(body, (block_size, block_size))

            head = pg.image.load("head.png")
            head = pg.transform.scale(head, (block_size, block_size))

        background = pg.image.load("background.png")
        background = pg.transform.scale(background, (screen.get_width(), screen.get_height()))

        apple_x = random.randrange(0, screen.get_width(), block_size)
        apple_y = random.randrange(0, screen.get_height(), block_size)

        apple_2x = random.randrange(0, screen.get_width(), block_size)
        apple_2y = random.randrange(0, screen.get_height(), block_size)

        apple = pg.image.load("mouse.png")
        apple = pg.transform.scale(apple, (block_size, block_size))

        f1 = pg.font.Font(None, 30)



        play = True

        pause = False
        z = 0
        x = 2
        x1 = 1
        x2 = 1
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if (event.key == pg.K_LEFT or event.key == pg.K_a) and (not( [snake[-1][0] - block_size, snake[-1][1]] in snake)):  # проверяем, что нажимаем на клавиатуру
                        direction = "left"
                    if (event.key == pg.K_RIGHT or event.key == pg.K_d) and (not( [snake[-1][0] + block_size, snake[-1][1]] in snake)):  # проверяем, что нажимаем на клавиатуру
                        direction = "right"
                    if (event.key == pg.K_UP or event.key == pg.K_w) and (not( [snake[-1][0], snake[-1][1] - block_size] in snake)):  # проверяем, что нажимаем на клавиатуру
                        direction = "up"
                    if (event.key == pg.K_DOWN or event.key == pg.K_s) and (not( [snake[-1][0], snake[-1][1] + block_size] in snake)):  # проверяем, что нажимаем на клавиатуру
                        direction = "down"

            if pause:
                continue

            if snake[-1] in snake[:-1]:
                play = False
                text = f1.render("ВЫ ПРОИГРАЛИ", True, pg.Color("black"))
                screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
                pg.display.flip()
                clock.tick(fps)
                for i in range(3, 0, -1):
                    screen.blit(background, (0, 0))
                    text = f1.render(f"Перезапуск. Старт через {i}", True, pg.Color("black"))
                    screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
                    pg.display.flip()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            quit()
                    clock.tick(1)
                Start()

            if direction == "left":
                old_block = snake[-1]
                new_block = [old_block[0] - block_size, old_block[1]]
                snake.append(new_block)

            if direction == "right":
                old_block = snake[-1]
                new_block = [old_block[0] + block_size, old_block[1]]
                snake.append(new_block)
            if direction == "up":
                old_block = snake[-1]
                new_block = [old_block[0], old_block[1] - block_size]
                snake.append(new_block)
            if direction == "down":
                old_block = snake[-1]
                new_block = [old_block[0], old_block[1] + block_size]
                snake.append(new_block)
            if snake[-1][0] + block_size == 0 or snake[-1][1] + block_size == 0 or snake[-1][0] == screen.get_width() or snake[-1][1] == screen.get_height():
                    if snake[-1][1] + block_size == 0:
                        old_block = snake[-1]
                        new_block = [old_block[0], screen.get_height() - block_size]
                        snake.append(new_block)
                        del snake[0]
                    if snake[-1][0] + block_size == 0:
                        old_block = snake[-1]
                        new_block = [ screen.get_width() - block_size, old_block[1]]
                        snake.append(new_block)
                        del snake[0]
                    if snake[-1][0] == screen.get_width():
                        old_block = snake[-1]
                        new_block = [0, old_block[1]]
                        snake.append(new_block)
                        del snake[0]
                    if snake[-1][1] == screen.get_height():
                        old_block = snake[-1]
                        new_block = [old_block[0], 0]
                        snake.append(new_block)
                        del snake[0]


            if (apple_x == snake[-1][0] and apple_y == snake[-1][1] and x1 == 1) or (apple_2x == snake[-1][0] and apple_2y == snake[-1][1] and x2 == 1) :
                if (apple_x == snake[-1][0] and apple_y == snake[-1][1]) and x1 == 1:
                    x1 = 0
                    x -= 1
                elif (apple_2x == snake[-1][0] and apple_2y == snake[-1][1]):
                    if x2 == 1:
                        x2 = 0
                        x -= 1
                if x == 0:
                    for i in range(2):
                        apple_x = random.randrange(0, screen.get_width(), block_size)
                        apple_y = random.randrange(0, screen.get_height(), block_size)
                        apple_2x = random.randrange(0, screen.get_width(), block_size)
                        apple_2y = random.randrange(0, screen.get_height(), block_size)
                        x1, x2 = 1, 1
                        x = 2
                        fps += 1
                        z = 0

            else:
                del snake[0]
                z += 1
                if z == 30:
                    fps -= 1
                    z = 0
            if fps < 5:
                fps = 5
            if fps > 10:
                fps = 10

            z1 = [apple_x, apple_y]
            z2 = [apple_2x, apple_2y]
            if z1 in snake:
                if mo < 10:
                    apple_x = random.randrange(0, screen.get_width(), block_size)
                    apple_y = random.randrange(0, screen.get_height(), block_size)
                    mo += 1
                else:
                    mo = 0
            if z2 in snake:
                if mo < 10:
                    apple_2x = random.randrange(0, screen.get_width(), block_size)
                    apple_2y = random.randrange(0, screen.get_height(), block_size)
                    mo += 1
                else:
                    mo = 0

            screen.blit(background, (0, 0))


            if image_mode == True:
                for snake_block in snake:
                    screen.blit(body, (snake_block[0], snake_block[1]))

                screen.blit(head, (snake[-1][0], snake[-1][1]))
            else:
                for snake_block in snake:
                    pg.draw.rect(screen, pg.Color("green"), (snake_block[0], snake_block[1], block_size, block_size))

            if x1 == 1:
                screen.blit(apple, (apple_x, apple_y))
            if x2 == 1:
                screen.blit(apple, (apple_2x, apple_2y))

            text = f1.render("Счёт: " + str(len(snake)) + ".  " + f"Скорость: {fps}.", True, pg.Color("black"))
            screen.blit(text, (0, 0))
            if len(snake) >= 875:
                for i in range(3):
                    text = f1.render("ВЫ ВЫЙГРАЛИ ", True, pg.Color("red"))
                    screen.blit(text, (15 * block_size, 12 * block_size))
                    pg.display.flip()
                    clock.tick(1)
                for i in range(3, 0, -1):
                    screen.blit(background, (0, 0))
                    text2 = f1.render(f"Перезапуск. Старт через {i}", True, pg.Color("black"))
                    screen.blit(text2, text2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
                    pg.display.flip()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            quit()
                    clock.tick(1)
                Start()

            pg.display.flip()
            clock.tick(fps)
    except:
        pass
Start()