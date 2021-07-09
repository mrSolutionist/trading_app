list_value = [12,2,2,3333,43,544,5,43,3,22,12,3,45,54,0]
def _list():
    for i in list_value:
        if i < list_value[0]:
            print(i)
        with open('value.txt', 'w') as f:
            f.write(str(i))
            
_list()

def write():
    with open('value.txt', 'w') as f:
        f.write('readme')

write()