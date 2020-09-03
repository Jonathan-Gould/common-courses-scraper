import pickle

# loads the saved dictionary of all the courses scraped
with open("classmates.pickle", "rb") as fhan:
    a = pickle.load(fhan)

# this is a way to map integers to class names
g_keys = list(a.keys())


def ks():
    "A way to get a listing of the integer-course pairings"
    return list(enumerate(g_keys))


def most_common(excludes=[]):
    """"
    This returns a list of classmates sorted from most to least common courses
    You can exclude courses from consideration by passing their integer keys in the excludes parameter
    """
    excludes = [g_keys[i] for i in excludes]
    classmates = {}
    for course in a:
        if course in excludes:
            continue
        for person in a[course]:
            classmates[person] = classmates.get(person, 0) + 1
    l = [(value, key) for key, value in classmates.items()]
    l.sort(reverse=True)
    return l[:30]


def common(includes=[]):
    """"
    This returns a list of classmates that are in all of the classes you specify in the includes parameter.
    To specify classes, pass their int keys in a list:
    >>> common([12, 4])
    """
    courses = []
    for c in includes:
        courses.append(g_keys[c])
    classmates = {}
    for course in courses:
        for person in a[course]:
            classmates[person] = classmates.get(person, 0) + 1
    l = [key for key, value in classmates.items() if value == len(includes)]
    l.sort(reverse=True)
    return l


def which_classes(name):
    """
    This returns a list of the classes you have in common with some person.
    It's usually best to use their NetId as the search string.
    """
    courses = set()
    for course in a:
        for person in a[course]:
            if name in person:
                print(person)
                # this prints all matches so you know about false positives
                courses.add(course)
    return courses
