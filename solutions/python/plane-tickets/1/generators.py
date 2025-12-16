"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    current_letter = 'A'
    i = 0
    while i < number:
        yield current_letter
        current_letter = chr(ord(current_letter) + 1)
        i += 1
        if i % 4 == 0:
            current_letter = 'A'
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    curr_seat_row = 1
    curr_num_seat = 0
    while curr_num_seat < number:
        ## Check if we are dealing with row 13 and skip it
        if curr_seat_row == 13:
            curr_seat_row += 1
        for letter in generate_seat_letters(4):
            if curr_num_seat == number:
                break 
            yield f"{curr_seat_row}{letter}"
            curr_num_seat += 1
        curr_seat_row += 1
            

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    num_seats = len(passengers)
    return {
        passenger : seat for passenger, seat in zip(passengers, generate_seats(num_seats))
    }

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    curr_idx = 0
    n = len(seat_numbers)
    while curr_idx < n:
        seat_number = seat_numbers[curr_idx]
        zeros = '0' * (12 - len(seat_number) - len(flight_id))
        yield f"{seat_number}{flight_id}{zeros}"
        curr_idx += 1
