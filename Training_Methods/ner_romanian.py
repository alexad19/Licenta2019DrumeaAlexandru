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
            


sentence = u"S-a născut la Tulcea pe 10 ianuarie 1906. Străbunicul său Grigore Moisil (1814-1891), a fost paroh la Năsăud și vicar episcopal greco-catolic pentru ținutul Rodnei, unul din întemeietorii primului liceu românesc din Năsăud. Tatăl său, Constantin Moisil (1867-1958), a fost profesor de istorie, arheolog, numismat, directorul Cabinetului Numismatic al Academiei și membru al acestei Academii. Mama sa, Elena (1863-1949) a fost institutoare la Tulcea, apoi directoarea școlii „Maidanul Dulapului”, azi Școala Nr. 74 „Ienăchiță Văcărescu” din București."

print (run("Alex prezinta licenta."))