import datetime
import sys
from utils import create_exesice

score = 0
timer = datetime.timedelta(seconds=55)
if timer > datetime.timedelta(seconds=59):
    sys.exit("timer < 60 s")
def quiz():
    global score
    global timer
    print("START")
    try:
        while timer >= datetime.timedelta(seconds=0):
            start = datetime.datetime.now().second
            print("timer", timer)
            ex, res = create_exesice()
            answer = int(input(f"Your score: {score} | {ex} = ? | Your answer: "))
            if answer == res:
                print("Corect!\n")
                score += 1
            else:
                print(f"Incorect, answer: {res}\n")
            end = datetime.datetime.now().second - start
            timer = datetime.timedelta(seconds=(timer.seconds - end))
            

    except ValueError:
        print("Need INT value")

quiz()
print("Your score:", score)
