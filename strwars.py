import pygame

class TextScroller(object):
    def __init__(self, lines, step, font, color, x = 0):
        self.step, self.font, self.color, self.x = step, font, color, x
        self.lines = [ (None, x) for x in lines]
        self.offset = 0
        self.running = True

    def get_img(self, idx):
        img, txt = self.lines[idx]
        if not img:
            # print("render", idx, txt)
            img = self.font.render(txt, True, self.color)
            self.lines[idx] = img, txt
        return img
    
    def render(self, screen):
        _, screen_y = screen.get_size()
        y = screen_y - self.offset
        for i in range(len(self.lines)):
            img = self.get_img(i)
            h = img.get_height()
            if y + h > 0:
                screen.blit(img, (0, y))
            y += h
            if y>screen_y:
                break
        self.offset += self.step
        self.running = y > 0
        return self.running


def get_scroller():
    lines = [
        "Þið kannizt við jólaköttinn", 
        "- sá köttur var griðarstór",
        "Fólk vissi'ekki hvaðan hann kom", 
        "eða hvert hann fór",
        "",
        "Hann glennti upp glyrnurnar sinar", 
        "glóandi báðar tvær",
        "Það var ekki heiglum hent", 
        "að horfa í þær",
        ]
    return TextScroller(lines, 1, pygame.font.Font(None,30), (255,255,0))

def get_screen(w,h):
    return pygame.display.set_mode((w,h), pygame.RESIZABLE)

def main():
    pygame.init()
    pygame.display.set_caption("scrolling message")
    SCROLL_EVENT = pygame.USEREVENT + 1
    scroller = get_scroller()
    pygame.time.set_timer(SCROLL_EVENT, 20)
    screen = get_screen(700,600)
    while screen:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            screen = None
        elif event.type == pygame.VIDEORESIZE:
            screen = get_screen(event.w, event.h)
        elif event.type == SCROLL_EVENT:
            screen.fill((0, 0, 0))
            screen = {True: screen, False: None}[scroller.render(screen)]
            pygame.display.flip()
    pygame.quit()

main()
