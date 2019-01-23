import cv2
import pygame
 

def runMovie():
	def play_videoFile(filePath,mirror=False):
		pygame.init()
		cap = cv2.VideoCapture(filePath)
		cv2.namedWindow('INTRO',cv2.WINDOW_AUTOSIZE)
		pygame.mixer.music.load("movies/song.wav")
		pygame.mixer.music.play()
		pygame.event.wait()
		while True:
			ret_val, frame = cap.read()

			if mirror:
				frame = cv2.flip(frame, 1)

			cv2.imshow('INTRO', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				pygame.mixer.music.stop()
				pygame.quit()
				break  # esc to quit

		cv2.destroyAllWindows()
	 
	def main():
	    play_videoFile('movies/intro.mpg',mirror=False)
	 
	if __name__ == '__main__':
	    main()	
	main()