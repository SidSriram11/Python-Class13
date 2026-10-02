n = int(input("Please enter the amount of rows you need : "))
no = 0

for i in range(0,n):

    for a in range(n - i):
        no = no + 1
        print(no , end=" ")

    print()

