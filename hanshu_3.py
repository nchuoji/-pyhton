def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
xingming = get_formatted_name('mang', 'panpai')
print(xingming)