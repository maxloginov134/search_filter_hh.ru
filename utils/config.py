from configparser import ConfigParser


def config(filename, section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    bd = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            bd[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return bd