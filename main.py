# import regex library
import re


def get_integer(m, min_number, max_number):
    """
    Ask user to enter number
    Check minimum and maximum number
    return error if outside of range
    repeat question if answer was outside of range
    return answer if correct
    """
    # my_integer = 0
    while True:
        my_integer_question = input(m)
        try:
            my_integer = int(my_integer_question)
            # add in validation for minimum and maximum integer length
            if my_integer < min_number or my_integer > max_number:
                # print error message saying they have too long or too short
                print('The integer you have entered is out of range')
            else:
                break
        except Exception as error:
            # print error message for entering a character instead of an integer
            print('You entered in an invalid character/s')

    return my_integer


def get_integer_length(m, min_length, max_length):
    """
    Ask user to enter number
    Check minimum and maximum length
    return error if outside of range
    repeat question if answer was outside of range
    return answer if correct
    """
    # my_integer = 0
    while True:
        my_integer_question = input(m)
        try:
            my_integer = int(my_integer_question)
            # add in validation for mininum and maximum integer length
            if len(my_integer_question) < min_length or len(my_integer_question) > max_length:
                # print error message saying they have too long or too short in length
                print(f'The integer you have entered is out of range {my_integer} min({min_length}) max({max_length})')
            else:
                break
        except Exception as error:
            # print error message for entering a character instead of an integer
            print('You entered in an invalid character/s')

    return my_integer


def get_string(m, *length):
    """
    Ask user to enter character
    Check minimum and maximum length
    return error if outside of range
    repeat question if answer was outside of range
    return answer if correct
    """
    # my_string = ""

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
                    print('Wrong Value entered')
            else:
                break
    return my_string

# def integer_in_array(c, question, min_length, max_length):
#     while True:
#         my_index = get_integer(question, min_length, max_length)
#         # check if index is less than index in the list
#         if len(c) < my_index:
#             # print error message
#             print("You entered an integer out of range, please enter a new integer")
#         else:
#             # if integer in the list then carry on
#             return my_index


def get_name():
    """
    Ask for users name
    reject if not a-z or space
    return answer if correct
    """
    while True:
        answer = input("What is your name? ")
        if len(answer) < 1:
            print("Name needs two or more characters")
        elif re.match(r"^[A-Z ]+$", answer.upper()):
            return answer
        else:
            print("Please only enter in letters")


def print_with_indexes(list_array):
    """
    print the menu list with indexes and indented correctly
    """
    for i in range(0, len(list_array)):
        output = " {:3} : {:10} : {:3}".format(i, list_array[i][0], list_array[i][1])
        print(output)


def print_customer_list_indexes(customer):
    """
    print the customer list with indexes and indented correctly
    """
    for i in range(0, len(customer)):
        output = " {:3} : {:10} : {:3} : ${:3}".format(i, customer[i][0], customer[i][1], customer[i][2])
        print(output)


def print_p_d_list_indexes(p_d):
    """
    print the pickup or delivery list with indexes and indented correctly
    """
    for i in range(0, len(p_d)):
        # output = " {:3} : {:10} : {:3} : ${:3}".format(i, p[i][0], p[i][1], p[i][2])
        print(f"{p_d[i][0]} :       {p_d[i][1]} : {p_d[i][2]} : {p_d[i][3]}")


def add_pasta(l_t, c_l):
    """
    function for add pasta

    Ask user to enter in the option number they want
    Ask quantity of pastas they want
    add their pasta to the order
    """
    print_with_indexes(l_t)
    pasta_index = get_integer("Please enter the option number of pasta you want: ", 0, len(l_t)-1)
    pasta_quantity = get_integer("Please enter the quantity(max of five pastas): ", 1, 5)
    customer_order = [l_t[pasta_index][0], pasta_quantity, l_t[pasta_index][1]]
    c_l.append(customer_order)
    print_customer_list_indexes(c_l)


def review_order(c_l):
    """
    print out the customer order
    """
    # print(c)
    print("")
    total = 0
    print("Name                           | Quantity | Unit price | Subtotal ")
    # loop through order and print each item
    for x in c_l:
        sub_total = x[1]*x[2]
        print("{} | {} | {} | {} ".format(x[0].rjust(30), str(x[1]).rjust(8), str(x[2]).rjust(10),
                                          str(sub_total).rjust(8)))
        # print("The sub-total for this section is ${}".format(sub_total))
        total += sub_total
    print("------------------------------------------")
    print(f"The total price for your order is ${total}\n")
    # print("")


