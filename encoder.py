#New file for final repository Cesar Gonzales Warrick Brugal
def encoder(pass_input):
    encoded_pass = ''

    for i in pass_input:
        if i == '0':
            encoded_pass+='3'
        elif i == '1':
            encoded_pass+='4'
        elif i == '2':
            encoded_pass+='5'
        elif i == '3':
            encoded_pass+='6'
        elif i == '4':
            encoded_pass+='7'
        elif i == '5':
            encoded_pass +='8'
        elif i == '6':
            encoded_pass+='9'
        elif i == '7':
            encoded_pass+='0'
        elif i == '8':
            encoded_pass+='1'
        elif i == '9':
            encoded_pass+='2'

    return encoded_pass

#print(encoder('0155562'))

#returns the original passcode by decoding the encoded passcode
def decoder(encoded_pass):
    decoded_pass = ''

    for i in encoded_pass:
        if i == '0':
            decoded_pass+='7'
        elif i == '1':
            decoded_pass+='8'
        elif i == '2':
            decoded_pass+='9'
        elif i == '3':
            decoded_pass+='0'
        elif i == '4':
            decoded_pass+='1'
        elif i == '5':
            decoded_pass+='2'
        elif i == '6':
            decoded_pass+='3'
        elif i == '7':
            decoded_pass+='4'
        elif i == '8':
            decoded_pass+='5'
        elif i == '9':
            decoded_pass+='6'

    return decoded_pass