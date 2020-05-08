def word_count(string):
    storage = dict()
    empty_dict = {}
    bad_chars = [':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(',  ')', '*', '^', '&', '"']
    for word in string.split():
        word = ''.join(c for c in word if not c in bad_chars)
        word = word.lower()
        if len(word) > 0:
            if word not in storage:
                storage[word] = 1
            else:
                storage[word] += 1    
    return storage


if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))