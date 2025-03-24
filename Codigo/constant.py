# cores
import pygame

COLOR_OY = (253, 116, 4)
COLOR_W = (255, 255, 255)
COLOR_Y = (254, 230, 12)

# Entity
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 4,
    'Level1Bg6': 6,
    'Player1': 4,
    'Player2': 4,
    'Enemy1': 3,
    'Enemy2': 2,
}
# Spawn_Enemy
SPAWN_TIME = 2000

# Menu
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# Player
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL}

# altura e largura
WIN_WIDTH = 576
WIN_HEIGHT = 324