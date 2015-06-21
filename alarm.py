import pygame, sys
from pygame.locals import *
import threading


class IntrusionAlarm(object):
	"""dcstring for IntrusionAlarm"""
	# set up the colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

	def __init__(self):
		# super(IntrusionAlarm, self).__init__()
		# threading.Thread.__init__(self)
		pygame.init()
		pygame.mixer.init()

		# set up the window
		self.windowSurface = pygame.display.set_mode((500, 400), 0, 32)
		pygame.display.set_caption('Warning!!!')

		

		# set up fonts
		basicFont = pygame.font.SysFont(None, 48)

		# set up the text
		self.text = basicFont.render('Motion Detected. ALARM!!!', True, self.WHITE, self.RED)
		self.textRect = self.text.get_rect()
		self.textRect.centerx = self.windowSurface.get_rect().centerx
		self.textRect.centery = self.windowSurface.get_rect().centery

		# draw the white background onto the surface
		self.windowSurface.fill(self.RED)

		# setup alarm image
		self.robber = pygame.image.load("resources\intrusion.jpg").convert()
		self.robberrect = self.robber.get_rect()

		# set up alarm sound
		pygame.mixer.music.load("resources\siren.mp3")

	def run(self):
		# draw the text's background rectangle onto the surface
		pygame.draw.rect(self.windowSurface, self.RED, (self.textRect.left - 20, self.textRect.top - 20, self.textRect.width + 40, self.textRect.height + 40))

		# get a pixel array of the surface
		pixArray = pygame.PixelArray(self.windowSurface)
		pixArray[480][380] = self.BLACK
		del pixArray

		# draw the text onto the surface
		self.windowSurface.blit(self.robber, self.robberrect)
		self.windowSurface.blit(self.text, self.textRect)
		pygame.mixer.music.play(-1)

		# draw the window onto the screen
		pygame.display.update()

		# run the game loop
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            pygame.quit()
		            sys.exit()
				



if __name__ == '__main__':
	alarm = IntrusionAlarm()
	alarm.trigger()












		


# # set up pygam
# pygame.init()

# # set up audio
# pygame.mixer.init()

# # set up the window
# windowSurface = pygame.display.set_mode((500, 400), 0, 32)
# pygame.display.set_caption('Warning!!!')

# # set up the colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # set up fonts
# basicFont = pygame.font.SysFont(None, 48)

# # set up the text
# text = basicFont.render('Motion Detected. ALARM!!!', True, WHITE, RED)
# textRect = text.get_rect()
# textRect.centerx = windowSurface.get_rect().centerx
# textRect.centery = windowSurface.get_rect().centery

# # draw the white background onto the surface
# windowSurface.fill(RED)

# # setup alarm image
# robber = pygame.image.load("intrusion.jpg").convert()
# robberrect = robber.get_rect()

# # set up alarm sound
# pygame.mixer.music.load("siren.mp3")
# sound = pygame.mixer.Sound("alarm.mp3")

# # draw a green polygon onto the surface
# # pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# # draw some blue lines onto the surface
# # pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
# # pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
# # pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# # draw a blue circle onto the surface
# # pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# # draw a red ellipse onto the surface
# # pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# # draw the text's background rectangle onto the surface
# pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# # get a pixel array of the surface
# pixArray = pygame.PixelArray(windowSurface)
# pixArray[480][380] = BLACK
# del pixArray

# # draw the text onto the surface
# windowSurface.blit(robber, robberrect)
# windowSurface.blit(text, textRect)
# pygame.mixer.music.play(-1)

# # draw the window onto the screen
# pygame.display.update()

# # run the game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
