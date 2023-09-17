import json

# TODO: make an automatic module import
# for module in modules:
#     import module
core_input = str


def debug(inpt):
    return inpt + ' it works'


def debug_2(inpt):
    return '> ' + inpt + ''


def echo(inpt):
    if ' > ' not in inpt:
        return inpt
    else:
        with open(inpt.split(' > ')[1], 'w') as new_file:
            new_file.write(inpt.split(' > ')[0])
            new_file.close()
            return f'Text was saved to {inpt.split(" > ")[1]}'


def update(function):
    with open("core_transfer.json", 'r') as f:
        data = json.load(f)
        core_input = data["main_input"]

    try:
        core_output = function(core_input)
    except TypeError:
        core_output = "Error: TypeError. Function name is probably invalid."

    with open("core_transfer.json", 'w+') as f:
        # print(data)
        data['main_output'] = core_output
        # print(data)
        json.dump(data, f)
