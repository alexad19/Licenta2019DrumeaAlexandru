def run_english(sent):
        import spacy
        import xx_ent_wiki_sm
        nlp = xx_ent_wiki_sm.load()
        
        sentence = nlp (sent)

        l =  [(X.text, X.label_) for X in sentence.ents]
        # print(l)
        to_return = []
        
        # print(l)
        for item in l: 
                if len(item[0].split(' ')) == 1:
                        if item[1] == 'PER':
                                new_tuple = (item[0], 'PERSON')
                        elif item[1] == 'ORG':
                                new_tuple = (item[0], 'ORGANIZATION')
                        elif item[1] == 'GPE':
                                new_tuple = (item[0], 'GPE')
                        else:
                                new_tuple = (item[0], 'MISC')
                        to_return.append(new_tuple)
                else:
                        for tab in item[0].split(' '):
                                if item[1] == 'PER':
                                        new_tuple = (tab, 'PERSON')
                                        to_return.append(new_tuple)
                                elif item[1] == 'ORG':
                                        new_tuple = (tab, 'ORGANIZATION')
                                        to_return.append(new_tuple)
                                elif item[1] == 'GPE':
                                        new_tuple = (tab, 'GPE')
                                        to_return.append(new_tuple)
                                else:
                                        new_tuple = (tab, 'MISC')
                                        to_return.append(new_tuple)

        return to_return

#print(run_english("Tudor Arghezi, pseudonimul lui Ion Nae Theodorescu, Academia Romana, nascut la 21 mai 1880, Bucuresti decedat in 14 iulie 1967 a fost un scriitor român, cunoscut pentru contribuția sa la dezvoltarea liricii românești sub influența baudelairianismului. Opera sa poetică, de o originalitate exemplară, reprezintă o altă vârstă marcantă a literaturii române. A scris, între altele, teatru, proză (notabile fiind romanele Cimitirul Buna Vestire și Ochii Maicii Domnului), pamflete, precum și literatură pentru copii. A fost printre autorii cei mai contestați din întreaga literatură română."))
