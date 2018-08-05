import hashlib

def main():
    index = 0
    familyNamesList = [ "Matt", "Megan", "Colby", "Mary", "Todd", "Jane", "Kenzie", "Evan" ]
    hashValues = list(range(len(familyNamesList)))
    
    for name in familyNamesList:
        hashValues[index] = hashlib.sha256(name.encode("utf-8")).hexdigest()
        print(name, " - Hash Value: ", hashValues[index])
        index += 1
main()