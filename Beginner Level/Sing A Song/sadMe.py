import time
import sys

def print_lyrics():
    lyrics = [
        "ভেবে দেখেছো কি",
        "তারা রাও যতো আলোকবর্ষ দূরে",
        "তারো দূরে",
        "তুমি আর আমি যাই ক্রমে সরে সরে",
        "ভেবে দেখেছো কি",
        "তারা রাও যতো আলোকবর্ষ দূরে",
        "তারো দূরে",
        "তুমি আর আমি যাই ক্রমে সরে সরে"
    ]
    
    
    delays = [1.2, 0.8, 0.6, 1.5, 1.2, 0.8, 0.6, 2.0]

    print("পৃথিবীটা নাকি \n")
    time.sleep(1.0)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
  
            time.sleep(0.10) 
        
        print() 
        
        if i < len(delays):
            time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()