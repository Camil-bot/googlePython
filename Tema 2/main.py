import MyModule


def your_function(*args, **kwargs):
    total = 0
    for item in args:
        try:
            tmp = int(item)
            total += tmp
        except ValueError:
            continue
        except TypeError:
            continue

    return total


def input_echo():
    try:
        tmp = int(input('Give a number or else there will be consequences \n'))
        print(tmp)
    except TypeError:
        print('Told you there would be consequences')
    except ValueError:
        print('Told you there would be consequences')


rez = MyModule.recursive_sum_impar(4)
print(rez)


