l1= ["anjali","priyanshi","om","ashvi","ram"]

long_words = filter(lambda word: len(word)>= 4,l1)
print(list(long_words))
