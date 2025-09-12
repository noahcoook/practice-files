
def print_list(list):
    if len(list) == 0:
        print('please insert atleast one item')
    if len(list) == 1:
        for name in list:
            print(name)
    if len(list) > 1:
        list.insert (-1, 'and')
        for names in spam:
            if names == list[-1]:
                print(names)
            else:
                print(names, end=', ')
        

spam = []
#spam = ['feet', 'toes', 'socks', 'toast', 'rice', 'food'] 
print_list(spam)


# spam = ['beans', 'toast', 'rice']

# if len(spam) > 1:
#     spam.insert(-1, 'and')
#     for names in spam:
#         print(names, end=', ')