###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Octavio Vega
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # initialize dictionary to store cow names as keys and weights as values
    cow_dict = {}

    # open the file and read lines to get data
    with open(filename, 'r') as f:
        for line in f:
            data = line.split(',')
            name = data[0]
            weight = int(data[1]) # convert weight from str to int
            cow_dict[name] = weight # enter into dictionary
    
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # create a list of cow (name, weight) pairs reverse-sorted by weight
    cows_sorted = sorted(cows.items(), key=lambda x:x[1], reverse=True) # lambda to index the value of the item in dict
    
    # initialize overall list of trips
    trips = []
    
    # make the trips as long as there are cows left to take
    while len(cows_sorted) != 0:
        trip = []
        weight = 0
        i = 0
        print('\nNew trip started. Total weight:', weight)
        while weight <= limit and len(cows_sorted) != 0:
            # try the heaviest cow (always first element)
            cow, w = cows_sorted[i]
            
            # check that weight limit still met and cow not already taken
            if (weight + w <= limit) and cow not in trip:
                trip.append(cow) # put cow on trip
                weight += w # add cow's weight to total trip weight
                print(f"{cow} weighing {w} added to trip. Total trip weight:", weight)
                cows_sorted.remove(cows_sorted[i]) # removes cow from list of cows not taken
            elif (i + 1 < len(cows_sorted)) and len(cows_sorted)>1:
                i += 1 # try the next heaviest cow
            else:
                break # if no more cows can fit
        trips.append(trip)
        print('Trip Full! Total weight:', weight)
    print('\nAll cows transported! Total number of trips:', len(trips))
    print('-----------------------------------------------------------------------------')
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # make a copy of the cows dictionary
    cows_dict = dict(cows)
    
    # initialize a list to store trips
    trips = []
    
    # helper function to find weights of a partition of cows
    def get_weight(partition, cows):
        """
        Parameters:
            partition: a list of lists, each inner list is a set of cow names
            cows: a dictionary of cow (name, weight) pairs
        Returns: 
            a list of the weights for each set in the partition
        """
        weights = []
        for s in partition:
            weight = 0
            for cow in s:
                weight += cows[cow]
            weights.append(weight)
        return weights
    
    # check if each set in a partition can be a trip
    for part in get_partitions(cows_dict.keys()):
        part_weight = get_weight(part, cows_dict)
        
        # each sub-trip must have a weight not exceeding the limit
        if all(w <= 10 for w in part_weight):
            print(f"Successful trip: Transporting {part}")
            trips.append(part)
    
    return trips    

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
