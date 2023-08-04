def validate():
    while True:
        valid = input("Please enter y or n to validate of unvalidate (y/n)? ")
        if valid == "y" or valid == "Y":
            print(" Lets proceed... ")
            return valid
        elif valid == "n" or valid == "N":
            print(" Bye ! ")
            return valid
        else:
            print("Invalid input please Try again")


print('Thanks for using our app')
choice = validate()
print(f" you chose {choice} !")

