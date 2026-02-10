def todo_search(entry):
    if not isinstance(entry, str):
        raise TypeError('Entry must be a string')
    return '#TODO' in entry