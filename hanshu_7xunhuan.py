def get_formatted_name(xing_x, ming_m):
    """返回整洁的姓名"""
    full_name = xing_x + ' ' + ming_m
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("xing_x: ")
    if f_name == 'q':
        break
    l_name = input("ming_m: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")