def create_phone_number(n):
    return ("({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(*n))

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])