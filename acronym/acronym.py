def abbreviate(words):
    # cleanup words of special characters
    words = words.replace('-', ' ')
    words = words.replace('_', '')

    # split input into list of words for ease
    list_words = words.split()
    first_char = [w[:1].upper() for w in list_words]

    return ''.join(first_char)
