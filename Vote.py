import os.path
import sys
sys.path.insert(0, r'./Training_Methods')

from Training_Methods import stanford
from Training_Methods import ner_romanian
from Training_Methods import ner_english

def beautify(sentence, ner_tags):
    
    to_return = ""
    for word in sentence.split(' '):
        aux = word
        new_word = ""
        for tupl in ner_tags:
            if tupl[0] == word.strip(',').strip(")").strip("("):
                # print(word)
                if tupl[1] == 'PERSON':
                    # print(tupl[0])
                    new_word = "<span style=\"color: red\">" + aux + "</span>"
                    break
                elif tupl[1] == 'GPE':
                    new_word = "<span style=\"color: blue\">" + aux + "</span>"
                    break     
                elif tupl[1] == 'ORGANIZATION':
                    new_word = "<span style=\"color: green\">" + aux + "</span>"
                    break
                else:
                    new_word = "<span style=\"color: pink\">" + aux + "</span>"
                    break 
        if len(new_word) == 0:
            new_word = aux
        to_return += new_word + ' '

    return to_return

#print(beautify("Tudor Arghezi, pseudonimul lui Ion Nae Theodorescu, Academia Romana, nascut la 21 mai 1880, a decedat in 14 iulie 1967 a fost un scriitor rom\u00e2n, cunoscut pentru contribu\u021bia sa la dezvoltarea liricii rom\u00e2ne\u0219ti sub influen\u021ba baudelairianismului. Opera sa poetic\u0103, de o originalitate exemplar\u0103, reprezint\u0103 o alt\u0103 v\u00e2rst\u0103 marcant\u0103 a literaturii rom\u00e2ne. A scris, \u00eentre altele, teatru, proz\u0103 (notabile fiind romanele Cimitirul Buna Vestire \u0219i Ochii Maicii Domnului), pamflete, precum \u0219i literatur\u0103 pentru copii. A fost printre autorii cei mai contesta\u021bi din \u00eentreaga literatur\u0103 rom\u00e2n\u0103", [('Tudor', 'PERSON'), ('Arghezi', 'PERSON'), ('Ion', 'PERSON'), ('Nae', 'PERSON'), ('Theodorescu', 'PERSON'), ('21', 'MISC'), ('mai', 'MISC'), ('1880', 'MISC'), ('Bucure\u0219ti', 'GPE'), ('14', 'MISC'), ('iulie', 'MISC'),('1967', 'MISC'), ('rom\u00e2n', 'MISC'), ('rom\u00e2ne\u0219ti', 'MISC'), ('rom\u00e2ne', 'MISC'), ('Academia', 'ORGANIZATION'), ('Romana', 'ORGANIZATION'),('Cimitirul', 'ORGANIZATION'), ('Buna', 'ORGANIZATION'), ('Vestire', 'ORGANIZATION'), ('Ochii', 'MISC'), ('Maicii', 'MISC'), ('Domnului', 'MISC'), ('rom\u00e2n\u0103', 'MISC')]))

def vote(sentence):

    result = []
    trained = ner_romanian.run(sentence)
    gazetteer = stanford.runGazeteer(sentence)
    spacy = ner_english.run_english(sentence)

    

    for data in trained:
        coefs = [0.42, 0.32, 0.25] #according to each method's F-measure score
        score = 0.42
        coefs.remove(0.42)
        if data in gazetteer and data not in result:
            score += 0.32
            coefs.remove(0.32)
        if data in spacy and data not in result:
            score += 0.25
            coefs.remove(0.25)
        if score > sum(coefs):
            result.append(data)
    
    for data in gazetteer:
        coefs = [0.42, 0.32, 0.25] #according to each method's F-measure score
        score = 0.32
        coefs.remove(0.32)
        # print(data)
        if data in trained and data not in result:
            score += 0.42
            coefs.remove(0.42)
        if data in spacy and data not in result:
            # print(data)
            score += 0.25
            coefs.remove(0.25)
            # print(score)
        if score > sum(coefs):
            # print(data)
            result.append(data)

    for data in spacy:
        coefs = [0.42, 0.32, 0.25] #according to each method's F-measure score
        score = 0.25
        coefs.remove(0.25)
        if data in trained and data not in result:
            score += 0.42
            coefs.remove(0.42)
        if data in gazetteer and data not in result:
            score += 0.32
            coefs.remove(0.32)
        if score > sum(coefs):
            result.append(data)
    

    return beautify(sentence, result)
    #return "<span style=\"color: red\">Tudor Arghezi</span>, pseudonimul lui Ion Nae Theodorescu, Academia Romana, nascut la 21 mai 1880, Bucuresti decedat in 14 iulie 1967 a fost un scriitor român, cunoscut pentru contribuția sa la dezvoltarea liricii românești sub influența baudelairianismului. Opera sa poetică, de o originalitate exemplară, reprezintă o altă vârstă marcantă a literaturii române. A scris, între altele, teatru, proză (notabile fiind romanele Cimitirul Buna Vestire și Ochii Maicii Domnului), pamflete, precum și literatură pentru copii. A fost printre autorii cei mai contestați din întreaga literatură română."

#print(vote("S-a născut la Tulcea pe 10 ianuarie 1906. Străbunicul său Grigore Moisil (1814-1891), a fost paroh la Năsăud și vicar episcopal greco-catolic pentru ținutul Rodnei, unul din întemeietorii primului liceu românesc din Năsăud. Tatăl său, Constantin Moisil (1867-1958), a fost profesor de istorie, arheolog, numismat, directorul Cabinetului Numismatic al Academiei și membru al acestei Academii. Mama sa, Elena (1863-1949) a fost institutoare la Tulcea, apoi directoarea școlii „Maidanul Dulapului”, azi Școala Nr. 74 „Ienăchiță Văcărescu” din București."))

print(vote("Alex prezinta licenta."))