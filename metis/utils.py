
def read_text(filename: str):
    """
    Read text from a file
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        out = f.read()
    return out