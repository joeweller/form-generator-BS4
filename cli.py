from BS4_gen import BS4Gen
import os

collected = []  # list of options selected for viewing

OPTIONS = {
        'size': '',  # small = 'form-control-sm', regular = '', large = 'form-control-lg'
        'placeholder': '',  # text for placeholder
        'label': '',  # text for label
        'type': '',  # for function call to relevent type
        'text-type': '',  # second type for 'text': password, email, text
        'id': '',  # widget id
        'small-hint': ''
    }


def main():

    print("BS4 Widget Generator")

    get_type()
    get_placeholder()
    get_label()
    get_id()
    get_size()
    get_small_hint()
    display_collected()
    print('output:\n\n')
    output = BS4Gen(OPTIONS).get_widget()
    print(output)
    return


def get_small_hint():
    """get input for small hint"""
    inp = option_text('Input "small" hint (leave blank for no hint)')
    add_to_collected('small hint', inp)
    OPTIONS['small-hint'] = inp
    return


def get_size():
    """get size for widget"""
    opt = ['regular', 'small', 'large']
    inp = option_menu(opt, 'Widget size:')
    OPTIONS['size'] = opt[inp]
    add_to_collected('size', opt[inp])
    return


def get_label():
    """get label for widget. '' if not widget required"""
    inp = option_text('Input label name (leave blank for no label):')
    add_to_collected('label', inp)
    OPTIONS['label'] = inp
    return


def get_id():
    """get id for widget"""
    inp = option_text('Input widget id:')
    add_to_collected('id', inp)
    OPTIONS['id'] = inp
    return


def get_placeholder():
    """get placeholder"""
    inp = option_text('Input placeholder (leave blank for no placeholder):')
    add_to_collected('placeholder', inp)
    OPTIONS['placeholder'] = inp
    return


def get_type():
    """get widget type"""
    opt = ['text', ]
    inp = option_menu(opt, 'Select widget:')

    OPTIONS['type'] = opt[inp]  # set option

    add_to_collected('type', opt[inp])

    if OPTIONS['type'] == 'text':
        get_text_type()
    return


def get_text_type():
    """get type of text widget"""
    opt = ['text', 'email', 'password']
    inp = option_menu(opt, 'Select text type:')

    # mark text type with option
    OPTIONS['text-type'] = opt[inp]

    # add option to collected list
    add_to_collected('text type', opt[inp])

    return


def option_menu(opt_list, title):
    """Generate a menu"""
    if collected:
        display_collected()

    print(title)
    count = 0
    for o in opt_list:
        print('({number}) : {option}'.format(number=count, option=o))
        count += 1

    return input_loop(len(opt_list))


def option_text(message=''):
    display_collected()
    return input(message)


def input_loop(menu_range):
    """Loop input for options menus"""
    def check(inp, rng):

        try:
            chk = int(inp)
        except ValueError:
            return False

        if chk in range(0, rng):
            return True
        else:
            return False

    print('-' * 20)  # spacer

    inpu = input('choose option: ')

    while not check(inpu, menu_range):
        inpu = input('try again: ')

    return int(inpu)


def add_to_collected(wtype, option):
    """add collected options to list"""
    collected.append('{} = {}'.format(wtype, option, ))
    return


def display_collected():
    """Display selected options list"""
    os.system('clear')  # clearscreen
    print('BS4 widget generator')
    print('-' * 20)
    print('options selected:')
    for col in collected:
        print(col)

    print('-' * 20)

    return


if __name__ == "__main__":
    main()
