
def e_state_exists(list,state): #check if state exists in explored list
    i = 0
    while i < len(list):
        if list[i] == state: return True
        i += 1
    return False

def e_exists_element(list,state):
    i = 0
    while i < len(list):
        if list[i] == state: return i
        i += 1
    return False