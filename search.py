import os

#Make this a global var, just makes things easier
finalOutput = {}

#index function
def index(tempList, filename,answer):
    wordListKeyValue = []
    #count the word frequencies
    wordfreq = [tempList.count(p) for p in tempList]
    #add them into a new list
    for item in wordfreq:
        item = (filename, item)
        wordListKeyValue.append(item)
        #return this new dict
    if answer == 'N':
        #return this dict
        return (dict(list(zip(tempList, wordListKeyValue))))
    if answer == 'Y':
        #index using 
        lambdaIndex = lambda wordListKeyValue: (dict(list(zip(tempList, wordListKeyValue))))
        return lambdaIndex(wordListKeyValue)

#Helper function for reducing, this just gets the values easily, then sends them to reduce
def reduceHelper(mapOfWords):
        for entry in mapOfWords:
            for dictionary in entry:
                reduce(dictionary, entry[dictionary])
                
#Reducing the values, and concatinating them to the finalOutput
def reduce(index, value):
    if index not in finalOutput:
        finalOutput[index] = [0]
    finalOutput[index].append(value)
        
#Helper function for getting stop words to make code cleaner
def getStopWords():
    #You will have to change this to your own path
    stopWordsPath = '/Users/katedavis/Desktop/stopwords.txt'
    stopWords = open(stopWordsPath, encoding = "utf8", errors = "ignore")
    result = [line.strip('\n') for line in stopWords.readlines()]
    return result

#Asks the user to print the 
def searchHelper():
    query = []
    searching = True
    while searching == True:
        print("Hello, welcome to Kate's search engine, enter words you would like to search for")
        search = input()
        query.append(search)
        print("Would you like to search for another word? Y/N")
        answer = input()
        if answer == 'N':
            searching = False

    return query

#Search for item in query then print locations and freqeuncies
def search(query):
    print("Here are your results (doc, frequency)")
    for entry in query:
        if entry in finalOutput:
            for i in finalOutput[entry]:
                if i == 0:
                    finalOutput[entry].remove(i)
        print(entry, ": ", sorted(finalOutput[entry]))
        if entry not in finalOutput:
            print("Sorry ", entry, " is not in the dictionary")
            
#Read in files and map the words within
def mapWords(mapOfWords):

        
    print("Complete indexing with lambda function? Y/N")
    answer = input()
    
    #modify path to your own location of the files folder on your machine
    path = '/Users/katedavis/Downloads/Assignment1 txt files'
   
    #get list of stop words
    stopWords = getStopWords()
    
    # use this command in a for loop to access all files in the directory
    for filename in os.listdir(path):
        #Grab .txt file
        if filename.endswith('.txt'):
            #Join path and filename to get access 
            fileToRead = os.path.join(path, filename)
            #Open the file and encode into utf 8
            fh = open(fileToRead, encoding = "utf8", errors = "ignore")
            #clean file names
            filename = filename.replace(".txt", "")
            filename = int(filename)
            #Parse each line
            tempList = []
            for line in fh:
                #Convert each line to lowercase
                line = line.lower()
                #Parse each word and clean them
                for word in line.split():
                    word = word.replace(",", "").replace(".", "").replace('"', "").replace("]", "").replace("[", "").replace("?","").replace(")", "").replace("(", "")
                    #If word not in list append to dict
                    if word not in stopWords:
                        tempList.append(word)
            #Take this tempory list and pass it into index function to return a dict
            mappedWords = index(tempList,filename,answer)
            #Map the words
            mapOfWords.append(mappedWords)
            
    return mapOfWords

#Main function
def main():  
    #Map the documents and words
    mapOfWords = []
    mapOfWords = mapWords(mapOfWords)
    
    #Begin to Reduce       
    reduceHelper(mapOfWords)    
    print(finalOutput)

    #Collect Query and print result to user
    query = searchHelper()
    search(query)
    
#Call Main
if __name__ == '__main__':
    main()
