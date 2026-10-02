n = int(input("Please enter the amount of rows you want:"))

for i in range(0 , n):

    for a in range(n - i):
        print("* " , end="")

    print()