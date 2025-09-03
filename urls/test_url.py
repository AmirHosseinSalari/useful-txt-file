import validators


def validate():
    with open('urls.txt', 'r') as file:
        for line in file:
            url = line.strip()
            if (validators.url(url)):
                print('is valid:' + line)
            else:
                print('is not valid:' + line)


validate()
