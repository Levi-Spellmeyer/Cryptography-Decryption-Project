Things I used for the first time completing this project: <br>
1. `var.replace(" ", "")` I used this to remove all spaces in specified strings but this can be used to replace specified characters like symbols or other letters
2.  `var for var, var2 in enumerate(variable text)` In the Caeser cipher I used this to put spaces back into my plaintext after removing them from the input ciphertext. The enumerate function allows you to keep up with multiple variables. In my case, I used it to keep up with the variable I was using to iterate as well as the indexs I would soon insert spaces into
3. `for i, space in enumerate(spaces): text = text[:space] + ' ' + text[space:]` I added spaces back into my code by maniplulating my cipher text to add spaces where specified. I wouuld overwrite my existing text variable with the characters of the ciphertext up to where I wanted to add the space, add in the desired space, then add the rest of the ciphertext back.
4. `index = alphabet.index(letter)` This takes the variable letter and fands it's index in the alphabet list which is then saved to index.
5. `arrFrequencies[i] = round(cipherAlphabet[1][i] / cipherTotal, 4)` The round function rounds decimal values based on the digit you place where I typed a 4


Things I could change or do better
1. I could have utilized directories instead of using as many list of lists.
2. I could have just used a string that contained every letter of the alphabet instead of a 2 layer list with letters and numbers (which I did more for testing sake than cleanliness)
3. I could have created a function within the Vigenere code to combine all of the decrypted alphabets into the final plaintext
4. Include a loop in vigenere as I did in Caeser cipher that allows user to iterate through most possible keys of decryption


 
