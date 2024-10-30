import pygame
pygame.init()
Screen_Height , Screen_width=500,500

display_surface=pygame.display.set_mode((Screen_Height , Screen_width))
pygame.display.set_caption("Adding image and background")

bg_image=pygame.transform.scale(
    pygame.image.load("bg.png").convert(),
    (Screen_Height , Screen_width))

image=pygame.transform.scale(
    pygame.image.load("car.jpeg").convert_alpha(),(200,200))

image_rect=image.get_rect(center=(Screen_Height//2,Screen_width//2-30))

text=pygame.font.Font(None,36).render("Hello World",True,pygame.Color('black'))
text_rect=text.get_rect(center=(Screen_Height//2,Screen_width//2+100))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        display_surface.blit(bg_image,(0,0))
        display_surface.blit(image,image_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=='__main__':
 game_loop()
