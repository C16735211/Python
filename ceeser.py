# Darren Byrne
# C16735211 

# Program in Python ceasea cipher that ciphers 
# text to display a message within the alphabet 
# 0 to 26 

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cracking caesar encryption with brute-force
def caesar_crack(cipher_text):

    # try all the possible key values
    for key in range(len(ALPHABET)):
        #reinitialize this to be an empty string
        plain_text = ''

        # make a simple caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index-key)%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]


        # print the actual decrypted string with the given key
        print('With key %s, the message result is: %s'%(key, plain_text))

if __name__ == "__main__":

    encrypted = 'VJKUBKUBCBOGUUCIG'
    caesar_crack(encrypted)
            

        
