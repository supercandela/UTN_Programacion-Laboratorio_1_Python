from Game import Game
from Home import Home
from MainMenu import MainMenu

from GamePlay import GamePlay
from HighScores import HighScores
from Settings import Settings  

game = Game('Tetris', 800, 800)
home = Home(game.screen)
main_menu = MainMenu(game.screen)
game_play = GamePlay(game.screen)
high_scores = HighScores(game.screen)
settings = Settings(game.screen)

#Le asigno a cada objeto las pantallas que necesito
#Game
game.settings = settings
#Home
home.main_menu = main_menu
#Main Menu
main_menu.home = home
main_menu.high_scores = high_scores
main_menu.settings = settings
main_menu.gameplay_scene = game_play
#GamePlay
game_play.main_menu = main_menu
game_play.settings = settings
game_play.high_scores = high_scores
#High Scores
high_scores.main_menu = main_menu
#Settings
settings.main_menu = main_menu

#Ejecuto el programa
game.run(home)