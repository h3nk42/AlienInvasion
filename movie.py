import cv2
import numpy as np
import pygame
pygame.init()

def runMovie():
	cap = cv2.VideoCapture('movies/intro.mpg')
	'''
	Make sure your_video is in the same dir, else mention the full path.
	
	'''
	pygame.mixer.music.load("movies/song.wav")
	pygame.mixer.music.play()
	pygame.event.wait()
	while True:
		
		ret, frame = cap.read()
		#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',frame)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
		     break
	 
	cap.release()
	pygame.mixer.music.stop()
	pygame.quit()
