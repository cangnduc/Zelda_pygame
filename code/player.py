import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obticle_sprite):
        super().__init__(groups)
        self.image =pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.obticle_sprite = obticle_sprite
        self.hitbox = self.rect.inflate(0,-20)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # self.rect.x += self.direction.x * speed
        # self.collision("horizontal")
        # self.rect.y += self.direction.y * speed
        # self.collision("vertical")

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center
        #self.rect.center += self.direction * speed
    def collision(self,direction):
        if direction == "horizontal":
            for sprite in self.obticle_sprite:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.x >0: #moving rigt
                        self.hitbox.right = sprite.rect.left
                    if self.direction.x <0:
                        self.hitbox.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obticle_sprite:
                if sprite.rect.colliderect(self.hitbox):

                    if self.direction.y < 0:
                        self.hitbox.top = sprite.rect.bottom
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.rect.top
    def update(self):
        self.input()
        self.move(self.speed)