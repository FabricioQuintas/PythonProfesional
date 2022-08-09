# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = [] # Create new list
    for element in some_list: # Itinerate through the arg
        # If the element not in our list, append it
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates # Return list without duplicates

# Challenge: Do the remove duplicates function with sets
def remove_duplicates1(some_list):
    # Make the some_list a set, it will remove duplicates, and make it a list again
    return list(set(some_list))

def run():
    list = [1, 1, 2, 2, 4]
    print(remove_duplicates1(list))

if __name__ == '__main__':
    run()