
def count(sequence, item):
  sum = 0 
  for i in sequence:
    if i == item:
      sum +=1
  return sum

print count("Hi jack, i'm you secretary", "y")

#This program do the function of count the word in a sentence
def count_word(sentence,word):
  sum = 0 
  sentence = sentence.lower()
  word = word.lower()
  sen_list = sentence.split()
  for i in sen_list:
    if i == word:
      sum += 1
  return sum

a = "I'm Jack Lee, and I will make a great company in the future."
b = 'Jack'

print(count_word(a,b))
