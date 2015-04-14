# put your code here.

file = open('twain.txt')

word_count = {}
poem = []

for line in file:
    line = line.rstrip().split(" ") #each line is in a separate list
    poem += line

for word in poem:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

for word, count in word_count.iteritems():
    print "%s %s" % (word, count)