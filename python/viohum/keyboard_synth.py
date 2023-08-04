import pygame as pg
import numpy as np


def synth(frequency, duration=1, sampling_rate=44100):
    #frames = int(duration*sampling_rate)
    frames = int(duration*sampling_rate/2)
    arr = np.cos(2*np.pi*frequency*np.linspace(0,duration, frames))
    arr = arr + np.cos(4*np.pi*frequency*np.linspace(0,duration, frames))
    arr = arr - np.cos(6*np.pi*frequency*np.linspace(0,duration, frames))
    arr = arr/max(np.abs(arr)) # triangularish waves pt1
    print(len(arr))
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
        if(i==10):
            print (xstart)
            #pg.draw.rect(screen, BLUE, pg.Rect(xstart, 0 , xstart+int(XMAX/NUMNOTES), YMAX))
            #pg.draw.rect(screen, BLUE, pg.Rect(xstart, 0 , xstart+10,10))
            #pg.display.update()
            None

    return None

running = 1
pg.display.set_caption("PyViolin")
MIDDLEC = 130
XMAX = 1280
YMAX = 720
NUMNOTES = 80
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((XMAX, YMAX))
draw_lines(screen)


counter = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            counter += 1
            print ("Mouse click detected")
            [x,y] = pg.mouse.get_pos()
            key =  int((x*NUMNOTES)/XMAX)
            freq = MIDDLEC*(2**(key/12))
            #volume = 0.1+0.05*counter
            volume = 0.2 + 0.8*(y/YMAX)
            print ("--"*10)
            print ("counter = ", counter)
            print ("frequency = ", freq)
            print("volume = ",volume)
            print ("mouse position = ", pg.mouse.get_pos())
            print ("--"*10)
            sample = synth(freq)
            sample.set_volume(volume)
            sample.play()
            sample.fadeout(400)
            None
    pg.display.update()

pg.mixer.quit()
pg.quit()
