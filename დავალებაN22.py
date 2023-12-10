import pygame
from pygame.locals import *
from random import randint, choice

enemy_number = int(input('Enter a number of enemies: '))

display_number = enemy_number

pygame.init()

size = width, height = 800, 600


back_image = pygame.image.load('back.jpg')
back_image = pygame.transform.scale(back_image, (width, height))
back_rect = back_image.get_rect()





screen = pygame.display.set_mode(size)
pygame.display.set_caption('Dragon')
clock = pygame.time.Clock()




class Player(pygame.sprite.Sprite):
    def __init__(self, image, size):
        super(Player, self).__init__()
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(image), (self.size, self.size))
        self.current_image = self.image
        self.rect = self.image.get_rect(center=(width/2, height/2))
        self.speed = randint(5, 10)

    def move(self, keys):
        if keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            self.current_image = pygame.transform.flip(self.image, False,False)
        if keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            self.current_image = pygame.transform.flip(self.image, True, False)
        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            self.current_image = pygame.transform.rotate(self.current_image, 0)
        if keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            self.current_image = pygame.transform.rotate(self.current_image, 0)
        # if keys[K_SPACE]:
        #     fire = Fire()
        #     fire.make_fire()
        #     fire.move()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def draw(self):
        screen.blit(self.current_image, self.rect)

    # def create_fire(self):
    #     fire = Fire()
    #     fire.make_fire()
    #     fire.move()




class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Enemy, self).__init__()
        self.size = randint(40, 90)
        self.image = pygame.transform.scale(pygame.image.load(image), (self.size, self.size))
        self.rect = self.image.get_rect(center=(randint(width+20, width+100), randint(0, height)))
        self.speed = randint(5, 10)
        self.is_alive = True

    def draw(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(-self.speed, 0)
        # if keys[K_DOWN]:
        #     self.rect.y += self.speed
        # if keys[K_UP]:
        #     self.rect.y -= self.speed
        # if keys[K_LEFT]:
        #     self.rect.x -= self.speed
        # if keys[K_RIGHT]:
        #     self.rect.move_ip(2*self.speed, 0)

    def update(self):
        self.draw()
        self.move()

class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super(Fire, self).__init__()
        self.fire_image = pygame.transform.scale(pygame.image.load('fireball.png'), (randint(30, 70), randint(30, 70)))
        self.rect = self.fire_image.get_rect(center=(player.rect.x, player.rect.y))
        self.active = Fire


    def make_fire(self):
        screen.blit(self.fire_image, self.rect)

    def move(self):
        self.rect.x += 30


player = Player('dragon.png', 100)


enemy_timer = USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1000)

enemies = pygame.sprite.Group()


fireballs = pygame.sprite.Group()

running = True
while running:

    keys = pygame.key.get_pressed()
    screen.blit(back_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                fire = Fire()
                fire.active = True
                fireballs.add(fire)
        elif event.type == enemy_timer:
            if len(enemies) < enemy_number:
                enemy_list = ['cthulhu.png', 'ghost.png', 'ufo.png', 'dragon_en.png']
                new_enemy = Enemy(choice(enemy_list))
                enemies.add(new_enemy)
            if display_number == 0:
                running = False

    player.draw()
    player.move(keys)

    for enemy in enemies:
        enemy.update()
        if pygame.Rect.colliderect(player.rect, enemy):
            running = False
        fire_collision = pygame.sprite.spritecollideany(enemy, fireballs)

        if enemy.rect.right < 0 or fire_collision:
            enemy.kill()
            display_number -= 1

    for fire in fireballs:
        if fire.active:
            fire.make_fire()
            fire.move()
        # if pygame.sprite.spritecollideany(fire, enemies):
        #     fire.kill()


    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f'Enemies:{display_number}', True, (23, 25, 26), (53, 64, 0))
    text_rect = text.get_rect()
    text_rect.center = (width / 2, height - 20)
    screen.blit(text, text_rect)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
