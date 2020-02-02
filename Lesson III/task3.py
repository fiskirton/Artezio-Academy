"This module contains function for working with arithmetic mean"


def mean(arg_a, arg_b, arg_c, arg_d):

    """
    This function returns the arithmetic mean of the arguments and
    the largest argument for all time calls to this function
    """

    args = [arg_a, arg_b, arg_c, arg_d]
    args_len = len(args)
    current_mean = sum(args) / args_len

    try:
        mean.max_item = max(mean.max_item, max(args))
    except AttributeError:
        mean.max_item = max(args)

    return current_mean, mean.max_item


# print(mean(4,4, 5, 6))
# print(mean(1,2,3,4))
