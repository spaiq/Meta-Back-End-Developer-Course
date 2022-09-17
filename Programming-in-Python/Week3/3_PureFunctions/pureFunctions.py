my_list = [1,2,3]

def add_to_list(lst, item):
    new_lst = lst.copy()
    new_lst.append(item)
    return new_lst

new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)