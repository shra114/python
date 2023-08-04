import pygame as pg
import numpy as np
import math
import matplotlib.pyplot as plt


def sine(t):
    volume = MASTER_VOLUME*2**(-t/HALF_LIFE)
    return volume * math.sin(t*math.tau*FREQUENCY)

def experiments():
    #piano sound
    #arr = -.25  * np.sin(3*np.pi*frequency*linspace_arry) + 0.25  * np.sin(  np.pi*frequency*linspace_arry)+ 0.866 * np.cos(  np.pi*frequency*linspace_arry)

    #arr = arr + 0.4*np.cos(4*np.pi*frequency*np.linspace(0,duration, frames))
    #arr = arr - 0.12*np.cos(6*np.pi*frequency*np.linspace(0,duration, frames))
    #arr = arr/max(np.abs(arr)) # triangularish waves pt1
    #plt.plot(arr[:300])
    #plt.show()
    #running = False
    None

def synth(frequency, duration=1, sampling_rate=44100):
    #frames = int(duration*sampling_rate)
    frames = int(duration*sampling_rate)
    linspace_arry  = np.linspace(0,duration, frames)
    w = 2*np.pi*frequency
    #arr  = np.cos(2*np.pi*frequency*np.linspace(0,duration, frames))
    #https://www.youtube.com/watch?v=ogFAHvYatWs&t=254s
    arr   = 0.6*np.sin(1*w*linspace_arry) * np.exp(-0.0015*w*linspace_arry)
    arr  += 0.4*np.sin(2*w*linspace_arry) * np.exp(-0.0015*w*linspace_arry)
    #plt.plot(arr[:300])
    #plt.show()

    sound = np.asarray([32767*arr,32767*arr]).T.astype(np.int16)
    sound = pg.sndarray.make_sound(sound.copy())

    return sound

def draw_lines(screen):
    WHITE=(255,255,255)
    BLUE=(0,0,255)
    for i in range(NUMNOTES):
        xstart = int(XMAX* (i/NUMNOTES))
        pg.draw.line(screen, WHITE, (xstart, 0), (xstart, YMAX))
        #Draw rectangle for the odd sections
        if(i%2):
            print (xstart)
            #The top-left vertex of the rectangle has coordinates (40, 80)
            #the width of the rectangle is 50 and the height is 30 pixels
            pg.draw.rect(screen, BLUE, pg.Rect(xstart, 0 , XMAX/NUMNOTES, YMAX))
            #pg.display.update()
    return None

pg.display.set_caption("PyViolin")
MIDDLEC = 265
XMAX = 1280
YMAX = 720
NUMNOTES = 18
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((XMAX, YMAX))
draw_lines(screen)
counter = 0
clock = pg.time.Clock()
SPS = 10 #samples per second

running = True
while running:
    clock.tick(SPS)
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            counter += 1
            print ("Mouse click detected")
            [x,y] = pg.mouse.get_pos()
            key =  int((x*NUMNOTES)/XMAX)
            freq = MIDDLEC*(2**(key/12))
            #volume = 0.1+0.05*counter
            volume = 0.2 + 0.4*(y/YMAX)
            print ("--"*10)
            print ("counter = ", counter)
            print ("frequency = ", freq)
            print("volume = ",volume)
            print ("mouse position = ", pg.mouse.get_pos())
            print ("--"*10)
            sample = synth(freq)
            sample.set_volume(volume)
            sample.play()
            break
    pg.display.update()

pg.mixer.quit()
pg.quit()
