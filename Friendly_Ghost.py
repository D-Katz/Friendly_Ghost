#David Katz
#101157096

#imports the pygame library
import pygame

#initializes the display module of pygame
pygame.display.init()

#Asks user if they need isntructions and capitalizes it so that it's easier to detect a yes/no answer
answer=input("Do you need instructions?\n").upper()

#Gives instructions if the user requested them
if(answer=="YES"):
	print("Please input the file names of the background image and then the ghost image, afterwards either input in the terminal or click with your mouse the (x,y) location of where you want the ghost. Thanks!\n")

#Gets the background image name from the user, sets it to a variable, and gets its dimensions
background_image= input("Please enter the name of the background image\n")
background=pygame.image.load(background_image)
(background_width, background_height) = background.get_rect().size

#Gets the ghost image name from the user, sets it to a variable, and gets its dimensions
ghost_image= input("Please enter the name of the ghost image\n")
ghost=pygame.image.load(ghost_image)
(ghost_width, ghost_height) = ghost.get_rect().size

#sets a tuple called screen with dimensions of the background
screen=(background_width,background_height)

#Sets the window dimenstions to that of the background image
window = pygame.display.set_mode(screen)

#copies the background image onto the window
window.blit(background,(0,0))
#updates the display to show the background image
pygame.display.update()

#loop to check that the user has inputed valid numbers fo the (x,y) coordinates
coordinates=False
while(coordinates!=True):
	ghostx=int(input("Please enter the X coordinate of where you want the ghost to be centred\n"))
	ghosty=int(input("Please enter the Y coordinate of where you want the ghost to be centred\n"))
	if((ghostx < 0 or ghostx > background_width)and(ghosty < 0 and ghosty > background_height)):
		print("Both coordinates are incorrect. Please enter valid coordinates for X and Y (HINT: Both have to be greater or equal to 0 and smaller than the size of the background image)")
	elif((ghostx < 0 or ghostx > background_width)and(ghosty > 0 and ghosty < background_height)):
		print("X coordinate is incorrect. Please enter a valid coordinates for X (HINT: Has to be greater or equal to 0 and smaller than the size of the background image)")
	elif((ghostx > 0 or ghostx < background_width)and(ghosty < 0 and ghosty > background_height)):
		print("Y coordinate is incorrect. Please enter a valid coordinates for Y (HINT: Has to be greater or equal to 0 and smaller than the size of the background image)")
	else:
		print("Your coordinates are a-ok.")
		

#Runs the loop to check through the pixels on by one starting on the first coordinate of the ghost image and then going to the next and blending in the image if the pixels aren't green
for x in range (ghost_width):
	for y in range (ghost_height):
		(r,g,b,_)=ghost.get_at((x,y))
		if (r,g,b) != (0,255,0) :
			x_coordinate= ghostx - int(ghost_width/2) + x
			y_coordinate= ghosty - int(ghost_height/2) + y
			if not(x_coordinate<=0 or y_coordinate<=0):
				if not(x_coordinate >= background_width or y_coordinate >= background_height):
					(rb, gb, bb,_)=background.get_at((x_coordinate,y_coordinate))
					RGB_Average=(((r+rb)/2),((g+gb)/2),((b+bb)/2))
					background.set_at([x_coordinate,y_coordinate],RGB_Average)

#sets the new image of the ghost
window=pygame.display.set_mode([background_width,background_height])
window.blit(background,(0,0))
pygame.display.update()

#Keeps the image on the screen until the user clicks the [X] to close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()