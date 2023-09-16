import json

import core

data = []
main_input = ''
main_output = ''


def main():
    main_input = input('test: ')
    with open("core_transfer.json", 'r') as f:
        data = json.load(f)
        print(data)

    with open("core_transfer.json", 'w+') as f:
        print(data)
        data['main_input'] = main_input
        print(data)
        json.dump(data, f)

    with open("core_transfer.json", 'r') as f:
        core.update()
        data = json.load(f)
        main_output = data["main_output"]

    print(main_output)


if __name__ == '__main__':
    main()
