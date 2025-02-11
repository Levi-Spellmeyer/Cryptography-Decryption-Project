# This funtion using the ciphertext and key passed as arguments to decrypt the ciphertext
def plaintext(ciphertext, key):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext=""
    for letter in ciphertext:
        index = alphabet.index(letter)
        decryptedIndex = (index - key) % 26
        plaintext += alphabet[decryptedIndex]
    return plaintext


def main():
    # This list is used to reference each letter in the alphabet in terms of the numbered key or index
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # THese frequencies were taken from the powerpoint provide in class
    CharacterFrequencies = [.083,.015,.027,.041,.126,.020,.019,.061,.067,.002,.009,.042,.025,.068,.077,.017,.0009,.057,.061,.094,.029,.011,.023,.002,.020,.0006]

    ciphertextInput=input("Enter the Ciphertext: ")              # Takes in ciphertext from user
    ciphertext = ciphertextInput.upper()                         # Sets every letter to upper case
    ciphertext = ciphertext.replace(" ","")


    arrOccurences = [0] * 26 # this list will hold the occurences of every letter in the alphabet in relation to the cipher text
    
# I use this for loop to count the occurence of each letter in the ciphertext and store it in a list
    for letter in alphabet:
        count = 0
        for char in ciphertext:    
            if letter == char:
                count += 1
        arrOccurences[alphabet.index(letter)] = count #adds how many timsee that letter is seen to a list

# at this point in time i have a list of how many occurences of each letter in alphabet (including those that are not seen)

#This removes every letter that is not seen in the cipher text to reduce the amount of future operations when iterating over the letters
    cipherAlphabet = [[],[]]
    for i in range(0,26):
        if arrOccurences[i] != 0:
            cipherAlphabet[0].append(alphabet[i])           # The 0 or 1st list holds the letter
            cipherAlphabet[1].append(arrOccurences[i])      # the 1 or 2nd list holds the whole number occurence of the letter in the ciphertext
    cipherTotal = sum(cipherAlphabet[1])
    cipherLength = len(cipherAlphabet[0])

    arrFrequencies = [0] * cipherLength
    for i in range(0,cipherLength):
        arrFrequencies[i] = cipherAlphabet[1][i] / cipherTotal #This calculated the decimal value of frequency of each letter in ciphertext

    correlationOfFrequency = [[],[]] # a 2d list to store the letters and their C.O.F
    for i in range(26):
        correlation=0
        for j in range (cipherLength):  # This for loop is the summation of the Correlation Frequency for every letter of alphabet
            Letter = cipherAlphabet[0][j]
            letterIndex = alphabet.index(Letter)
            correlation += (arrFrequencies[j] * CharacterFrequencies[(letterIndex-i) % 26]) 
        correlationOfFrequency[0].append(alphabet[i])   #stores the letter
        correlationOfFrequency[1].append(correlation)   #corresponding correlation

    # Because the highest correlation of frequency is not always the key this while loop will travers through the highest frequencies 
    # decryting the ciphertext based on each key and output it to the user so that they may see if the message is decrypted correctly
    TF=True
    while(True):
        max=-1
        index=-1
        for i in range(26):
            if correlationOfFrequency[1][i] > max:
                max = correlationOfFrequency[1][i]
                index=i
        
        print(f"\n\nThe predicted key is: {correlationOfFrequency[0][index]} or a shift of {alphabet.index(correlationOfFrequency[0][index])}")

        text = plaintext(ciphertext, alphabet.index(correlationOfFrequency[0][index]))
        spaces = [index for index, char in enumerate(ciphertextInput) if char == ' ']
        
        for i, space in enumerate(spaces):
            text = text[:space] + ' ' + text[space:]

        print(f"\n\n{text}")

        yesNo=input("\nWas this the correct key? (Enter y/n): ").strip()

        if yesNo.upper() == 'Y':
            TF=False
            break
        elif yesNo.upper() == 'N':
            correlationOfFrequency[1][index]=0
        else:
            yesNo = input("invalid input try again: ")
main()


