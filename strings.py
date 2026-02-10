sentence = "this is a sentence and this is simple"

words = sentence.split()

print(words)

word_counts = {} #this is a dictionary

# for myWord in words:
#     word_counts[myWord] = word_counts.get(myWord, 0) + 1 #returns 0 if myWord does not exist

for myWord in words:
    if myWord in word_counts:
        word_counts[myWord] +=1;
    else:
        word_counts[myWord] = 1;

print(word_counts)
