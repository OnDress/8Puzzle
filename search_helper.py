
def q_state_exists(list,state): #check if state exists in frontier
    i = 0
    while i < len(list):
        if list[i].state == state: return True
        i += 1
    return False

def exists_element(list,state): #find index of existing state in q
    i = 0
    while i < len(list):
        if list[i].state == state: return i
        i += 1
    return False

def e_state_exists(list,state): #check if state exists in explored list
    i = 0
    while i < len(list):
        if list[i] == state: return True
        i += 1
    return False