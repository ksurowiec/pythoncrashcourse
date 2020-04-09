def get_formatted_name(firstname, lastname, middle=None):
    if middle:
        return f'{firstname} {middle} {lastname}'.title()
    else:
        return f'{firstname} {lastname}'.title()
