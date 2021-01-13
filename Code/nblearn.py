import os
import sys
import re
import json
import sys


path=sys.argv[1]

directory=os.listdir(path)   #Ex. ['.DS_Store', 'LICENSE', 'positive_polarity', 'README.md', 'README.txt', 'negative_polarity']

#Class types
positive='positive'
negative='negative'

deceptive='deceptive'
truthful='truthful'



#Positive and Negative Folders    ex. 'positive_path'
    #variabl for positive is positive_folder
    #variable for negative is negative_folder
for i in directory:
    if positive in i:
        positive_folder=i
    if negative in i:
        negative_folder=i

#Positive and Negative Paths    ex. '/Users/lukenelson/Desktop/CSCI_544/Homework/Assignment_3/My_Codes/Testing/op_spam_training_data/positive_polarity'
positive_path=os.path.join(path, positive_folder)
negative_path=os.path.join(path, negative_folder)

positive_directory=os.listdir(positive_path)
negative_directory=os.listdir(negative_path)

#Deceptive and Truthful folders
for i in positive_directory:
    if deceptive in i:
        deceptive_folder_1=i
    if truthful in i:
        truthful_folder_1=i

for i in negative_directory:
    if deceptive in i:
        deceptive_folder_2=i
    if truthful in i:
        truthful_folder_2=i
        
#Deceptive and Truthful Paths and Directories
positive_deceptive_path=os.path.join(positive_path, deceptive_folder_1)
negative_deceptive_path=os.path.join(negative_path, deceptive_folder_2)

positive_truthful_path=os.path.join(positive_path, truthful_folder_1)
negative_truthful_path=os.path.join(negative_path, truthful_folder_2)

#Final 4 Directories    ex. ['fold2', 'fold4', 'fold3']
positive_deceptive_directory=os.listdir(positive_deceptive_path)    
positive_truthful_directory=os.listdir(positive_truthful_path)

negative_deceptive_directory=os.listdir(negative_deceptive_path)
negative_truthful_directory=os.listdir(negative_truthful_path)

#Remove '.DS_Store' from directories
try:
    positive_deceptive_directory.remove('.DS_Store')
    positive_truthful_directory.remove('.DS_Store')
    negative_deceptive_directory.remove('.DS_Store')
    negative_truthful_directory.remove('.DS_Store')
except:
    pass

#Open every folder in each of the 4 paths and concatenate all of the txt files into a list of words

def remove(ls): 
    pattern = '[0-9]'
    ls = [re.sub(pattern, '', i) for i in ls] 
    return ls

#Total # of Documents
total_documents=0

#Total Documents for Each of the 4 classes
positive_documents=0
negative_documents=0
deceptive_documents=0
truthful_documents=0

###POSITIVE DECEPTIVE###
positive_deceptive_reviews = ''

# Get the list of all files in directory tree at given path
positive_deceptive_files = list()
for (dirpath, dirnames, filenames) in os.walk(positive_deceptive_path):
    positive_deceptive_files += [os.path.join(dirpath, file) for file in filenames]
    
#Create list of all the pathnames of text files in the directory
positive_deceptive_text_files=list()
for i in positive_deceptive_files:
    if i[-4:] == '.txt':
        positive_deceptive_text_files.append(i)
        
for file in positive_deceptive_text_files:
    total_documents = total_documents + 1
    positive_documents = positive_documents + 1
    deceptive_documents = deceptive_documents + 1
    file = open(file, 'r')
    lines=file.readlines()
    for line in lines:
        line=line.rstrip()    #Get rid of newline characters
        line = re.sub(r'[^\w\s]','',line)    #Remove punctuation
        line=line.lower()    #Make all words lowercase
        positive_deceptive_reviews=positive_deceptive_reviews+line

positive_deceptive_reviews=positive_deceptive_reviews.split(' ')    #positive_deceptive_reviews is now a list with every single word
positive_deceptive_reviews=remove(positive_deceptive_reviews)
try:
    positive_deceptive_reviews.remove('')
except:
    pass


###POSITIVE TRUTHFUL###
positive_truthful_reviews = ''

# Get the list of all files in directory tree at given path
positive_truthful_files = list()
for (dirpath, dirnames, filenames) in os.walk(positive_truthful_path):
    positive_truthful_files += [os.path.join(dirpath, file) for file in filenames]
    
#Create list of all the pathnames of text files in the directory
positive_truthful_text_files=list()
for i in positive_truthful_files:
    if i[-4:] == '.txt':
        positive_truthful_text_files.append(i)
        
for file in positive_truthful_text_files:
    total_documents = total_documents + 1
    positive_documents = positive_documents + 1
    truthful_documents = truthful_documents + 1
    file = open(file, 'r')
    lines=file.readlines()
    for line in lines:
        line=line.rstrip()    #Get rid of newline characters
        line = re.sub(r'[^\w\s]','',line)    #Remove punctuation
        line=line.lower()    #Make all words lowercase
        positive_truthful_reviews=positive_truthful_reviews+line

positive_truthful_reviews=positive_truthful_reviews.split(' ')    #positive_truthful_reviews is now a list with every single word
positive_truthful_reviews=remove(positive_truthful_reviews)
try:
    positive_truthful_reviews.remove('')
except:
    pass

