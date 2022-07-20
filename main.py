def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def print_with_indexes(l):
    for i in range (0, len(l)):
        output = " {:3} : {:10} : {:3}".format(i, l[i][0], l[i][1])
        print(output)

def print_customer_list_indexes(c):
    for i in range (0, len(c)):
        output = " {:3} : {:10} : {:3} : ${:3}".format(i, c[i][0], c[i][1], c[i][2])
        print(output)

def add_pasta(l, c):
    print_with_indexes(l)
    pasta_index = get_integer("Please enter the option number of pasta you want: ")
    pasta_quantity = get_integer("Please enter the quantity: ")
    customer_order = [l[pasta_index][0], pasta_quantity, l[pasta_index][1]]
    c.append(customer_order)
    print(c)
    return None

def review_order(c):
    print(c)
    print("")
    total = 0
    for x in c:
        print(x)
        sub_total = x[1]*x[2]
        print("The sub-total for this section is ${}".format(sub_total))
        total += sub_total
    print("----------------")
    print("The total price for your order is${}".format(total))
    print("")

#def subtract_pasta(c):
   # print(print_customer_list_indexes(c))
   # pasta_index = get_integer("Which pasta index would you like to subtract from: ->")
   # print(c[pasta_index][0], c[pasta_index][1])
   # print("You currently have ordered {} {} on the order".format(c[pasta_index][1], c[pasta_index][0])
    #print("How many {} would you like to remove from the customer order".format(c[pasta_index][0]))

def subtract_pasta(c):
    print_customer_list_indexes(c)
    my_index = get_integer("Choose index number to update the fruit quantity")
    print()
    old_amount = c[my_index][1]
    number = get_integer("Enter how many you would like to remove:")
    print()
    new_amount = old_amount - number
    print("{} - {} = {} left in the bowl".format(old_amount, number, new_amount))
    print()
    output_message = "The number of {} {} has been updated to {}.".format(old_amount, c[my_index][0], new_amount)
    print(output_message)

    #if pasta_index in c:
       # c.remove(pasta_index)
        #output = "{} has been removed from the customer order".format(pasta_index)
        #print(output)
    #else:
        #output = "{} can not be found, so it is not in the list".format(pasta_index)
        #print(output)

def edit_order(l):
    print_with_indexes(l)
    user_choice = get_integer("PLease enter the index number to update the name: ")
    #print(L[my_index])
    new_pasta = get_integer("Please enter the new quantity of fruit: ")
    old_pasta = l[user_choice][1]
    l[user_choice][1] = new_pasta
    #print(l [my_index][1])
    output_message = "{} many has now been changed to {}".format(old_pasta, new_pasta)
    print(output_message)

def main():
    #customer_order = []
    customer_order = [['Rigatoni alla Caponata', 2, 21],["Conchilglie alla Bolognese", 7, 22]]

    pasta_list = [
        ["Linguine Gamberi", 23],
        ["Fusilli Pesto", 19],
        ["Conchilglie alla Bolognese", 22],
        ["Rigatoni alla Caponata", 21],
        ["Fettuccine Carbonara", 20],
        ["Spaghetti Pomodoro", 16],
        ["Pappardelle Ricci D’Angello", 26],
        ["Raviolo di Salsiccia", 22],
        ["Ravioli di Ricotta", 20]
    ]

    option_list = [
        ["P", "Print the menu"],
        ["A", "Add pasta to order"],
        ["R", "Review customer order"],
        ["D", "Delete item from customer list"],
        ["E", "Edit order"],
        ["S", "Stop program"]
        ]


    run_program=True
    while run_program:
        for x in option_list:
            output = "{} -- {} ".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ->").upper()
        print(user_choice)
        if user_choice == "P":
            print(print_with_indexes(pasta_list))
        elif user_choice == "A":
            add_pasta(pasta_list, customer_order)
        elif user_choice == "R":
            review_order(customer_order)
        elif user_choice == "D":
            subtract_pasta(customer_order)
        elif user_choice == "E":
            edit_order(customer_order)
        elif user_choice == "S":
            exit(0)
    print("Thank you, the program has ended")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()