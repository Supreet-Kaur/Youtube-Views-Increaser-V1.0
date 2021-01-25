import webbrowser
import os
import time



url =  input("https://www.youtube.com/watch?v=olquo9bHEDE&feature=youtu.be&ab_channel=AshishThind")

refreshrate = input("120")

browserr = input("Google chrome")


def letsdoit():
    os.system("TASKKILL /F /IM "+browserr+".exe")
    webbrowser.open(url)
    time.sleep(int(refreshrate))

views = input("10")
for i in range(int(views)+1):
    letsdoit()
