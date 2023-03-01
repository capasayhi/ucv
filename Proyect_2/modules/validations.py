def valComplex(num, array=None):
    status = True
    if not isinstance(num, complex):
        status = False

    if array != None:
        complex_num_module = abs(num)

        if isinstance(array, tuple):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered"
                                 "in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than"
                                 "two elements")
            elif complex_num_module <= array[0] or \
                    complex_num_module >= array[-1]:
                status = False

        elif isinstance(array, list):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered"
                                 " in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than"
                                 " two elements")
            elif complex_num_module < array[0] or \
                    complex_num_module > array[-1]:
                status = False

        else:
            raise TypeError("The second argument is not the right type")

    return status


def valFloat(num, array=None):
    variable = True
    if not isinstance(num, float):
        variable = False

    if array != None:
        if isinstance(array, tuple):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered"
                                 "in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than"
                                 "two elements")
            elif num <= array[0] or num >= array[-1]:
                variable = False
        elif isinstance(array, list):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered"
                                 " in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than"
                                 " two elements")
            elif num < array[0] or num > array[-1]:
                variable = False
        else:
            raise TypeError("The second argument is not the right type")

    return variable


def valInt(num, array=None):
    variable = True
    if not isinstance(num, int):
        variable = False
        return variable

    if array != None:
        if isinstance(array, tuple):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered"
                                 "in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than"
                                 "two elements")
            elif num <= array[0] or num >= array[-1]:
                variable = False
        elif isinstance(array, list):
            if array[0] >= array[-1]:
                raise ValueError("The range provided is not ordered"
                                 " in an increasing way")
            elif len(array) != 2:
                raise ValueError("The range provided has more than"
                                 " two elements")
            elif num < array[0] or num > array[-1]:
                variable = False
        else:
            raise TypeError("The second argument is not the right type")

    return variable


def valList(array, var=None, string=None):
    status = True
    if not isinstance(array, list):
        status = False

    if var != None or string != None:
        if string == "value":
            if isinstance(var, list):
                if not var == array:
                    status = False
            else:
                status = False
        elif string == "len":
            if isinstance(var, int):
                var = str(var)
                if not len(array) == len(var):
                    status = False
            else:
                status = False
        else:
            if var != list or var != int:
                raise TypeError("The second argument is not "
                                "of a list or int type")
            else:
                raise ValueError("The third argument is not 'value' "
                                 "or 'len'")

    return status
