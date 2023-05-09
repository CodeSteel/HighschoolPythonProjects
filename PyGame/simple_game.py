import os, pygame

win = pygame.display.set_mode((650,500), 0, 32)
run = True

surface = pygame.display.get_surface()
ScrW = surface.get_width()
ScrH = surface.get_height()

class Rectangle:
    def __init__(self, x, y, w, h, r = 255, b = 0, g = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.b = b
        self.g = g

    def draw(self):
        self.rect = pygame.draw.rect(win, (self.r, self.b, self.g), (self.x, self.y, self.w, self.h))


player = Rectangle(0, 0, 5, 5)
speed = .2

def update():
    player.draw()
    pygame.display.update()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.blit()
        player.y -= speed

    if keys[pygame.K_s]:
        player.y += speed

    if keys[pygame.K_a]:
        player.x -= speed

    if keys[pygame.K_d]:
        player.x += speed

    if keys[pygame.K_SPACE]:
        win.fill((0,0,0))
        player.x = 0
        player.y = 0
        

while run:
    update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("First Game")

pygame.quit()