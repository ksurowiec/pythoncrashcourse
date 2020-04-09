def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, mode='r', encoding='utf-8') as file_reader:
            content = file_reader.read()
    except FileNotFoundError:
        print(f'Sorry the file {filename} cannot be found!')
    else:
        words = content.split()
        num_words = len(words)
        print(f'The file {filename} has {num_words} words.')
