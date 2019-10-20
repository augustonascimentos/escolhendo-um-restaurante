def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))


def one():
    return "January"


def two():
    return "February"


def three():
    return "March"


def four():
    return "April"


def five():
    return "May"


def six():
    return "June"


def seven():
    return "July"


def eight():
    return "August"


def nine():
    return "September"


def ten():
    return "October"


def eleven():
    return "November"


def twelve():
    return "December"


def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print(func())


class Switcher(object):
    def numbers_to_months(self, argument):
        """Dispatch method"""
        method_name = 'month_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()

    def month_1(self):
        return "January"

    def month_2(self):
        return "February"

    def month_3(self):
        return "March"


print(Switcher().numbers_to_months(2))


def sayhello(*names):
    for name in names:
        print(f"Hello, {name}")


tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])