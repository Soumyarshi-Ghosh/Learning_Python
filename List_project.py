cakes = ['Muffins', 'Rum Ball', 'Black Forest']
cakes.sort()
for cake in cakes:
    print(cake)
print()

while True:
    change = input(" (A)dd or (R)emove an item ")
    while True:
        if change == 'A' or change == 'a':
            Item = input(" What item would you like to add : ")
            cakes.append(Item)
            cakes.sort()
            break
        elif change == 'R' or change == 'r':
            Item2 = input(" What item would you like to remove : ")
            if Item2 in cakes:
                check_item = input(f"Are you sure you want to remove {Item2} (y/n)? ")
                if check_item == 'y' or check_item == 'Y':
                    cakes.remove(Item2)
                    print(Item2 + ' Has been removed from menu')
                    cakes.sort()
            else:
                print(" That item is not in the current menu ! ")
            break
        else:
            print("Please enter a valid option ")
    print("The current menu is : ")
    for cake in cakes:
        print(cake)
    print()
    exit_loop = input(" Type 'q' to quit or any key to continue ")
    if exit_loop == 'q':
        break

print(" Thank you for using the menu app ,  Have a great day !")