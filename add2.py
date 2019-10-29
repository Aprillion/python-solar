"""TODO"""

def add_one(x):
    if x == 9:
        print('Warning: might take longer')
    elif x >= 10:
        return 'too big'
    print('processing...')
    return x + 1

if __name__ == '__main__':
    result = add_one(1)
    print(result)
    print(add_one(11))
    print(add_one(9))
