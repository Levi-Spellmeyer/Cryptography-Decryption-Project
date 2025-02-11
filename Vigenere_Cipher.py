# This function calculates the idex of coincidence which in turn is used to estimate the period or length of the key
def IndexCoincidence(ciphertext, arrOccurences):
    length=len(ciphertext)
    firstHalfOfIC = (1/(length * (length-1)))
    
    #summation of n sub i times (n sub i - 1) from 0 to 26
    secondHalfOfIC = 0
    for i in range(0,26):
        temp = arrOccurences[i] * (arrOccurences[i]-1)
        secondHalfOfIC += temp

    #multiply the first and second half of the equation together to get to IC which is returned
    IC = firstHalfOfIC * secondHalfOfIC
    return IC



# This funtion creates and returns a list of the number of times each letter shows up in the ciphertext
def Occurences(ciphertext):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    arrOccurences = [0] * 26 # this list will hold the occurences of every letter in the alphabet in relation to the cipher text

    for letter in alphabet: # For loop to count occurence of each leter
        count = 0
        for char in ciphertext:    
            if letter == char:
                count += 1
        arrOccurences[alphabet.index(letter)] = count #adds the occurence to a list
    return arrOccurences


# Function that accepts each seperated alphabet of the ciphertext and decrypts it using the caeser cipher code
# I already created
def CaeserCipher(ciphertext):
      # This list is used to reference each letter in the alphabet in terms of the numbered key or index
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    CharacterFrequencies = [.083,.015,.027,.041,.126,.020,.019,.061,.067,.002,.009,.042,.025,.068,.077,.017,.0009,.057,.061,.094,.029,.011,.023,.002,.020,.0006]
    arrOccurences = [0] * 26 
    
    for letter in alphabet:
        count = 0
        for char in ciphertext:    
            if letter == char:
                count += 1
        arrOccurences[alphabet.index(letter)] = count

    cipherAlphabet = [[],[]]
    for i in range(0,26):
        if arrOccurences[i] != 0:
            cipherAlphabet[0].append(alphabet[i])        
            cipherAlphabet[1].append(arrOccurences[i])  
            cipherTotal = sum(cipherAlphabet[1])
    cipherLength = len(cipherAlphabet[0])


    arrFrequencies = [0] * cipherLength
    for i in range(0,cipherLength):
        arrFrequencies[i] = round(cipherAlphabet[1][i] / cipherTotal, 4) 


    correlationOfFrequency = [[],[]]
    for i in range(0,26):
        correlation=0
        for j in range (0,len(cipherAlphabet[0])): 
            Letter = cipherAlphabet[0][j]
            letterIndex = alphabet.index(Letter)

            correlation += (arrFrequencies[j] * CharacterFrequencies[(letterIndex-i)%26]) 
        correlationOfFrequency[0].append(alphabet[i])  
        correlationOfFrequency[1].append(correlation) 
    max=-1
    index=-1
    for i in range(26):
        if correlationOfFrequency[1][i] > max:
            max = correlationOfFrequency[1][i]
            index=i
    return correlationOfFrequency[0][index]
    
# This function take in the individual alphabets and their corresponding key to decypher them (returned by Caeser function)
# to decryt/ shift each letter back to its plaintext form
def plaintext(ciphertext, key):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = alphabet.index(key)
    plaintext=""
    for letter in ciphertext:
        index = alphabet.index(letter)
        decryptedIndex = (index - key) % 26
        plaintext += alphabet[decryptedIndex]
    return plaintext



def main():
    ciphertext = input("Enter ciphertext: ")
    ciphertext = ciphertext.replace(" ", "").upper()
    ciphertextLen = len(ciphertext)

    # Passes the ciphertext and returns a list of occurences
    arrOccurences=Occurences(ciphertext)
   
    IC = IndexCoincidence(ciphertext, arrOccurences)

    # After calculating the value of the IC the user is prompted to use the IC to make a guess using the IC as to how long the period is
    print("\n\n\nThe index of coincidence for the cipher text provide is: ", IC)
    potentialKey = int(input("please enter the potential key that the IC correlates to: "))

    # This seperates the inputed ciphertext into period number of equal length alphabets 
    period = [[] for _ in range(potentialKey)]
    for i in range(0,ciphertextLen):
        period[i % potentialKey].append(ciphertext[i])
    
    # This is a list that will associate the key found using Caeser cipher with each of the seperated alphabets
    alphabetKeys= [0] * potentialKey
    for i in range(0,potentialKey):
        text = ''.join(period[i])
        alphabetKeys[i]=CaeserCipher(text.upper())

    # This for loop joins each alphabet into a single string and passes it to the Caeser cipher to be decrypted and output to the user
    for i in range(potentialKey):
        text2 = ''.join(period[i])
        text2 = plaintext(text2, alphabetKeys[i])
        print(f"\nThe key to deciphering alphabet {i+1} using ceaser cipher is {alphabetKeys[i]}")
        print(f"The potential deciphered alphebet {i+1} is {text2}")

main()