n = int(input("Please enter how many rows you want : "))
no = 0

for i in range(1 , n+1):
    
    for a in range(i):
        no = no + 1
        if no == 10:
            no = 1

        print(no , end=" ")


    print()
        

