#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # IR PARA CIMA É k_up
            self.rect.centery -= ENTITY_SPEED[self.name]  # QUANDO FOR PARA CIMA USAR VALOR NEGATIVO -=
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # IR PARA BAICO É K_DOWN
            self.rect.centery += ENTITY_SPEED[self.name]  # QUANDO FOR PARA BAIXO USAR VALOR POSITIVO +=
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # IR PARA ESQUERDA É K_LEFT
            self.rect.centerx -= ENTITY_SPEED[self.name]  # QUANDO FOR PARA ESQUERDA USAR VALOR NEGATIVO -=
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # IR PARA A DIREITA É K_RIGHT
            self.rect.centerx += ENTITY_SPEED[self.name]  # QUANDO FOR PARA DIREITA USAR VALOR POSITIVO +=

        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))