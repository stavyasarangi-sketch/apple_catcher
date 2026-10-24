import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

img_still_orig = pygame.image.load('Images/still.png').convert() 
img_left_orig = pygame.image.load('Images/left_foot.png').convert()
img_right_orig = pygame.image.load('Images/right_foot.png').convert()
img_apple_orig = pygame.image.load('Images/apple.jpeg').convert()

img_still_orig.set_colorkey((255, 255, 255))
img_left_orig.set_colorkey((255, 255, 255))
img_right_orig.set_colorkey((255, 255, 255))
img_apple_orig.set_colorkey((255, 255, 255))

SPRITE_SIZE = (40, 40)
img_still = pygame.transform.scale(img_still_orig, SPRITE_SIZE)
img_left = pygame.transform.scale(img_left_orig, SPRITE_SIZE)
img_right = pygame.transform.scale(img_right_orig, SPRITE_SIZE)

APPLE_SIZE = (30, 30)
img_apple = pygame.transform.scale(img_apple_orig, APPLE_SIZE)

current_image = img_still
frame_number = 1
animation_timer = 0

x = 400
y = 300
facing_left = False

score = 0
apple_x = random.randint(0, 800 - 30)
apple_y = random.randint(0, 600 - 30)
apple_timer = 0
APPLE_LIFETIME = 180

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    is_moving = False

    if keys[pygame.K_LEFT]:
        x = x - 4
        facing_left = True
        is_moving = True
        
    if keys[pygame.K_RIGHT]:
        x = x + 4
        facing_left = False
        is_moving = True
        
    if keys[pygame.K_UP]:
        y = y - 4
        is_moving = True
        
    if keys[pygame.K_DOWN]:
        y = y + 4
        is_moving = True

    x = max(0, min(x, 800 - 40))
    y = max(0, min(y, 600 - 40))

    if is_moving == True:
        animation_timer = animation_timer + 1
        
        if animation_timer >= 10:
            animation_timer = 0
            if frame_number == 1:
                frame_number = 2
            else:
                frame_number = 1
                
        if frame_number == 1:
            current_image = img_left
        else:
            current_image = img_right
    else:
        animation_timer = 0
        current_image = img_still

    image_to_draw = current_image

    if facing_left == True:
        image_to_draw = pygame.transform.flip(image_to_draw, True, False)

    apple_timer += 1
    if apple_timer >= APPLE_LIFETIME:
        apple_x = random.randint(0, 800 - 30)
        apple_y = random.randint(0, 600 - 30)
        apple_timer = 0

    player_rect = pygame.Rect(x, y, 40, 40)
    apple_rect = pygame.Rect(apple_x, apple_y, 30, 30)

    if player_rect.colliderect(apple_rect):
        score += 1
        apple_x = random.randint(0, 800 - 30)
        apple_y = random.randint(0, 600 - 30)
        apple_timer = 0

    screen.fill((50, 50, 50))
    
    screen.blit(img_apple, (apple_x, apple_y))
    
    screen.blit(image_to_draw, (x, y))
    
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)
