#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import pygame.image
import random
import math
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, C_CYAN


class Menu:
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.particles = []  # Lista de partículas para efeito de estrelas

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # Draw images (desenha as imagens)
            self.window.blit(source=self.surf, dest=self.rect)

            time_now = pygame.time.get_ticks()  # Tempo atual para efeito de onda

            # Aplica efeito de onda apenas no título
            self.menu_text_wave(50, "Galaxy Star", C_WHITE, ((WIN_WIDTH / 2), 100), time_now)

            # Desenha as opções do menu normalmente (sem efeito de onda)
            for i in range(len(MENU_OPTION)):
                y_offset = 200 + 20 * i
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_CYAN, ((WIN_WIDTH / 2), y_offset))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), y_offset))

            # Atualizar e desenhar partículas
            self.update_particles()

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text_wave(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, time_now: int):
        """ Desenha o título com efeito de onda e sombra """
        text_font: Font = pygame.font.SysFont(name="Galaxia", size=text_size)

        # Efeito de onda no eixo Y
        wave_offset = math.sin(time_now * 0.005) * 10
        text_y = text_center_pos[1] + wave_offset

        # Criando sombra preta para o título
        shadow_surf: Surface = text_font.render(text, True, (0, 128, 128)).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + 3, text_y + 3))
        self.window.blit(source=shadow_surf, dest=shadow_rect)

        # Título principal com efeito de onda
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=(text_center_pos[0], text_y))
        self.window.blit(source=text_surf, dest=text_rect)

        # Criar partículas saindo do título
        self.create_particles(text_rect)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """ Desenha o texto normal (sem efeito de onda) com sombra """
        text_font: Font = pygame.font.SysFont(name="Cardinal", size=text_size)

        # Criando sombra preta para o texto
        shadow_surf: Surface = text_font.render(text, True, (0, 0, 0)).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + 3, text_center_pos[1] + 3))
        self.window.blit(source=shadow_surf, dest=shadow_rect)

        # Texto principal
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def create_particles(self, text_rect):
        """ Cria partículas simulando estrelas saindo do texto """
        if random.random() < 0.2:  # Probabilidade de gerar partículas
            x = random.randint(text_rect.left, text_rect.right)
            y = text_rect.top
            self.particles.append(StarParticle(x, y))

    def update_particles(self):
        """ Atualiza e desenha partículas na tela """
        for particle in self.particles[:]:
            particle.update()
            particle.draw(self.window)
            if particle.lifetime <= 0:
                self.particles.remove(particle)


class StarParticle:
    """ Classe para criar partículas de estrelas saindo do título """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(-1, -2)
        self.size = random.randint(2, 4)
        self.lifetime = random.randint(30, 60)  # Tempo de vida da estrela

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.size)
