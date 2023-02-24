

def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    name_list = []
    for name in names:
        badge = badge_maker(name)
        name_list.append(badge)
    return name_list
        

def assign_rooms(names):
    rooms = []
    for i in range (1, 9):
        message = f"Hello, {names[i-1]}! You'll be assigned to room {i}!"
        rooms.append(message)
    return rooms

def printer(names):
    badge_names = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for name in badge_names:
        print(name)
    for message in rooms:
        print(message)
    

