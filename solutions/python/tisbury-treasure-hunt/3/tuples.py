"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    if record is None or len(record) <= 1:
        return ''
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)

    


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    _, azara_coords = azara_record
    _, rui_coords, _ = rui_record

    return (convert_coordinate(azara_coords) == convert_coordinate(rui_coords))


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return (azara_record + rui_record)
    return 'not a match'


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    out_str = """"""
    for record in combined_record_group:
        rec0, rec1, rec2, rec3, rec4 = record
        if convert_coordinate(rec1) == convert_coordinate(rec3):
            out_str += f"('{rec0}', '{rec2}', {convert_coordinate(rec3)}, '{rec4}')\n"
        else:
            out_str += f"{record}\n"
    return out_str
            
    
    
