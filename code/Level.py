#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import WIN_WIDTH


class Level:

    def __init__(self, window, name, game_mode, level_number=1, is_menu=False):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # modo de jogo
        self.is_menu = is_menu  # Flag para verificar se é o menu
        self.level_number = level_number # Número do nível
        self.entity_list: list[Entity] = []
        self.scroll_x = 0 # Variável para controlar o scroll horizontal

        # Carregar o fundo dependendo se é menu ou nível de jogo
        if self.is_menu:
            self.entity_list.extend(EntityFactory.get_entity('MenuBg')) # Carrega o fundo do menu
        else:
            if self.level_number == 1:
                self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
            elif self.level_number == 2:
                self.entity_list.extend(EntityFactory.get_entity('Level2Bg'))
            # Adicione mais níveis aqui se necessário

    def resize_background(self):
        # Obtém o tamanho da janela
        width, height = self.window.get_size()

        # Só redimensionar se não for o menu
        for entity in self.entity_list:
            # Obtém o tamanho original da superfície da entidade
            orig_width, orig_height = entity.surf.get_size()

            # Calcula o fator de escala para manter a proporção da imagem
            scale_factor = min(width / orig_width, height / orig_height)

            # Calcula o novo tamanho mantendo a proporção
            new_width = int(orig_width * scale_factor)
            new_height = int(orig_height * scale_factor)

            # Redimensiona a superfície da entidade mantendo a proporção
            entity.surf = pygame.transform.scale(entity.surf, (new_width, new_height))

            # Atualiza o retângulo da entidade
            entity.rect = entity.surf.get_rect()

            # Centraliza a entidade na janela (opcional, pode remover se usar scroll)
            entity.rect.center = (width // 2, height // 2)

    def run(self):
        # Redimensiona o fundo, se necessário
        self.resize_background()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Simulação de movimento do personagem (substitua pela lógica real)
            keys = pygame.key.get_pressed()
            player_speed = 1
            if not self.is_menu and self.entity_list:
                if keys[pygame.K_LEFT]:
                    self.scroll_x += player_speed
                if keys[pygame.K_RIGHT]:
                    self.scroll_x -= player_speed

            # Limpa a tela antes de desenhar os elementos
            self.window.fill((0, 0, 0))  # Preenche com preto ou outra cor

            if not self.is_menu and self.entity_list:
                for ent in self.entity_list:
                    # Move o background
                    ent.move(self.scroll_x)
                    # Desenha a entidade na janela
                    self.window.blit(source=ent.surf, dest=ent.rect)
            elif self.is_menu:
                for ent in self.entity_list:
                    # Desenha a entidade na janela
                    self.window.blit(source=ent.surf, dest=ent.rect)

            pygame.display.flip()  # Atualiza a tela

        pygame.quit() # Adicione esta linha para fechar o Pygame quando o loop terminar