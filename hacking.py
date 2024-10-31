import time
import random

print(' Initiating mainframe hack...')

for i in range(1, 101, random.randint(5,30)):
    time.sleep(0.2)
    print(f'Hacking {i}% complete...')
    
time.sleep(1)
print(' Accessing classified files...')
time.sleep(1)

secrets = [' Pinaeapple does not belong on pizza.',
           ' Spies dont actually wear sunglasses indoors.',
           ' Blockbuster is making a comebackl.',
           ' Robots secretly want to be friends.',
           ' Aliens think Earth is a tourist trap.']

time.sleep(1)
print(' Files accessed! Secret revealed')
print(random.choice(secrets))