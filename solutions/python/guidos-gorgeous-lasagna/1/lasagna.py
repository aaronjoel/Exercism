# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for the lasagna.
    
    :param number_of_layers: int the number of layers of the lasagna.
    :return: int total preparation time derived from 'PREPARATION_TIME'.
    
    Function that takes the number of layers of the lasagna and returns
    how many minutes are needed to prepare it based on the 
    `PREPARATION_TIME`.
    """

    return number_of_layers * PREPARATION_TIME
    
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time the lasagna has been baking for.
    
    :param number_of_layers: int the number of layers of the lasagna.
    :elapsed_bake_time: int the number of minues the lasagna has been cooking.
    :return: int the total number of minutes the lasagna has been cooking. This
    includes the preparation time.

    Function that takes the number of layers of the lasagna and the
    elapsed_bake_time and returns the time the lasagna has already spent baking
    since preparation."""
    
    prep_time = number_of_layers * PREPARATION_TIME
    time_baking = prep_time + elapsed_bake_time
    return time_baking