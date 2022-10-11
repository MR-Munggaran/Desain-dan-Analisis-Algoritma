#first two terms
nterms = int(input("How Many terms  : "))
n1, n2 = 0,1
count = 0

# check if the number of terms is valid
if nterms<=0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms," :")
else:
    print("Fibonacci sequence   : ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
            #update nilai
        n1 = n2
        n2 = nth
        count += 1
