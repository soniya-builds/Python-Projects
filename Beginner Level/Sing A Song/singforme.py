import time
import sys
import pygame

def print_lyrics_with_audio():

    pygame.mixer.init()

    pygame.mixer.music.load("Pal Pal(KoshalWorld.Com).mp3") 
    pygame.mixer.music.play()

    lyrics = [
        "Mein ab kyun hosh may aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        
    ]
    
    for line in lyrics:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)
        print()
        time.sleep(1.5)