#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        oprtn = a / b
    except:
        oprtn = None
    finally:
        print('Inside result: {}'.format(oprtn))
        return oprtn
