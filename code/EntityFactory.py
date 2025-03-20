from code.Background import Background
from code.Const import WIN_WIDTH

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        if entity_name == 'Level1Bg':
            list_bg = []
            bg_width = 0
            # Aumente significativamente o número de repetições
            for i in range(3):
                bg = Background(f'Level1Bg{i}', (bg_width, 0))
                list_bg.append(bg)
                bg_width += bg.rect.width
            return list_bg
        elif entity_name == 'Level2Bg':
            list_bg = []
            bg_width = 0
            # Aumente significativamente o número de repetições
            for i in range(3):
                bg = Background(f'Level2Bg{i}', (bg_width, 0))
                list_bg.append(bg)
                bg_width += bg.rect.width
            return list_bg
        elif entity_name == 'MenuBg':
            return [Background('MenuBg', (0, 0))]
        else:
            return []