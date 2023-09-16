import json

# TODO: make an automatic module import
# for module in modules:
#     import module
core_input = str

def debug(inpt):
    return inpt + ' it works'


def update():
    with open("core_transfer.json", 'r') as f:
        data = json.load(f)
        core_input = data["main_input"]

    core_output = debug(core_input)

    with open("core_transfer.json", 'w+') as f:
        print(data)
        data['main_output'] = core_output
        print(data)
        json.dump(data, f)