def subtract_pasta(c):
    """
    function for subtract pasta

    Check if there are any items in order
    If no items return to main page
    If there are items ask which one to remove
    ask how many they want to remove
    check if they have ordered that many pastas
    remove correct amount from order and get rid of item if necessary
    """
    # check if there are items in the order if not return to main menu
    if len(c) == 0:
        print("There are no items in the order")
        print("returning to main menu")
        return None
    print_customer_list_indexes(c)
    my_index = get_integer("Choose index number to update the pasta quantity: ", 0, len(c)-1)
    print()
    old_amount = c[my_index][1]
    # check if there enough pastas in the order to remove, error message if not
    while True:
        number = get_integer("Enter how many you would like to remove: ", 1, old_amount)
        if number > old_amount:
            print("Invalid number, you are unable to get rid of more pastas than you have ordered")
        else:
            break
    print()
    # remove items from order
    if (old_amount - number) == 0:
        print(f"Removing {c[my_index][0]} from the order")
        del c[my_index]
    # remove pasta from order
    else:
        c[my_index][1] = old_amount - number
        print(f"Item {c[my_index][0]} has {c[my_index][1]} left in the order")
    print()


def edit_order(c):
    """
    edit the order function

    check to see if there are items in order, send back to main page if not
    ask which pasta they want to change
    ask them to enter the new quantity of pasta
    change quantity in customer list
    """
    # check to see if there are items in order, return to main menu if not
    if len(c) == 0:
        print("There are no items in the order")
        print("returning to main menu")
        return None
    # call function for edit order
    print_customer_list_indexes(c)
    user_choice = get_integer("Please enter the index number to update the pastas in your order: ", 0, len(c)-1)
    new_pasta = get_integer("Please enter the new quantity of pasta(max of 5): ", 0, 5)
    old_pasta = c[user_choice][1]
    c[user_choice][1] = new_pasta
    output_message = "{} many pastas has now been changed to {}".format(old_pasta, new_pasta)
    print(output_message)


def pickup_or_delivery(p, c):
    """
    pick up or delivery function

    Ask if they want pickup or delivery
    if pickup then ask for name and phone number
    add to pickup or delivery order
    if pickup
    """
    p_d = get_string("Would you like pick up or delivery? (P/D): ", 1, ['P', 'D']).upper()
    p.clear()
    name = get_name()
    phone_number = get_integer_length("What if your phone number? ", 9, 12)
    if p_d == "P":
        p.append(['pickup', name, phone_number, ''])
        # Check if order has a delivery and remove it as it's a pickup
        for item in c:
            if item[0] == 'delivery':
                c.remove(item)
    elif p_d == "D":
        address = get_string("What is your address? ", 6)
        p.append(['delivery', name, phone_number, address])
        # Check if order does not have a delivery
        has_delivery = False
        for item in c:
            if item[0] == 'delivery':
                has_delivery = True
        # Add delivery if it does not have delivery in order
        if not has_delivery:
            c.append(['delivery', 1, 3])


def confirm_order(c, p):
    """
    print out customer order and pickup or delivery information
    ask if they are the right details
    and then if yes say thank you for order and ask if they want to order again
    if no then return to main page
    if they want to order again then clear customer and pickup/delivery
    if they don't want to order again stop program
    """
    print_customer_list_indexes(c)
    print_p_d_list_indexes(p)
    order_complete = get_string("Are these the right order and details? (Y/N): ", 1, ['Y', 'N']).upper()
    # Check if answer is order complete
    if order_complete == "Y":
        new_order = get_string("Thank you for ordering would you like to order again? (Y/N): ", 1, ['Y', 'N']).upper()
        # Answer is yes to do a new order and then clear order
        if new_order == "Y":
            c.clear()
            p.clear()
        # Answer is no to exit program
        elif new_order == "N":
            print("Thank you for ordering")
            exit(0)


def main():
    """ Main program """
    # customer_order = []
    # Default list of pastas
    # customer_order = [['Rigatoni alla Caponata', 2, 21],["Conchilglie alla Bolognese", 7, 22]]

    # Create empty order and pickup/delivery list
    customer_order = []
    pickup_delivery = []

    # List of pastas
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

    # Options for main menu
    option_list = [
        ["V", "View the menu"],
        ["A", "Add pasta to order"],
        ["R", "Review customer order"],
        ["D", "Delete item from customer list"],
        ["E", "Edit order"],
        ["O", "Option for pick up or delivery"],
        ["C", "Confirm order"],
        ["S", "Stop program"]
        ]

    # Main program
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
        elif user_choice == "C":
            confirm_order(customer_order, pickup_delivery)
        elif user_choice == "S":
            exit(0)
    print("Thank you, the program has ended")


if __name__ == '__main__':
    """ Default program that calls main """
    main()
