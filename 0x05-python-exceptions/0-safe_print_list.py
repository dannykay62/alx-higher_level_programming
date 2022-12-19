#!/bin/bash/python2.8

def safe_print_list(my_list=[], x=0):
    """Function prints x elements oflist

    Args:
        my_list (lost): The list to print elements from.
        x (int): number of elements to be printed by my_list

    Returns:
        The number of elements printed
    """

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
                    ret +=1
        except IndexError:
            break
    print("")
    return (ret)