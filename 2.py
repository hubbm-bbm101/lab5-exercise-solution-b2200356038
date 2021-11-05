valid=False
while valid == False:
    email=input("Enter your email.")
    if "@" in email:
        if "." in email:
            print("Your mail:", email)
            valid=True
        else:
            valid=False
    else:
        valid= False