from fungi.models import Glossary
from django.urls import reverse
import string


def InsertLinks(Text):
    glossary = Glossary.objects.all()
    terms, texts, termstarts, termends, textstarts,  textends, allvars, TextList = ([] for i in range(8))
    LinksInserted ={}
    glossarytermfound = False



    #loop through Glossary, if glossary term in text from DB get start/end indexes of term in text
    for glossaryterm in glossary:
        lcstr = glossaryterm.Term.casefold()
        try:
            if Text.find(glossaryterm.Term) > -1:
                glossarytermfound = True
                index1 = Text.index(glossaryterm.Term)
                index2 = index1+(len(glossaryterm.Term))
                termstarts.append(index1)
                termends.append(index2-1)
            elif Text.find(lcstr) > -1:
                glossarytermfound = True
                index1 = Text.index(lcstr)
                index2 = index1+(len(lcstr))
                termstarts.append(index1)
                termends.append(index2-1)
        except ValueError:
            glossarytermfound = False
    
    if glossarytermfound:

        terms = termstarts+termends
        terms.sort()

        textfirst = False
        termfirst = False

        if terms[0] == 0:
            termfirst = True
        else:
             textfirst = True

        if termfirst:
            termcount = int(len(terms)/2)
            count = 1
            for x in range(termcount):
                texts.append(terms[count]+1)
                count += 1
                if x == termcount-1:
                    texts.append(len(Text)-1)
                else:    
                    texts.append(terms[count]-1)
                    count += 1


        if textfirst:
            count = 0
            for y in range(int(len(terms)/2)):
                if y == 0:
                    if terms[count] == 0:
                        texts.append(terms[count]-terms[count])
                        texts.append(terms[count-1])
                        count += 1
                    else:
                        texts.append(terms[0]-terms[0])
                        texts.append(terms[0]-1)
                        count += 1
                else:
                    texts.append(terms[count]+1)
                    count += 1
                    texts.append(terms[count]-1)
                    count += 1

        if len(Text) > terms[-1]:
            texts.append(terms[-1]+1)
            texts.append(len(Text))



        allvars = terms+texts
        allvars.sort()

        if textfirst:
            count_a = 0
            count_b = 1
            count_c = 0

            for x in range(int(len(allvars)/4)+1): 
                try:
                    LinksInserted['item'+str(count_c)]= Text[texts[count_a]:texts[count_b]+1]
                    TextList.append(Text[texts[count_a]:texts[count_b]+1])
                except IndexError:
                    print('Reached end of texts')  
                try:
                    termtext = Text[terms[count_a]:terms[count_b]+1]
                    LinksInserted['link'+str(count_c)] = [reverse('glossary_entry', args=[termtext]),termtext]
                except IndexError:
                    print('Reached end of terms')                            

                count_a += 2
                count_b += 2
                count_c += 1
        else:
            count_a = 0
            count_b = 1
            count_c = 0
            for x in range(int(len(allvars)/4)+1): 
                try:
                    termtext = Text[terms[count_a]:terms[count_b]+1]
                    LinksInserted['link'+str(count_c)] = [reverse('glossary_entry', args=[termtext]),termtext]
                    LinksInserted['item'+str(count_c)]= Text[texts[count_a]:texts[count_b]+1]
                    print('Text:', Text[texts[count_a]:texts[count_b]+1] )
                    print('Text:', Text[texts[count_a]-1:texts[count_b]+1] )
                except IndexError:
                    print('Reached end of texts')                            

                count_a += 2
                count_b += 2
                count_c += 1

    else:
        LinksInserted = Text
    
    return [LinksInserted, glossarytermfound]
