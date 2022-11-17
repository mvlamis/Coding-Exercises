# display an image of a cat on the screen

import urllib.request
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Random Image")

url = "https://picsum.photos/640/480"
image = urllib.request.urlopen(url).read()

# create a file-like object from the image data
import io
imageFile = io.BytesIO(image)

# load the image
image = pygame.image.load(imageFile)

# display the image
screen.blit(image, (0, 0))

# wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # get a new image
                image = urllib.request.urlopen(url).read()
                imageFile = io.BytesIO(image)
                image = pygame.image.load(imageFile)
                screen.blit(image, (0, 0))
                
    pygame.display.flip()
                