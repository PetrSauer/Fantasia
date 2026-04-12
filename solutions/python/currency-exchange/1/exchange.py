"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    exchanged_cur = 1 / exchange_rate
    convert_back_to_home_cur = budget * exchanged_cur
    print(convert_back_to_home_cur)
    return convert_back_to_home_cur
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    pass


def get_change(budget, exchanging_value):
    budget_left = budget - exchanging_value
    return budget_left
    
    """
    
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    pass


def get_value_of_bills(denomination, number_of_bills):
    calc_val_of_bills = denomination * number_of_bills
    return calc_val_of_bills
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    pass


def get_number_of_bills(amount, denomination):
    calc_num_of_bills = int(amount) / int(denomination) 
    return round(calc_num_of_bills)
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    pass


def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = spread / 100
    actual_rate = exchange_rate * (1 + spread_decimal)

    exchanged_money = budget / actual_rate

    max_whole_value = int(exchanged_money // denomination) * denomination

    return int(max_whole_value)


    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    pass
