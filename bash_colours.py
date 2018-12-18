def print_format_table():
    """
    prints table of formatted text format options
    """
    for bg in range(40,48):
        for fg in range(30,38):
            s1 = ''
            for style in range(8):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()
a = input("press <enter> to close")