###NEGATIVE DECEPTIVE###
negative_deceptive_reviews = ''

# Get the list of all files in directory tree at given path
negative_deceptive_files = list()
for (dirpath, dirnames, filenames) in os.walk(negative_deceptive_path):
    negative_deceptive_files += [os.path.join(dirpath, file) for file in filenames]
    
#Create list of all the pathnames of text files in the directory
negative_deceptive_text_files=list()
for i in negative_deceptive_files:
    if i[-4:] == '.txt':
        negative_deceptive_text_files.append(i)
        
for file in negative_deceptive_text_files:
    total_documents = total_documents + 1
    negative_documents = negative_documents + 1
    deceptive_documents = deceptive_documents + 1
    file = open(file, 'r')
    lines=file.readlines()
    for line in lines:
        line=line.rstrip()    #Get rid of newline characters
        line = re.sub(r'[^\w\s]','',line)    #Remove punctuation
        line=line.lower()    #Make all words lowercase
        negative_deceptive_reviews=negative_deceptive_reviews+line

negative_deceptive_reviews=negative_deceptive_reviews.split(' ')    #negative_deceptive_reviews is now a list with every single word
negative_deceptive_reviews=remove(negative_deceptive_reviews)
try:
    negative_deceptive_reviews.remove('')
except:
    pass


###NEGATIVE TRUTHFUL###
negative_truthful_reviews = ''

# Get the list of all files in directory tree at given path
negative_truthful_files = list()
for (dirpath, dirnames, filenames) in os.walk(negative_truthful_path):
    negative_truthful_files += [os.path.join(dirpath, file) for file in filenames]
    
#Create list of all the pathnames of text files in the directory
negative_truthful_text_files=list()
for i in negative_truthful_files:
    if i[-4:] == '.txt':
        negative_truthful_text_files.append(i)
        
for file in negative_truthful_text_files:
    total_documents = total_documents + 1
    negative_documents = negative_documents + 1
    truthful_documents = truthful_documents + 1
    file = open(file, 'r')
    lines=file.readlines()
    for line in lines:
        line=line.rstrip()    #Get rid of newline characters
        line = re.sub(r'[^\w\s]','',line)    #Remove punctuation
        line=line.lower()    #Make all words lowercase
        negative_truthful_reviews=negative_truthful_reviews+line

negative_truthful_reviews=negative_truthful_reviews.split(' ')    #negative_truthful_reviews is now a list with every single word
negative_truthful_reviews=remove(negative_truthful_reviews)
try:
    negative_truthful_reviews.remove('')
except:
    pass

#These are lists of the words in each class
positive_reviews = positive_deceptive_reviews + positive_truthful_reviews
negative_reviews = negative_deceptive_reviews + negative_truthful_reviews

deceptive_reviews = positive_deceptive_reviews + negative_deceptive_reviews
truthful_reviews = positive_truthful_reviews + negative_truthful_reviews

#The Vocabulary
V = positive_deceptive_reviews + positive_truthful_reviews + negative_deceptive_reviews + negative_truthful_reviews
V=list(set(V))
try:
    V.remove('')
except:
    pass


#Calculate P(c)
positive_prior = positive_documents / total_documents
negative_prior = negative_documents / total_documents
deceptive_prior = deceptive_documents / total_documents
truthful_prior = truthful_documents / total_documents

#Calculate P(d|c)

#Dictionary of word counts for each class
###POSITIVE###
positive_wordcount_dct=dict()
for word in positive_reviews:
    positive_wordcount_dct[word]=positive_wordcount_dct.get(word,0) + 1

###NEGATIVE###
negative_wordcount_dct=dict()
for word in negative_reviews:
    negative_wordcount_dct[word]=negative_wordcount_dct.get(word,0) + 1
    
###DECEPTIVE###
deceptive_wordcount_dct=dict()
for word in deceptive_reviews:
    deceptive_wordcount_dct[word]=deceptive_wordcount_dct.get(word,0) + 1
    
###TRUTHFUL###
truthful_wordcount_dct=dict()
for word in truthful_reviews:
    truthful_wordcount_dct[word]=truthful_wordcount_dct.get(word,0) + 1
    

#The count of the number of words in each class
positive_total_words=len(positive_reviews)
negative_total_words=len(negative_reviews)
deceptive_total_words=len(deceptive_reviews)
truthful_total_words=len(truthful_reviews)

#Place all of the parameters in a dictionary to read into your text file
params=dict()

params['V']=V

params['positive_prior']=positive_prior
params['negative_prior']=negative_prior
params['deceptive_prior']=deceptive_prior
params['truthful_prior']=truthful_prior

params['positive_wordcount_dct']=positive_wordcount_dct
params['negative_wordcount_dct']=negative_wordcount_dct
params['deceptive_wordcount_dct']=deceptive_wordcount_dct
params['truthful_wordcount_dct']=truthful_wordcount_dct

params['positive_total_words']=positive_total_words
params['negative_total_words']=negative_total_words
params['deceptive_total_words']=deceptive_total_words
params['truthful_total_words']=truthful_total_words

#Write the params dictionary to a text file
with open('nbmodel.txt', 'w') as file:
     file.write(json.dumps(params)) # use `json.loads` to do the reverse

file.close()