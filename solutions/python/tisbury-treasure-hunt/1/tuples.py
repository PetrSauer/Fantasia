"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    unpack = [record]
    return record[1]
    pass


def convert_coordinate(coordinate):
    split = tuple(coordinate)
    return split

    pass


def compare_records(azara_record, rui_record):

    azara_cord = azara_record[1]
    rui_cord = rui_record[1]
    formated_rui = rui_cord[0] + rui_cord[1]
    return formated_rui == azara_cord

    pass


def create_record(azara_record, rui_record):
    azara_cord = azara_record[1]
    rui_cord = rui_record[1]
    formated_rui = rui_cord[0] + rui_cord[1]

    if formated_rui == azara_cord:
        return azara_record + rui_record
    else:
        return 'not a match'
    
    pass




def clean_up(combined_records):
    report = ""
    
    for record in combined_records:
        cleaned_record = (record[0], record[2], record[3], record[4])
        report += str(cleaned_record) + "\n"
        
    return report
    pass
