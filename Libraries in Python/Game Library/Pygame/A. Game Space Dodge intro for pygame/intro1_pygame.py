import pygame
import time
import random


pygame.init()

WIDTH, HEIGHT = 800, 600

# Window for our game
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 

# Window Title
pygame.display.set_caption("Space Dodge")

# Background image

BG = pygame.image.load("space_image.jpeg").convert()
# To resize background image according to window size
scaled_bg = pygame.transform.scale(BG, WIN.get_size()) 




PLAYER_WIDTH = 40
PLAYER_HEIGHT = 80
PLAYER_VELOCITY = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3


FONT = pygame.font.SysFont("comicsans", 30)






# To put image in the background and player
def draw(player, elapsed_time, stars):
    WIN.blit(scaled_bg, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10 ,10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update() # This will refresh the screen 




# Main Game logic
def main():
    run = True

    player = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0


    star_add_increment = 2000 # Here 2000 is in miliseconds
    star_count = 0

    stars = []
    hit = False



    while run:
        star_count += clock.tick(60) # This will make sure the while loop will run maximum 60 times a sec.
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 100)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed() # To get which keys are pressed by user
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and  player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + STAR_HEIGHT >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()



if __name__ == "__main__":
    main()

