import numpy as np
from skimage import transform as tf

#from moviepy.editor import *
#from moviepy.video.tools.drawing import color_gradient


# RESOLUTION

w = 720
h = w*9/16 # 16/9 screen
moviesize = w,h



# THE RAW TEXT
txt = "\n".join([
"A long time ago, in a faraway galaxy,",
"there lived a prince and a princess",
"who had never seen the stars, for they",
"lived deep underground.",
"",
"Many years before, the prince's",
"grandfather had ventured out to the",
"surface and had been burnt to ashes by",
"solar winds.",
"",
"One day, as the princess was coding",
"and the prince was shopping online, a",
"meteor landed just a few megameters",
"from the couple's flat."
])


# Add blanks
txt = 10*"\n" +txt + 10*"\n"


# CREATE THE TEXT IMAGE


clip_txt = TextClip(txt,color='white', align='West',fontsize=25,
                    font='Xolonium-Bold', method='label')