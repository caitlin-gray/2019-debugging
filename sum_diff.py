from numbers import Number


def add(arg1, arg2):
    return arg1 + arg2


def sub(arg1, arg2):
    assert isinstance(arg1, Number)
    assert isinstance(arg2, Number)
    result = sub_pre_checked(arg1, arg2)
    return result


def sub_pre_checked(arg1, arg2):
    return arg1 - arg2


def div(arg1, arg2):
    assert isinstance(arg1, Number)
    assert isinstance(arg2, Number)
    result = div_pre_checked(arg1, arg2)
    return result


def div_pre_checked(arg1, arg2):
    return arg1 / arg2


def sum_over_difference(arg1, arg2):
    """Compute sum of arguments over difference of arguments."""
    arg_sum = add(arg1, arg2)
    arg_diff = sub(arg1, arg2)
    sum_over_diff = div(arg_sum, arg_diff)
    return sum_over_diff


if __name__ == '__main__':
    result = sum_over_difference(12., 12.)
    print(result)

