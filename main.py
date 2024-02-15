import time


def main() -> None:

    startTime = time.time()
    for trial in range(10_000):
        building_str = ''
        for i in range(10_000):
            building_str += 'x'
    print('String concatenation: ', (time.time() - startTime))

    startTime = time.time()
    for trial in range(10_000):
        building_list = []
        for i in range(10_000):
            building_list.append('x')
        building_str = ''.join(building_list)
    print('List appending: ', (time.time() - startTime))


if __name__ == '__main__':
    main()
