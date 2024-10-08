withdrawal = float(input("Enter the amount you want to withdraw: "))

if withdrawal > 1000:
    print("Large transaction: Approval required.")
elif 500 <= withdrawal <= 1000:
    print("Transaction in review.")
else:
    if withdrawal < 10:
        pass
    else:
        print("Transaction approved.")