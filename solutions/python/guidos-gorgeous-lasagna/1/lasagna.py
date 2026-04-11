EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate remaining bake time."""
    remain = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remain


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers."""
    prep_time = number_of_layers * 2
    return prep_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time."""
    total_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_time


# Function calls
print(preparation_time_in_minutes(2))
print(bake_time_remaining(30))
print(elapsed_time_in_minutes(3, 20))