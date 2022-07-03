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

def main():
    customer_order = []
    #customer_order = [['Rigatoni alla Caponata', 2, 21],["Conchilglie alla Bolognese", 7, 22]]

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
        elif user_choice == "S":
            exit(0)
    print("Thank you, the program has ended")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()