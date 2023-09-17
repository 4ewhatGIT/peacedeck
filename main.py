import json

import core

turned_on = True

data = []
main_input = ''
main_output = ''

functions = [core.debug, core.debug_2, core.echo]


def main(current):
    main_input = input('> ')
    with open("core_transfer.json", 'r') as f:
        data = json.load(f)
        # print(data)

    with open("core_transfer.json", 'w+') as f:
        # print(data)
        data['main_input'] = main_input
        # print(data)
        json.dump(data, f)

    with open("core_transfer.json", 'r') as f:
        core.update(functions[current])
        data = json.load(f)
        main_output = data["main_output"]

    print(main_output)


if __name__ == '__main__':
    while turned_on:
        current = int(input(f'select a funtion to use (0-{len(functions) - 1}):\n'))
        main(current)
