def get_integer(m, min_length, max_length):
    my_integer = 0
    while True:
        my_integer_question = input(m)
        try:
            my_integer = int(my_integer_question)
            # add in validation for mininum and maximum integer length
            if len(my_integer_question) < min_length or len(my_integer_question) > max_length:
                # print error message saying they have too long or too short in length
                print(f'The number is less than {min_length} or longer than {max_length}')
            else:
                break
        except Exception as error:
            # print error message for entering a character instead of an integer
            print('You entered in an invalid character/s')

    return my_integer

#
def get_string(m, *length):
    my_string = ""
    #
    while True:
        my_string = input(m)
        if len(length) == 0:
            break
        # put in minimum and maximum length
        if len(length) > 0 and len(my_string) >= length[0]:
            if len(length) > 1 and length[1]:
                if my_string.upper() in length[1]:
                    # If they have
                    break
                else:
                    # error message
                    print('Wrong Value')
            else:
                break
    return my_string

def integer_in_array(c, question, min_length, max_length):
    while True:
        my_index = get_integer(question, min_length, max_length)
        # check if index is less than index in the list
        if len(c) < my_index:
            # print error message
            print("You entered an integer out of range, please enter a new integer")
        else:
            # if integer in the list then carry on
            return my_index

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
    pasta_index = integer_in_array(c, "Please enter the option number of pasta you want: ", 1, 1)
    pasta_quantity = integer_in_array(c, "Please enter the quantity: ", 1, 5)
    customer_order = [l[pasta_index][0], pasta_quantity, l[pasta_index][1]]
    c.append(customer_order)
    print_customer_list_indexes(c)
    return None

def review_order(c):
    #print(c)
    print("")
    total = 0
    print("Name                           | Quantity | Unit price | Subtotal ")
    for x in c:
        sub_total = x[1]*x[2]
        print("{} | {} | {} | {} ".format(x[0].rjust(30), str(x[1]).rjust(8), str(x[2]).rjust(10), str(sub_total).rjust(8)))
        # print("The sub-total for this section is ${}".format(sub_total))
        total += sub_total
    print("----------------")
    print("The total price for your order is${}".format(total))
    print("")


def subtract_pasta(c):
    print_customer_list_indexes(c)
    my_index = integer_in_array(c, "Choose index number to update the pasta quantity", 1, 1)
    print()
    old_amount = c[my_index][1]
    while True:
        number = get_integer("Enter how many you would like to remove:", 1, old_amount)
        if number > old_amount:
            print("Invalid number, you are unable to get rid of more pastas than you have ordered")
        else:
            break
    print()
    new_amount = old_amount - number
    print("{} - {} = {}, there are {} left in the order".format(old_amount, number, new_amount, new_amount))
    print()
    output_message = "The number of {} {} has been updated to {}.".format(old_amount, c[my_index][0], new_amount)
    print(output_message)

# edit the order function
def edit_order(l):
    print_with_indexes(l)
    user_choice = get_integer("Please enter the index number to update the name: ", 1, 1)
    #print(L[my_index])
    new_pasta = get_integer("Please enter the new quantity of pasta(max of 5): ", 1, 5)
    old_pasta = l[user_choice][1]
    l[user_choice][1] = new_pasta
    #print(l [my_index][1])
    output_message = "{} many has now been changed to {}".format(old_pasta, new_pasta)
    print(output_message)

def pickup_or_delivery(p, c):
    p_d = get_string("Would you like pick up or delivery? (P/D): ", 1, ['P', 'D']).upper()
    if p_d == "P":
        name = get_string("What is your full name? ", 3)
        phone_number = get_integer("What if your phone number? ", 9, 12)
        p.append(['pickup', name, phone_number])
    elif p_d == "D":
        name = get_string("What is your full name? ", 3)
        phone_number = get_integer("What if your phone number? ", 9, 12)
        address = get_string("What is your address? ", 6)
        p.append(['delivery',name,phone_number, address])
        c.append(['delivery', 1, 3])

def main():
    #customer_order = []
    customer_order = [['Rigatoni alla Caponata', 2, 21],["Conchilglie alla Bolognese", 7, 22]]

    pickup_delivery = []

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
        ["V", "View the menu"],
        ["A", "Add pasta to order"],
        ["R", "Review customer order"],
        ["D", "Delete item from customer list"],
        ["E", "Edit order"],
        ["O", "Option for pick up or delivery"],
        ["S", "Stop program"]
        ]


    run_program=True
    while run_program:
        for x in option_list:
            output = "{} -- {} ".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ->").upper()
        # print(user_choice)
        if user_choice == "V":
            print(print_with_indexes(pasta_list))
        elif user_choice == "A":
            add_pasta(pasta_list, customer_order)
        elif user_choice == "R":
            review_order(customer_order)
        elif user_choice == "D":
            subtract_pasta(customer_order)
        elif user_choice == "E":
            edit_order(customer_order)
        elif user_choice == "O":
            pickup_or_delivery(pickup_delivery, customer_order)
        elif user_choice == "S":
            exit(0)
    print("Thank you, the program has ended")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()