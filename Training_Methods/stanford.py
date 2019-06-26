import re
import stanfordnlp

nlp = stanfordnlp.Pipeline(lang="ro", treebank="ro_rrt")

# for i in doc.sentences:
#     print(i.words)

#extract parts of speech
def extract_pos(doc):
    result = []
    for sent in doc.sentences:
        for wrd in sent.words:
            result.append((wrd.text, wrd.upos))
    #return a dataframe of pos and text
    return result

#print (extract_pos(nlp("Tudor Arghezi, pseudonimul lui Ion Nae Theodorescu, Academia Romana, nascut la 21 mai 1880, Bucuresti decedat in 14 iulie 1967 a fost un scriitor român, cunoscut pentru contribuția sa la dezvoltarea liricii românești sub influența baudelairianismului. Opera sa poetică, de o originalitate exemplară, reprezintă o altă vârstă marcantă a literaturii române. A scris, între altele, teatru, proză (notabile fiind romanele Cimitirul Buna Vestire și Ochii Maicii Domnului), pamflete, precum și literatură pentru copii. A fost printre autorii cei mai contestați din întreaga literatură română.")))
def runGazeteer(sentence):
    f = open(r"D:\Anul_3\Lic\Resources\PERSON.txt", "r", encoding="utf8").read()
    g = open(r"D:\Anul_3\Lic\Resources\GPE.txt", "r", encoding="utf8").read()
    h = open(r"D:\Anul_3\Lic\Resources\MISC.txt", "r", encoding="utf8").read()
    j = open(r"D:\Anul_3\Lic\Resources\ORGANIZATION.txt", "r", encoding="utf8").read()
    # #extract pos
    # print(extract_pos(doc))
    person = []
    gpe = []
    misc = []
    organization = []
    for line in f.split('\n'):
        person.append(line)
    for line in g.split('\n'):
        gpe.append(line)
    for line in h.split('\n'):
        misc.append(line)
    for line in j.split('\n'):
       organization.append(line) 
    sent = nlp(sentence)
    pos_tagged = extract_pos(sent)
    ner_list = []
    # print ("Arghezi" in person)
    
    for word in pos_tagged:
        if word[1] == 'NOUN' or word[1] == 'PROPN':
            if word[0] in person:
                ner_list.append((word[0], "PERSON"))
            elif word[0] in gpe:
                ner_list.append((word[0], "GPE"))
            elif word[0] in organization:
                ner_list.append((word[0], "ORGANIZATION"))
            elif word[0] in misc:
                ner_list.append((word[0], "MISC"))
            
    return ner_list


doc = "Tudor Arghezi, pseudonimul lui Ion Nae Theodorescu, Academia Romana, nascut la 21 mai 1880, Bucuresti decedat in 14 iulie 1967 a fost un scriitor român, cunoscut pentru contribuția sa la dezvoltarea liricii românești sub influența baudelairianismului. Opera sa poetică, de o originalitate exemplară, reprezintă o altă vârstă marcantă a literaturii române. A scris, între altele, teatru, proză (notabile fiind romanele Cimitirul Buna Vestire și Ochii Maicii Domnului), pamflete, precum și literatură pentru copii. A fost printre autorii cei mai contestați din întreaga literatură română."
#print(runGazeteer(doc))