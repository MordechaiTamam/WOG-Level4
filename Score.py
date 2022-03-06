import Utils


def add_score(value):
    with open(utils.SCORES_FILE_NAME, 'r+') as file:
        data = int(file.read())
        file.seek(0)
        file.write(str(data+value))

