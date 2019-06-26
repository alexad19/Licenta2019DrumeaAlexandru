import nltk
from nltk.tag.stanford import StanfordNERTagger

# Optional
def run(sentence):
    import os
    java_path = "C:/Program Files/Java/jdk-12.0.1/bin"
    os.environ['JAVAHOME'] = java_path

    jar = 'D:/Anul_3/Lic/stanford/stanford-ner.jar'
    model = 'D:/Anul_3/Lic/stanford/train/dummy-ner-model-romanian.ser.gz'

    ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

    words = nltk.word_tokenize(sentence)
    raw_data = ner_tagger.tag(words)
    to_return = []
    for tuplu in raw_data:
        if tuplu[1] != 'O':
            if tuplu[1] == 'PERSON' or tuplu[1] == 'GPE' or tuplu[1] == 'ORGANIZATION':
                to_return.append(tuplu)
            else:
                new_tuplu = (tuplu[0], 'MISC')
                to_return.append(new_tuplu)
    return to_return
            


sentence = u"Tudor Arghezi, pseudonimul lui Ion Nae Theodorescu, Academia Romana, nascut la 21 mai 1880, a decedat in 14 iulie 1967 a fost un scriitor roman, cunoscut pentru contributia sa la dezvoltarea liricii romanesti sub influenta baudelairianismului."

# print (run(sentence))