Medical_cause = input("Are you have any medical cause say y or n = ").lower()
attendance = int(input("Enter your attendance : "))
if Medical_cause == 'y':
    print("You are allowed for exam")
else:
    if attendance >= 70:
        print("You are allowed for exam")
    else:
        print("Your are not allowed for exam")