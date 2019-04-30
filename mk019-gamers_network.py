# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network
# information and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <user> is connected to <user1>, ..., <userM>.<user> likes to play
# <game1>, ..., <gameN>.
#
# For example:
#
# John is connected to Bryant, Debra, Walter.John likes to play The Movie:
# The Game, The Legend of Corgi, Dinosaur Diner.
#
# Note that each sentence will be separated from the next by only a period.
# There will not be whitespace or new lines between sentences.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists,
# dictionaries, and combinations of the two (e.g. lists of dictionaries).
# Pick one that will allow you to manage the data above and implement the
# procedures below.
#
# You may assume that <user> is a unique identifier for a user. For example,
# there can be at most one 'John' in the network. Furthermore, connections
# are not symmetric - if 'Bob' is connected to 'Alice', it does not mean that
# 'Alice' is connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in
# accomplishing a task. You are encouraged to test your code by using print
# statements and the Test Run button.
# -----------------------------------------------------------------------------

# Example string input. Use it to test your code.
example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse \
Adventures.Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, \
Dwarves and Swords.Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: \
The Fiscal Dilemma.Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# -----------------------------------------------------------------------------


def create_data_structure(string_input):
    """
    Parses a block of text and stores relevant information
    into a data structure. You are free to choose and design any
    data structure you would like to use to manage the information.
    Arguments:
    string_input: block of text containing the network information.
    Returns:
    The newly created network data structure
    """
    sentence_list = string_input.split(".")
    friend_list = [sentence_list[i].split(" is connected to ")
                   for i in range(len(sentence_list))
                   if i % 2 == 0 and sentence_list[i] != ""]
    games_list = [sentence_list[i].split(" likes to play ")
                  for i in range(len(sentence_list))
                  if i % 2 == 1 and sentence_list[i] != ""]
    network = {friend_list[i][0]:
               [friend_list[i][1].split(", "), games_list[i][1].split(", ")]
               for i in range(len(friend_list))}
    # for i in range(len(friend_list)):
    #     network[friend_list[i][0]] = [friend_list[i][1].split(", "),
    #                                 games_list[i][1].split(", ")]

    return network


def get_connections(network, user):
    """
    Returns a list of all the connections that user has.
    Arguments:
    network: the gamer network data structure.
    user:    a string containing the name of the user.
    Returns:
    A list of all connections the user has.
    - If the user has no connections, return an empty list.
    - If the user is not in network, return None.
    """
    if user not in network or network[user][0] == []:
        return None
    return network[user][0]


def get_games_liked(network, user):
    """
    Returns a list of all the games a user likes.
    Arguments:
    network: the gamer network data structure.
    user:    a string containing the name of the user.
    Returns:
    A list of all games the user likes.
    - If the user likes no games, return an empty list.
    - If the user is not in network, return None.
    """
    if user not in network or network[user][1] == []:
        return None
    return network[user][1]


def add_connection(network, user_A, user_B):
    """
    Adds a connection from user_A to user_B. Makes sure to check that
    both users exist in network.
    Arguments:
    network: the gamer network data structure.
    user_A:  a string with the name of the user the connection is from.
    user_B:  a string with the name of the user the connection is to.
    Returns:
    The updated network with the new connection added.
    - If a connection already exists from user_A to user_B, return network
    unchanged.
    - If user_A or user_B is not in network, return False.
    """
    if user_A not in network or user_B not in network:
        return False
    if user_B not in network[user_A][0]:
        network[user_A][0].append(user_B)
        return network[user_A][0]


def add_new_user(network, user, games):
    """
    Creates a new user profile and adds that user to the network, along with
    any game preferences specified in games. Assumes that the user has no
    connections to begin with.
    Arguments:
    network: the gamer network data structure.
    user: a string containing the name of the user to be added to the network.
    games: a list of strings containing the user's favorite games, e.g.:
    ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
    Returns:
    The updated network with the new user and game preferences added.
    The new user has no connections.
    - If the user already exists in network, returns network *UNCHANGED*.
    (does not change the user's game preferences)
    """
    if user not in network:
        network[user] = [[], games]
    return network


def get_secondary_connections(network, user):
    """
    Finds all the secondary connections (i.e. connections of connections)
    of a given user.
    Arguments:
    network: the gamer network data structure.
    user: a string containing the name of the user.
    Returns:
    A list containing the secondary connections (connections of connections).
    - If the user is not in the network, returns None.
    - If a user has no primary connections to begin with,
    returns an empty list.
    NOTE:
    It is OK if a user's list of secondary connections includes the user
    himself/herself. It is also OK if the list contains a user's primary
    connection that is a secondary connection as well.
    """
    if user not in network:
        return None
    if network[user][0] == []:
        return []
    return [person
            for group in
            [network[connection][0] for connection in network[user][0]]
            for person in group]


def count_common_connections(network, user_A, user_B):
    """
    Finds the number of people that user_A and user_B have in common.
    Arguments:
    network: the gamer network data structure.
    user_A:  a string containing the name of user_A.
    user_B:  a string containing the name of user_B.
    Returns:
    The number of connections in common (as an integer).
    - If user_A or user_B is not in network, returns False.
    """
    count = 0
    if user_A not in network or user_B not in network:
        return False
    for person in network[user_A][0]:
        if person in network[user_B][0]:
            count += 1
    return count


def create_path(network, user_A, user_B, path=[]):
    """
    Finds a connections path from user_A to user_B using recursion.
    It has to be an existing path but it DOES NOT have to be the
    shortest path. Circular loops returns None (for example,
    A is connected to B. B is connected to C. C is connected to B.).
    Arguments:
    network: The network created with create_data_structure.
    user_A:  String holding the starting username.
    user_B:  String holding the ending username.
    path: The current path(for recursion).
    Returns:
    A list showing the path from user_A to user_B.
    - If such a path does not exist, returns None.
    Sample output:
    print find_path_to_friend(network, "Abe", "Zed")
    ['Abe', 'Gel', 'Sam', 'Zed']
    This implies that Abe is connected with Gel,
    who is connected with Sam, who is connected with Zed.
    """
    path = path + [user_A]  # all paths include starting node
    if user_A == user_B:  # id the last node is user_B a valid path exists
        return path  # base case
    for node in network[user_A][0]:
        if node not in path:  # otherwise path is an infinite loop
            path = create_path(network, node, user_B, path)
            if path:  # after the recursion hits the base case
                return path
    return None


def find_path_to_friend(network, user_A, user_B):
    """
    Finds whether both input users are in network or not.
    If they are, calls create_path function.
    Arguments:
    network: The network created with create_data_structure.
    user_A:  String holding the starting username.
    user_B:  String holding the ending username.
    Returns:
    A call to create_path function.
    """
    if user_A not in network or user_B not in network:
        return None
    # if both users exist there may be a path
    return create_path(network, user_A, user_B)


net = create_data_structure(example_input)
print(net)
print(get_connections(net, "Debra"))
print(get_connections(net, "Mercedes"))
print(get_games_liked(net, "John"))
print(add_connection(net, "John", "Freda"))
print(add_new_user(net, "Debra", []))
print(add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]))
print(get_secondary_connections(net, "Mercedes"))
print(count_common_connections(net, "Mercedes", "John"))
print(find_path_to_friend(net, "John", "Ollie"))
