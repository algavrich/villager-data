"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    # create var for opened file
    # create empty species list
    # iterate over file line by line
        # strip each line .rstrip(" ")
        # split each line at pipe delimeter
        # unpack list of split "things"
        # append given species to species list
    # turn species list into set
    # return species set

    # TODO: replace this with your code
    villager_data = open(filename)
    species_list = []
    for villager in villager_data:
        # villager.rstrip(" ")
        tokens = villager.split('|')
        name, species, personality, hobby, motto = tokens
        species_list.append(species)
        #print(name)
        # print(tokens)
    # print(species_list)
    species = set(species_list)
    return species

# print(all_species("villagers.csv"))
#Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.
    
    
    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    # TODO: replace this with your code

    # open villager_data to variable
    # create empty villager_names list
    # loop through each line in villager_data
        # split each line at pipe delimeter
        # unpack list of split "things"
        # if search_string is "All"
            # append name to villager_names
        # else
            # if species is same as search_string
                # append name to villager_names list
    villager_data = open(filename)
    villager_names = []
    for villager in villager_data:
        tokens = villager.split("|")
        name, species, personality, hobby, motto = tokens
        if search_string == "All":
            villager_names.append(name)
        else:
            if search_string == species:
                villager_names.append(name)
    return sorted(villager_names)

#print(get_villagers_by_species("villagers.csv", search_string="Anteater"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
