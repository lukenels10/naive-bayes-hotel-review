import os
import sys
import re
import json
import math
import sys

#Bring in the params from nbmodel.txt
with open("nbmodel.txt") as file:
    params = json.load(file)

V=params['V']

positive_prior=params['positive_prior']
negative_prior=params['negative_prior']
deceptive_prior=params['deceptive_prior']
truthful_prior=params['truthful_prior']

positive_wordcount_dct=params['positive_wordcount_dct']
negative_wordcount_dct=params['negative_wordcount_dct']
deceptive_wordcount_dct=params['deceptive_wordcount_dct']
truthful_wordcount_dct=params['truthful_wordcount_dct']

positive_total_words=params['positive_total_words']
negative_total_words=params['negative_total_words']
deceptive_total_words=params['deceptive_total_words']
truthful_total_words=params['truthful_total_words']

#Read in all txt files from the test folder
test_path=path=sys.argv[1]

# Get the list of all files in directory tree at given path
list_of_files = list()
for (dirpath, dirnames, filenames) in os.walk(test_path):
    list_of_files += [os.path.join(dirpath, file) for file in filenames]
    
#Create list of all the pathnames of text files in the Test directory
all_text_files=list()
for i in list_of_files:
    if i[-4:] == '.txt':
        all_text_files.append(i)

#Create new txt file
text_file = open("nboutput.txt", "w")

def remove(ls): 
    pattern = '[0-9]'
    ls = [re.sub(pattern, '', i) for i in ls] 
    return ls

for file in all_text_files:   #This is where we starg going through the test txt files
    file_path=file    #NOTE: This is the filepath you will add to the txt file
    test_list=''
    file = open(file, 'r')
    lines=file.readlines()
    for line in lines:
        line=line.rstrip()    #Get rid of newline characters
        line = re.sub(r'[^\w\s]','',line)    #Remove punctuation
        line=line.lower()    #Make all words lowercase
        test_list=test_list+line

    ######Let's Make some Prediction!!!####
    test_list=test_list.split(' ')   #Turn the file into a list of words in it
    test_list=remove(test_list)

    #Create Variables needed for each of the 4 classes
    positive_probability=math.log(positive_prior)
    negative_probability=math.log(negative_prior)
    deceptive_probability=math.log(deceptive_prior)
    truthful_probability=math.log(truthful_prior)

    for word in test_list:
        if word not in V:    #Skip words that are not in the vocabulary
            continue

        #Calculate the likelihood for each word and add the likelihood to that classes probability total
        #Positive
        positive_likelihood_numerator=positive_wordcount_dct.get(word,0)+1
        positive_likelihood_denominator=positive_total_words+len(V)
        positive_likelihood = positive_likelihood_numerator / positive_likelihood_denominator
        positive_probability = positive_probability + math.log(positive_likelihood)

        #Negative
        negative_likelihood_numerator=negative_wordcount_dct.get(word,0)+1
        negative_likelihood_denominator=negative_total_words+len(V)
        negative_likelihood = negative_likelihood_numerator / negative_likelihood_denominator
        negative_probability = negative_probability + math.log(negative_likelihood)

        #Deceptive
        deceptive_likelihood_numerator=deceptive_wordcount_dct.get(word,0)+1
        deceptive_likelihood_denominator=deceptive_total_words+len(V)
        deceptive_likelihood = deceptive_likelihood_numerator / deceptive_likelihood_denominator
        deceptive_probability = deceptive_probability + math.log(deceptive_likelihood)

        #Truthful
        truthful_likelihood_numerator=truthful_wordcount_dct.get(word,0)+1
        truthful_likelihood_denominator=truthful_total_words+len(V)
        truthful_likelihood = truthful_likelihood_numerator / truthful_likelihood_denominator
        truthful_probability = truthful_probability + math.log(truthful_likelihood)

    #Determine the Labels!!!!
    if positive_probability >= negative_probability:
        label_b = 'positive'
    else:
        label_b = 'negative'

    if truthful_probability >= deceptive_probability:
        label_a = 'truthful'
    else:
        label_a = 'deceptive'

    text_file.write(label_a+' '+label_b+' '+file_path+'\n')

text_file.close()