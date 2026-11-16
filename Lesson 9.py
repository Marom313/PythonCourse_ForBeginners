import marom_solution_3


def precent(whole, part):
    return (part / whole) * 100


def precent_str(whole, part):
    return str((part / whole) * 100) + ' ' + '%'


print(precent_str(1000, 25))
