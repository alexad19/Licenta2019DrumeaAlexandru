import sys
import os.path
import json

sys.path.insert(0, r'./Training_Methods')

from Training_Methods import stanford
from Training_Methods import ner_romanian
from Training_Methods import ner_english

def ComputeParams(method):
    all_words = 0
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0
    f = open("./Resources/test_data.txt", 'r', encoding='utf8')
    dictionary = json.load(f)
    
    sentences = dictionary['sentence']
    
    for sentence in sentences:
        # print(sentence['raw'].split(' '))
        all_words += len (sentence['raw'].split(' '))
        # print(all_words)
        break
    all_correct_tagged = 0
    for sentence in sentences:
        all_correct_tagged +=  len(sentence['tagged'])
        # print(sentence['tagged'])
    
    if method.lower() == 'gazetteer':

        for sentence in sentences:
            tagged_sentence = stanford.runGazeteer(sentence['raw'])
            for item in tagged_sentence:
                if str(item) in sentence['tagged']:
                    true_positives += 1
                elif str(item[0]) in sentence['tagged']:
                    false_negatives += 1
                else:
                    false_positives += 1
                # false_negatives += (all_correct_tagged - true_positives)
                true_negatives = all_words - all_correct_tagged 
    elif method.lower() == 'trained':
 
        for sentence in sentences:
            tagged_sentence = ner_romanian.run(sentence['raw'])
            for item in tagged_sentence:
                if str(item) in sentence['tagged']:
                    true_positives += 1
                elif str(item[0]) in sentence['tagged']:
                    false_negatives += 1
                else:
                    false_positives += 1
                # false_negatives += (all_correct_tagged - true_positives)
                true_negatives = all_words - all_correct_tagged 
    elif method.lower() == 'blind':

        for sentence in sentences:
            tagged_sentence =ner_english.run_english(sentence['raw'])
            for item in tagged_sentence:
                if str(item) in sentence['tagged']:
                    true_positives += 1
                elif str(item[0]) in sentence['tagged']:
                    false_negatives += 1
                else:
                    false_positives += 1
                true_negatives = all_words - all_correct_tagged 
                # print(all_words, all_correct_tagged)
    
    return true_positives, false_positives, false_negatives, true_negatives

def ComputePrecision(method):
    
    #true_negatives = those who are not named entities and have not been classified as such
    #true_positives = those who are named entities and have correctly been classified
    #false_positives = those who are not named entities, but have been classified as such 
    #false_negatives = those who are named entities, but have not been classified as such or those who are named entities, but have been wrongly classified
    true_positives, false_positives, false_negatives, true_negatives = ComputeParams(method)
  
    return true_positives/ (true_positives + false_positives)  

def ComputeRecall(method):
    true_positives, false_positives, false_negatives, true_negatives  = ComputeParams(method)
    return true_positives/ (true_positives + false_negatives)  

def ComputeFMeasure(method):
    recall = ComputeRecall(method)
    precision = ComputePrecision(method)
    return 2*(precision * recall) / (precision + recall)

# print("The recall of the trained Stanford CRFClassifier is:", ComputeRecall("trained"))
# print("The recall of the Gazetteer Classifier is:", ComputeRecall("gazetteer"))
# print("The recall of the SpaCy multi-language model Classifier is:", ComputeRecall("blind"))

# print("The F-measure result of the trained Stanford CRFClassifier is:", ComputeFMeasure("trained"))
# print("The F-measure result of the Gazetteer Classifier is:", ComputeFMeasure("gazetteer"))
# print("The F-measure result of the SpaCy multi-language model Classifier is:", ComputeFMeasure("blind"))


