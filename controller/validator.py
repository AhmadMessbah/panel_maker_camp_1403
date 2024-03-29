import re


def name_validator(name):
    return bool(re.match(r"^[a-zA-Z\s]{3,30}$", name))
def family_validator(family):
    return bool(re.match(r""))
