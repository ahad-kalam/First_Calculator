a = []
sum = 0
i = 0

while(True):
    user_input = input("Enter your product price or press 'q' for quite : ")
    a.append(user_input)
    if (user_input != "q") :
        sum = sum + int(user_input)
        print(f"your total amount so far : {sum} .")
    else :
        while i < (len(a)-1):
            print(a[i])
            i += 1
        print(f"Your total bill amount is {sum}, Thanks for shopping with us..! ")
        break