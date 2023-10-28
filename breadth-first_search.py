# Search for a name with a certain number of letters. O(V + E),
# V is the number of vertices (people), and E is the number of edges (connections) between them.


from collections import deque
import random

# Dictionary representing relationships between people
people = {
    "you": ["aliceee", "bob", "claire"],
    "bob": ['anuj', "peggy"],
    "aliceee": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


# function to check if a name has the required number of letters
def person_name_has_needed_length(name: str, needed_name_length: int) -> bool:
    return len(name) == needed_name_length


def search(name: str, needed_name_length: int) -> bool:
    search_queue = deque()
    search_queue += people[name]  # start with the initial name
    searched = []  # list to keep track of names already checked

    while search_queue:
        person = search_queue.popleft()  # get the first name from the queue

        if person not in searched:
            if person_name_has_needed_length(person, needed_name_length):

                # if the name fits, print a message and end the search
                print(f"{person} contains the required number of letters in the name: {needed_name_length}")
                return True

            # add related names to the queue for further search
            search_queue += people[person]

            searched.append(person)  # add the name to the list of checked names

    # if no suitable name is found
    print(f"A person containing the required number of letters in the name was not found: {needed_name_length}")
    return False


search("you", random.randint(3, 7))
