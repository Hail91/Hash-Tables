import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
# TODO: analyze which words can follow other words
# Your code here
cache = {}
# we have to split the words into individual words- turns it into a list
words_list = words.split()
test_list = ["Cats", "and", "dogs", "and",
             "birds", "and", "fish", "dogs", "birds"]
# look at each word
for idx, word in enumerate(words_list):
    # if word is in cache already, just append next word in existing []
    if idx < (len(words_list) - 1):
        if word in cache:
            cache[word].append(words_list[idx + 1])
        # if word is not in cache already, create new key idx and [with next word value in list]
        else:
            cache[word] = [words_list[idx + 1]]
    else:
        break
    # do we need pointers?
    # appending next word to list at key of "cat" for example
# TODO: construct 5 random sentences
# Your code here
# we want to loop through the cache keys and find "start" and "stop" words
    # if word is capitalized or starts with "followed by a capital
        # add to start: [word]
    # if word ends with .?! or ." ?" !"
        # add to stop: [word]
start_stop_cache = {
    "start": [],
    "stop": []
}
keys = list(cache.keys())
punct = [".", "?", "!"]
quote_punct = [".\"", "?\"", "!\""]
for key in keys:
    first_char = key[0]
    first_two_char = key[:2]
    last_char = key[len(key) - 1]
    last_two_char = key[:-2]
    if first_char.isupper() or first_two_char == ("\"" + first_char.upper()):
        start_stop_cache["start"].append(key)
    if last_char in punct or last_two_char in quote_punct:
        start_stop_cache["stop"].append(key)
# print(start_stop_cache["stop"])
random_start = random.choice(start_stop_cache["start"])
print(random_start, end=" ")
current_word = random_start
while current_word not in start_stop_cache["stop"]:
    new_word = random.choice(cache[current_word])
    if new_word in start_stop_cache["stop"]:
        print(new_word)
        break
    else:
        print(new_word, end=" ")
        current_word = new_word
