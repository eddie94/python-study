def check_datatype(arg):

    if type(arg) == str:
        if '.' in arg:
            return str, float(arg)
        else:
            return int, int(arg)
    elif type(arg) == int:
        return int, arg
    else:
        return float, arg

def Max(*args):
    max_value =args[0]
    max_data_type = None

    iter_objects = (list, tuple)

    try:
        for argument in args:
            if argument.__class__ in iter_objects:

                max_element = Max(*argument)

                current_data_type, max_element = check_datatype(max_element)

                if max_element >= max_value:
                    max_value = max_element
                    max_data_type = current_data_type
                else:
                    pass

            else:

                current_data_type,argument = check_datatype(argument)

                if argument >= max_value:
                    max_value = argument
                    max_data_type = current_data_type
                else:
                    pass

        if max_data_type == str and '.' not in max_data_type(max_value):
            return max_data_type(max_value).split('.')[0]
        else:
            return max_data_type(max_value)

    except ValueError:
        print('STR OBJECTS MUST BE 0~1')

print(Max(1, 2, [1, 12, ('123.12')]))