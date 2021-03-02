from pygame import mixer, event
from time import sleep
print('{1} {0} {1}'.format('DESAFIO #021', '=' * 5))

mixer.init()
mixer.music.load('./assets/MyWar.wav')
mixer.music.play()
sleep(111)
mixer.quit()
