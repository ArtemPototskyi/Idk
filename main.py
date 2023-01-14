import pygame
import os
pygame.init()

def path_file(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path

WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 40

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
fon = pygame.image.load(path_file("videogamebackground1.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))

win_picture = pygame.image.load(path_file("winningscreen.jfif"))
win_picture = pygame.transform.scale(win_picture, (WIN_WIDTH, WIN_HEIGHT))

#pygame.mixer.music.load(path_file("backgroundmusic.html"))
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play()

#music.win = pygame.mixer.Sound(path_file("victorysound.html"))

#music.loss = pygame.mixer.Sound(path_file("defeatsound.html"))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def __init__(self, x, y, width, height, file_name, speed, direction, min_coord, max_coord) 
        super().__init__(x, y, width, height, file_name)
        self.speed = speed
        self.direction = direction
        self.min_coord = min_coord
        self.max_coord = max_coord

    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed
            if self.direction == "right":
                self.rect.x += self.speed

            if self.rect.right >= self.max_coord:
                self.direction = "left"
            if self.rect.left  <= self.min_coord:
                self.direction = "right"

        elif self.direction == "up" or self.destruction == "down":
            if self.direction == "down":
                self.rect.y += self.speed
            if self.direction== "up":
                self.rect.y -= self.speed

            if self.rect.top <= self.min_coord
                self.direction = "down"
            if self.rect.bottom >= self.max_coord
                self.direction = "up"

class Player(GameSprite):
    def __init__(self, x, y, width, height, img):
        super().__init__(x, y, width, height, img)
        self.speed_x = 0
        self.speed_y = 0
        self.direction = "right"
        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.speed_x > 0 and self.rect.right < WIN_WIDTH or self.speed_x < 0 and self.rect.left > 0:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        elif self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)        

        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
        elif self.speed_y < 0:
            for walls in touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)

player = Player(100, 100, 50, 50, path_file("knight1.jfif"))
enemy = GameSprite(400, 400, 70, 70, path_file("enemy.jpg"), 4, "up", 200, 400)
goal = GameSprite(715, 380, 100, 70, path_file("goal.png"))

walls = pygame.sprite.Group()
wall_1 = GameSprite(0, 210, 200, 20, path_file("walls.jpg"))
walls.add(wall_1)
wall_2 = GameSprite(250, 0, 20, 225, path_file("walls.jpg"))
walls.add(wall_2)
wall_3 = GameSprite(0, 0, 20, 430, path_file("walls.jpg"))
walls.add(wall_3)
wall_4 = GameSprite(250, 210, 100, 20, path_file("walls.jpg"))
walls.add(wall_4)
wall_5 = GameSprite(330, 225, 20, 125, path_file("walls.jpg"))
walls.add(wall_5)
wall_6 = GameSprite(250, 0, 20, 200, path_file("walls.jpg"))
walls.add(wall_6)
wall_7 = GameSprite(180, 225, 20, 125, path_file("walls.jpg"))
walls.add(wall_7)
wall_8 = GameSprite(100, 330, 100, 20, path_file("walls.jpg"))
walls.add(wall_8)
wall_9 = GameSprite(100, 280, 20, 50, path_file("walls.jpg"))
walls.add(wall_9)
wall_10 = GameSprite(330, 330, 275, 20, path_file("walls.jpg"))
walls.add(wall_10)
wall_11 = GameSprite(600, 0, 20, 350, path_file("walls.jpg"))
walls.add(wall_11)
wall_12 = GameSprite(0, 0, 800, 20, path_file("walls.jpg"))
walls.add(wall_12)
wall_13 = GameSprite(0, 410, 800, 20, path_file("walls.jpg"))
walls.add(wall_13)
wall_14 = GameSprite(685, 150, 20, 260, path_file("walls.jpg"))
walls.add(wall_14)
wall_15 = GameSprite(780, 0, 20, 410, path_file("walls.jpg"))
walls.add(wall_15)
game = True
play = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.speed_x = 5
                player.direction = "right"
                player.image = player.image_r
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.speed_x = -5
                player.direction = "left"
                player.image = player.image_l
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.speed_y = -5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.speed_y = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.speed_x = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.speed_y = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.speed_y = 0           
    if play == True:
        window.blit(fon, (0, 0))
        player.reset()
        player.update()

        enemy.reset()
        enemy.update()
        
        goal.reset()

        walls.draw(window)

        if pygame.sprite.collide_rect(player, goal):
            play = False
            window.blit(win_picture, (0, 0))
            pygame.mixer.music.stop()
            music.win.play()

    clock.tick(FPS)
    pygame.display.update()
