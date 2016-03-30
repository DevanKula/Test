in_file = open("items.csv", "r")
items_list =[]
choice = input(">>>").upper()
while choice != 'Q':
    for line in in_file:
        counter = 0
        DOLLAR_EQUALS_SIGN = "= $"
        counter += 1
        items_list = line.split(',')
        items_list.append(items_list[-1])
        items_list.append(counter)
        car_tuple = (items_list[5],items_list[0], items_list[1], float(items_list[2]),items_list[3])
        items_list.append(car_tuple)
        if choice == "L":
            print("{} - {:12} ({:25}".format(car_tuple[0], car_tuple[1],car_tuple[2]),'){:>40}{:,.2f}{}'.format(DOLLAR_EQUALS_SIGN,car_tuple[3], car_tuple[4].strip().replace('out','*').replace('in',' ')))

        elif choice == 'H':
            if car_tuple[4] == 'in\n':
                print("{} - {:12} ({:25}".format(car_tuple[0], car_tuple[1],car_tuple[2]),'){:>40}{:,.2f}{}'.format(DOLLAR_EQUALS_SIGN,car_tuple[3], car_tuple[4].strip().replace('out','*').replace('in',' ')))
        #print("Enter the number of an item to hire")
        #hire_choice = input()
    choice = input(">>>").upper()
