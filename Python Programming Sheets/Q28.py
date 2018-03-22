import winsound
import time

def play(frequency, duration):
    winsound.Beep(frequency,duration)

play(293,200)
play(293,200)
play(293,200)
play(293,600)
play(246,600)

time.sleep(0.1)