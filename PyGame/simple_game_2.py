import os, pygame

class Display():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700,500))
        pygame.display.set_caption("Better Game")
        self.player = drawRectangle(0, 0, 100, 100, 255, 0, 0, self.window)
        self.surface = pygame.display.get_surface()
        self.ScrW = self.surface.get_width()
        self.ScrH = self.surface.get_height()

    def update(self):
        pygame.display.update()
        speed = 9

        self.window.fill((0,0,0))
        self.player.draw()

        keys = pygame.key.get_pressed()
        
        if self.player.x <= 0:
            if keys[pygame.K_w]:
                self.player.y -= speed

            if keys[pygame.K_s]:
                self.player.y += speed

            if keys[pygame.K_d]:
                self.player.x += speed
        elif self.player.x >= self.ScrW - 100:
            if keys[pygame.K_a]:
                self.player.x -= speed

            if keys[pygame.K_w]:
                self.player.y -= speed

            if keys[pygame.K_s]:
                self.player.y += speed
        elif self.player.y <= 0:
            if keys[pygame.K_a]:
                self.player.x -= speed

            if keys[pygame.K_s]:
                self.player.y += speed

            if keys[pygame.K_d]:
                self.player.x += speed
        elif self.player.y >= self.ScrH - 100:
            if keys[pygame.K_a]:
                self.player.x -= speed

            if keys[pygame.K_w]:
                self.player.y -= speed

            if keys[pygame.K_d]:
                self.player.x += speed
        else:
            if keys[pygame.K_a]:
                self.player.x -= speed

            if keys[pygame.K_w]:
                self.player.y -= speed

            if keys[pygame.K_s]:
                self.player.y += speed

            if keys[pygame.K_d]:
                self.player.x += speed




                

class drawRectangle():
    def __init__(self, x, y, w, h, r, b, g, display):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.b = b
        self.g = g
        self.display = display
    
    def draw(self):
        pygame.draw.rect(self.display, (self.r, self.b, self.g), (self.x, self.y, self.w, self.h))


if __name__ == "__main__":
    display = Display()
    run = True

    while run:
        display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False