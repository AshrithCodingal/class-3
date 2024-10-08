import pygame
import random


pygame.init()

sprite_color_change_event =pygame.USEREVENT + 1
baground_color_change_even = pygame.USEREVENT + 2

blue=pygame.Color('blue')
lightblue=pygame.Color('lightblue')
darkblue=pygame.Color('darkblue')

yellow=pygame.Color('yellow')
marron=pygame.Color('red')
orange=pygame.Color('orange')
white=pygame.Color('white')



class Sprite(pygame.sprite.Sprite):
    
    def __init__(self,colour,width,height):


        super() .__init__() 
        self.image = pygame.Surface([width,height])
        self.image.fill (colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1]) ]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0] = - self.velocity[0]
            boundary_hit = True

        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1]= -self.velocity[1]
            boundary_hit = True


        if boundary_hit:

            pygame.event.post(pygame.event.Event (sprite_color_change_event))
            pygame.event.post(pygame.event.Event (baground_color_change_even))

    def change_colour(self):
        self.image.fill(random.choice([yellow,marron,orange,white]))
    


def change_baground_colour():
    global bg_colour
    bg_colour = random.choice([blue,lightblue,darkblue])







all_sprites_list = pygame.sprite.Group()



sp1 = Sprite(white,20,10)


sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)


all_sprites_list.add(sp1)



screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("COLOUR BOUNCE")
screen.fill(blue)



exit = False
clock = pygame.time.Clock()


while not exit:

    for event in pygame.event.get():
        if event.type ==pygame.quit:
            exit = True
        

        elif event.type ==sprite_color_change_event:
            sp1.change_colour()
        
        elif event.type == baground_color_change_even:
            change_baground_colour()

    all_sprites_list.update()


    screen.fill(blue)

    all_sprites_list.draw(screen)


    pygame.display.flip()



    clock.tick(240)


pygame.quit()
        

      

