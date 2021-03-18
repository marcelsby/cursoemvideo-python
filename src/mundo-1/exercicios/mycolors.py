# Front-end para cores e estilos ANSI desenvolvido por mim
def colorthis(text='', style='default', font='default', background='default'):
    tipography = {
        'style': {
            'default': '0',
            'bold': '1',
            'italic': '3',
            'underlined': '4',
            'inverted': '7'
        },
        'font': {
            'default': '',
            'white': '29',
            'black': '30',
            'red': '31',
            'green': '32',
            'yellow': '33',
            'blue': '34',
            'purple': '35',
            'cyan': '36',
            'grey': '37'
        },
        'background': {
            'default': '',
            'black': '40',
            'red': '41',
            'green': '42',
            'yellow': '43',
            'blue': '44',
            'purple': '45',
            'cyan': '46',
            'grey': '47',
        }
    }

    sty_arg = style
    fc_arg = font
    bg_arg = background

    esc_start = '\033[{};{}{}m{}'.format(tipography['style'][sty_arg],
                                         tipography['font'][fc_arg],
                                         tipography['background'][bg_arg],
                                         str(text))
    esc_end = '\033[m'

    colored = '{}{}'.format(esc_start, esc_end)

    return colored

# greeting = 'Hello World!'
# print(colorthis(greeting, font='blue'))
