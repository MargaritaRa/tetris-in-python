from lib.settings import *
from sys import exit
from lib.game import Game
from lib.score import Score

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    game_update = pygame.USEREVENT
    pygame.time.set_timer(game_update, update_start_speed)
    pygame.display.set_caption("Tetris")
    score = Score()

    class player_score:
        def __init__(self):
            self.score = 0
            self.level = 1
            self.lines = 0

    ps = player_score()
    
    def update_score(score, level, lines, speed):
        ps.score = score
        ps.level = level
        ps.lines = lines
        pygame.time.set_timer(game_update, int(speed))
    
    game = Game(update_score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == game_update and game.game_over == False:
                game.move_down()
            if game.game_over == True:
                game.game_over = False
                game.reset()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == True and game.game_over == False:
            game.move_left()
        elif key[pygame.K_RIGHT] == True and game.game_over == False:
            game.move_right()
        elif key[pygame.K_DOWN] == True and game.game_over == False:
            game.move_down()
        elif key[pygame.K_UP] == True and game.game_over == False:
            game.rotation()
                
        gradient_colors = [(255, 255, 255), (0,0,0)] 
        num_gradient_steps = window_width  # Number of steps in the gradient
        gradient_step = 1 / num_gradient_steps
            
        for i in range(num_gradient_steps):
                color = tuple(int(gradient_colors[0][c] * (1 - gradient_step * i) + gradient_colors[1][c] * gradient_step * i) for c in range(3))
                pygame.draw.rect(screen, color, (0, i, window_width, 1))
        game.run()
        score.run(ps.score, ps.level, ps.lines)
       
        pygame.display.update()
        clock.tick(12)
    
if __name__ == '__main__':
    main()
