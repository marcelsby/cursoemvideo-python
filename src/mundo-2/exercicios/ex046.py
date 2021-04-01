from time import sleep
from emoji import emojize

print('{1} {0} {1}'.format('DESAFIO #046', '=' * 5))

for seg in range(10, 0, -1):
    sleep(1)
    print(seg)

    if seg == 1:
        sleep(1)
        print(emojize(':party_popper: Feliz ano novo :party_popper:'))
