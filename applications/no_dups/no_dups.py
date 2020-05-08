def no_dups(string):
    storage = dict()
    # Loop over the input string, assign each word in the string to a dictionary key
    for word in string.split():
        if word not in storage:    # [ cats, dogs, fish, ]
            storage[word] = 1
        elif word in storage:
            storage[word] += 1
    result = " ".join(storage.keys())
    return result




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))