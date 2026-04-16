"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    #Add to express_queue
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    #Add to normal_queue    
    else: 
        normal_queue.append(person_name)
        return normal_queue
    pass


def find_my_friend(queue, friend_name):
    #.index() to find a place in queue
    return queue.index(friend_name)
    
    pass


def add_me_with_my_friends(queue, index, person_name):
    #adding to friens .insert()
    queue.insert(index, person_name)
    return queue

    pass


def remove_the_mean_person(queue, person_name):
    #Using .remove() to remove the troublemaker
    queue.remove(person_name)
    return queue
 
    pass


def how_many_namefellows(queue, person_name):
    #using .count() returning the result as INT
    result = int(queue.count(person_name))
    return result

    pass


def remove_the_last_person(queue):
    #Using .pop() to remove last person
    return queue.pop()

    pass


def sorted_names(queue):
    # Sort this out 
    new_sorted_list = sorted(queue)
    return new_sorted_list
    
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    pass
