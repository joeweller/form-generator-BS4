import BS4_gen

OPTIONS = {
        'size': '',  # sm = 'form-control-sm', re = '', lg = 'form-control-lg'
        'placeholder': '',  # text for placeholder
        'label': '',  # text for label
        'type': '',  # for function call to relevent type
        'text-type': ''  # second type for 'text': password, email, text
    }

def main():

    print("BS4 Form Widget Generator.")

    get_type()

    return

def get_type():
    """display menu and get widget type"""
    opt = ['text',]
    inp = display_menu(opt, 'Select Widget:')

    OPTIONS['type'] = opt[inp]  # set option

    if OPTIONS['type'] == 'text':
        get_texttype()

    return

def get_texttype():
    opt = ['text', 'email', 'password']
    inp = display_menu(opt, 'Select text type:')

    OPTIONS['text-type'] = opt[inp]

    return

def display_menu(opt_list, title):
    """Generate a menu"""
    print(title)
    count = 0
    for o in opt_list:
        print('({number}) : {option}'.format(number=count, option=o))
    return input_loop(opt_list.count)

def input_text(message=''):
    return input(message)

def input_loop(menu_range):
    """Loop input for options menus"""
    def check(inp, rng):

        try:
            chk = int(inp)
        except ValueError:
            return False

        if int(chk) in range(0, rng):
            return True

    inpu = input('choose option: ')

    while check(inpu, menu_range) == False:
        inpu = input('try again: ')

    return int(inpu)

if __name__ == "__main__":
    main()
