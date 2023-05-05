
def state_exists(list,state):
    i = 0
    while i < len(list):
        if list[i].state == state: return True
        i += 1
    return False

def exists_element(list,state):
    i = 0
    while i < len(list):
        if list[i].state == state: return i
        i += 1
    return False