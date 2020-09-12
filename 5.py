import pygame
import random


pygame.init()

WIDTH = 720
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHOOT")

screen.fill((0, 0, 0))
pygame.display.update()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen.fill(BLACK)
pygame.display.update()

clock = pygame.time.Clock()
fps = 100

def draw_text(surf, text, size, x, y):
    font2 = pygame.font.SysFont("comicsans.ttc", size)
    img2 = font2.render(text, True, WHITE)
    surf.blit(img2, (x, y))

def wait(sec):
    on = 1
    for one in range(0, sec):
        pygame.time.wait(on)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            on = 0
        else:
            pass




def retry():
    pass


def intro():
    screen.fill((0, 0, 0))
    draw_text(screen, "Gullible Humans advaced Technology to an unprecented degree", 25, 60, HEIGHT / 2 - 31)
    draw_text(screen,"forming Spaceships that can reach the AQI they did not know that", 25, 60, HEIGHT / 2)
    draw_text(screen, "their first little step would be the start of the CHAOS ERA... ", 25, 60, HEIGHT / 2+ 31)
    pygame.display.update()
    wait(9000)
    screen.fill((0, 0, 0))
    draw_text(screen, "Life Forms retaliated against Humanity for resoures, rising in the", 25, 60, HEIGHT / 2- 31)
    draw_text(screen, "CHAOS chosen humans gained their GEN powers. As Time passed Humanity", 25, 60, HEIGHT / 2)
    draw_text(screen,
              "continued to wither due to the Scaren race, Humanity need its Hero...",
              25, 60, HEIGHT / 2 + 31)
    pygame.display.update()
    wait(9000)
    screen.fill((0, 0, 0))
    draw_text(screen, "Do you want to become a Hero? ", 55, 130,HEIGHT / 2 - 56)
    draw_text(screen, " Then Fight! ", 60, 250, HEIGHT / 2 )
    pygame.display.update()
    wait(2000)

draw_text(screen, "Press S to Fast-Forward", 60, 140,HEIGHT / 2)
pygame.display.update()
pygame.time.wait(2000)
intro()



class system(object):

    def __init__(self, x, y, HP, score):
        self.x = x
        self.y = y
        self.HP = HP
        self.score = score
        self.color = WHITE
        self.back = BLACK
        self.vel = 35
        self.width = 35
        self.life = 3
        self.highscore = 0
        self.money = 50
        self.cont = True
        self.wave = 0

    def shoot(self):
        pygame.time.wait(8)
        if len(bullets) < 1 and self.money > 0:
            self.money -= 1
            bullet = Bullet(self.x + 15, self.y + 20)
            all_sprites.add(bullet)
            bullets.add(bullet)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 20 and self.cont:
            self.x -= self.vel
            pygame.time.wait(1)

        if keys[pygame.K_RIGHT] and self.x < WIDTH - 55 and self.cont:
            self.x += self.vel
            pygame.time.wait(1)

        if keys[pygame.K_SPACE] and self.cont:
            self.shoot()
            pygame.time.wait(1)

        pygame.time.delay(20)
        if keys[pygame.K_p]:
            self.cont = not self.cont

        pygame.time.delay(10)
        if keys[pygame.K_r]:
            retry()



    def death(self, mobs, bullets, all_sprites):
        if self.HP <= 0:
            if self.score > self.highscore:
                self.highscore = self.score
            self.score = 0
            self.life -= 1
            mobs.empty()
            bullets.empty()
            all_sprites.empty()
            self.HP = 100
            self.wave = 0




class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 12))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -40
        self.hit = 0

    def update(self):
        if Player.cont:
            self.rect.y += self.speedy
            pygame.time.wait(1)
            if self.rect.bottom < 0:
                self.kill()

            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            for self.hit in hits:
                Player.score += 2
                Player.money += random.randrange(2, 3)

class Mobs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(25, 465)
        self.rect.y = random.randrange(0, 80, 40)
        self.direction = "R"
        self.vel = 12

    def update(self):

        if self.direction == "R" and Player.cont:
            self.rect.x += self.vel
            pygame.time.wait(1)

        if self.direction == "L" and Player.cont:
            self.rect.x -= self.vel
            pygame.time.wait(1)

        if self.rect.y > HEIGHT + 30 and Player.cont:
            Player.HP -= 10
            self.kill()

        if self.rect.x > WIDTH + 5 and Player.cont:
            self.rect.y += 55
            pygame.time.wait(1)
            self.direction = "L"

        if self.rect.x < -5 and Player.cont:
            self.rect.y += 55
            pygame.time.wait(1)
            self.direction = "R"


Player = system(WIDTH / 2, HEIGHT - 50, 100, 0)
pygame.time.wait(1)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()


run = True
while run and Player.life > 0:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    screen.fill(Player.back)
    Player.update(keys)
    Player.death(mobs, bullets, all_sprites)
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        Player.score += 2
        Player.money += random.randrange(2, 3)

    if len(mobs) == 0:
        Player.wave += 1
        for i in range(Player.wave * 5 + 10):
            m = Mobs()
            all_sprites.add(m)
            mobs.add(m)

    all_sprites.draw(screen)
    pygame.draw.rect(screen, Player.color, (Player.x, Player.y, Player.width, Player.width))
    draw_text(screen, "Score: "+str(Player.score), 18, WIDTH - 80, 10)
    draw_text(screen, "Hp: "+str(Player.HP), 18, 10, 10)
    draw_text(screen, "Lives Left: "+str(Player.life), 18, 200, 10)
    draw_text(screen, "Wave: " + str(Player.wave), 18, 460, 10)
    draw_text(screen,"High Score: "+str(Player.highscore), 18, WIDTH - 100, 40)
    draw_text(screen, "Money: " + str(Player.money), 18, 10, 40)

    if not Player.cont:
        screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(fps)


pygame.quit()
