
def hashList(list):

        for names in list:
            hashValue = hash(names)
            print(names, hashValue)
        
def main():
    
    familyNamesList = [ "Matt", "Megan", "Colby", "Mary", "Todd", "Jane", "Kenzie", "Evan"]
    hashList(familyNamesList)
    
main()

