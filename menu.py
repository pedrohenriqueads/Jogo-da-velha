import pygame
import pygame_menu



pygame.init()
surface = pygame.display.set_mode((600, 600),0,32)

#Criando Menu
def set_difficulty(value, difficulty):
    
    pass

def start_the_game():
    
    pass

def set_options(value, options):

    pass

menu = pygame_menu.Menu('Bem vindo', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Jogo da Velha')
menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
menu.add.selector('Opitions :', [('Single Player', 1), ('Multi Player', 2)], onchange=set_options)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

#Executando o Menu
menu.mainloop(surface)