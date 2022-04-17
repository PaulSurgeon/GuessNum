import random

r = random.randint(1, 100)

while True:
    Guessss = input("1至100當中，請猜一個數字:")
    Guessss = int(Guessss)
    if Guessss == r:
        print("恭喜你，猜對了。")
        break
    elif Guessss > r:
    	print("往小的數字猜。")
    elif Guessss < r:
    	print("往大的數字猜。")
