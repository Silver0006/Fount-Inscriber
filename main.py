import keyboard, pystray, threading, random, msvcrt
from PIL import Image
from playsound import playsound

image = Image.open(r"D:\Python\Fount-Inscriber\icon.png")


def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()
        exit()


def sounds():
    while True:
        if keyboard.read_key() and not keyboard.is_pressed("space") and not keyboard.is_pressed("enter"):
            ranma = random.randint(1,3)
            playsound("D:\Python\Fount-Inscriber\Key " + str(ranma) + ".mp3", block=False)
        elif keyboard.is_pressed("enter"):
            playsound("D:\Python\Fount-Inscriber\enter.mp3", block=False)
        elif keyboard.is_pressed("space"):
            playsound("D:\Python\Fount-Inscriber\space.mp3", block=False)
        
            


        
sound_thread = threading.Thread(target=sounds, daemon = True)
sound_thread.start()
icon = pystray.Icon("FI", image, "Fount Inscriber", menu=pystray.Menu(pystray.MenuItem("Exit", after_click)))
icon.run()