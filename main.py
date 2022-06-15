def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string

def print_with_indexes(l):
    for i in range (0, len(l)):
        output = " {:3} : {:10} {:10}".format(i, l[i][0], l[i][1])
        print(output)

def main():
    pasta_list = [
        ["Linguine Gamberi", " $23"],
        ["Fusilli Pesto", "$19"],
        ["Conchilglie alla Bolognese", " $22"],
        ["Rigatoni alla Caponata", "$21"],
        ["Fettuccine Carbonara", "$20"],
        ["Spaghetti Pomodoro", "$16"],
        ["Pappardelle Ricci D’Angello", "$26"],
        ["Raviolo di Salsiccia", "$22"],
        ["Ravioli di Ricotta", "$20"]
    ]

    option_list = [
        ["R", "Review the menu"],
        ["S", "Stop program"]
        ]
    #add_new_entry(fruit_list)

    run_program=True
    while run_program:
        for x in option_list:
            output = "{} -- {} ".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: ->").upper()
        print(user_choice)
        if user_choice == "R":
            print(pasta_list)
        elif user_choice == "S":
            exit(0)
    print("Thank you, the program has ended")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


