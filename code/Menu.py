import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, WIN_HEIGHT, COLOR_GOLD

class Menu:
    def __init__(self, screen):
        self.screen = screen  # Inicializa a tela passada como parâmetro
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Carrega a imagem de fundo
        self.rect = self.surf.get_rect(left=0, top=0)  # Define a posição da imagem

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        title_font_size = 120  # Tamanho da fonte para o título
        option_font_size = 50  # Tamanho da fonte para as opções do menu

        # Ajusta o espaçamento entre o título e as opções
        title_y_position = WIN_HEIGHT // 2 - 100  # Coloca o título mais alto na tela
        option_y_position = title_y_position + title_font_size + 50  # Ajusta as opções mais abaixo

        while True:
            # Desenha a imagem de fundo
            self.screen.blit(self.surf, self.rect)

            # Usa a fonte personalizada para o título "Arcane Duel" com cor dourada
            self.menu_text(title_font_size, "Arcane", COLOR_GOLD, WIN_WIDTH / 2 - 150, title_y_position, custom_font=True)
            self.menu_text(title_font_size, "Duel", COLOR_GOLD, WIN_WIDTH / 2 + 150, title_y_position, custom_font=True)

            # Desenha as opções do menu com a fonte padrão e aplica a cor de destaque
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    # Destaca a opção selecionada com cor dourada
                    self.menu_text(option_font_size, MENU_OPTION[i], COLOR_GOLD, WIN_WIDTH / 2, option_y_position + 60 * i)
                else:
                    # Mantém a cor normal para as opções não selecionadas
                    self.menu_text(option_font_size, MENU_OPTION[i], COLOR_WHITE, WIN_WIDTH / 2, option_y_position + 60 * i)

            pygame.display.flip()

            # Verifica os eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # tecla para baixo DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # tecla para cima UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # tecla ENTER
                        return MENU_OPTION[menu_option]  # Retorna a opção selecionada

    def menu_text(self, font_size, text, color, x_position, y_position, custom_font=False):
        if custom_font:
            # Usando a fonte personalizada para o título "Arcane Duel"
            font_path = "./asset/Cardinal.ttf"  # Caminho para a fonte personalizada
            text_font = pygame.font.Font(font_path, font_size)
        else:
            # Usando a fonte padrão do Pygame para as opções do menu
            text_font = pygame.font.SysFont("Consolas", font_size)

        text_surface = text_font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x_position, y_position))
        self.screen.blit(text_surface, text_rect)
