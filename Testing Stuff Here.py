import time

seconds = 1
minutes = 1
hours = 1

while True:
    time.sleep(0.1)
    seconds += 1
    print(seconds)
    if seconds % 60 is 0:
        minutes += 1
        print('SECONDS IF')
    if minutes % 360 is 0:
        print('Minute IF')