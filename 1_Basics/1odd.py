from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13]

right_this_minute = datetime.today().minute

for i in range(5):
    if right_this_minute in odds:
        print(i, " odd 1-13")
    else:
        print(i, " not odd 1-13")