def word_count(sentence):
    sentence = sentence.split(" ")
   #an array for words that appear once in a sentence
    appear_once= []
    for items in sentence:
        if items not in appear_once:
            appear_once.append(items)
    for chr_string in appear_once:
      print(chr_string+': '+str(sentence.count(chr_string)))
word_count("olly olly in come free")