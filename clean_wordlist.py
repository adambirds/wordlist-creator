import os

existing_words = []
with open('wordlist.txt', 'r') as f:
    for line in f:
        existing_words.append(line.rstrip())

new_words = []
for word in existing_words:
    if word not in new_words:
        new_words.append(word)

new_words = sorted(new_words)

with open('wordlist.txt', 'w') as f:
    for word in new_words:
        f.write(word + '\n')