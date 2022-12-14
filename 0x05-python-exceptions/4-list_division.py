#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []

    for item in range(0, list_length):
        try:
            division = my_list_1[item] / my_list_2[item]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            my_new_list.append(divsion)
    return (my_new_list)
