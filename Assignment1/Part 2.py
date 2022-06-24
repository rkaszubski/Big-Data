#Part 2

#a
def part_a(filename):
    f = open(filename)
    lines = f.read().split(" ")
    words = {}
    f.close()
    for word in lines:
        if word in words.keys():
            words[word] = words[word] + 1
        else:
            words[word] = 1
    print("Key Count : " + str(len(words.keys())))
    return words

print("Part A - Original Dictionary")
originaldict = part_a(r'C:\Users\rober\Desktop\Grad\CSC555\Assignment1\HadoopBlurb.txt')
print()

#b
import random
from types import new_class

def part_b(filename):
    f = open(filename)
    lines = f.read().split(" ")
    words = [{},{},{}]
    for word in lines:
        dic = random.randint(0,2)
        if word in words[dic].keys():
            words[dic][word] = words[dic][word] + 1
        else:
            words[dic][word] = 1
    print("Total words: " + str(len(lines)))
    print("Key Count in Dict 0 : " + str(len(words[0].keys())))
    print("Key Count in Dict 1 : " + str(len(words[1].keys())))
    print("Key Count in Dict 2 : " + str(len(words[2].keys())))
    return words

print("Part B - Three Dictionaries")
randomdicts = part_b(r'C:\Users\rober\Desktop\Grad\CSC555\Assignment1\HadoopBlurb.txt')
print()

#c
newdict = {}

for dictid in range(0,3):
    dictionary = randomdicts[dictid]
    for word in dictionary.keys():
        if word in newdict.keys():
            newdict[word] = newdict[word] + dictionary[word]
        else:
            newdict[word] = dictionary[word]

print("Part C - Merged Dictionary")
print("Key Count : " + str(len(newdict.keys())))
print("Is the merged dictionary equal to the original? : " + str(newdict == originaldict))
print()

#d
def part_d(filename):
    f = open(filename)
    lines = f.read().split(" ")
    words = [{},{},{}]
    for word in lines:
        dic = hash(word)%3
        if word in words[dic].keys():
            words[dic][word] = words[dic][word] + 1
        else:
            words[dic][word] = 1
    print("Key Count in Dict 0 : " + str(len(words[0].keys())))
    print("Key Count in Dict 1 : " + str(len(words[1].keys())))
    print("Key Count in Dict 2 : " + str(len(words[2].keys())))
    return words

print("Part D - Deterministic Dictionaries")
determinedicts = part_d(r'C:\Users\rober\Desktop\Grad\CSC555\Assignment1\HadoopBlurb.txt')
print()

#e
newdict2 = {}

for dictid in range(0,3):
    dictionary = determinedicts[dictid]
    for word in dictionary.keys():
        if word in newdict2.keys():
            newdict2[word] = newdict2[word] + dictionary[word]
        else:
            newdict2[word] = dictionary[word]

print("Part E - Merged Dictionary 2")
print("Key Count : " + str(len(newdict2.keys())))
print("Is the merged dictionary equal to the original? : " + str(newdict2 == originaldict))
print()
