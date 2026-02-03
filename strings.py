sentence = "this is a sentence and this is simple"

words = sentence.split()

print(words)

word_counts = {}

for myWord in words:
    word_counts[myWord] = word_counts.get(myWord, 0) + 1

print(word_counts)
