#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Any

import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1536, 1024))  # Tela inicializada como self.screen
        pygame.display.set_caption("Arcane Duel")

    def run(self):
        menu = Menu(self.screen)  # Passando a tela para o Menu
        menu_return = menu.run()  # Guardando o retorno do menu


        if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
            level = Level(self.screen, 'Level1', menu_return)  # Usando self.screen
            level_return = level.run()
        elif menu_return == MENU_OPTION[4]:
            pygame.quit()
            quit()
        else:
            pass