
#Warrick Brugal and Cesar Gonzales
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

if __name__ == '__main__':

    run = True

    while run:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        Select = int(input('Please enter an option:'))

        if Select == 1:
            number = input('Please enter you password to encode:')
            encoded_password = encoder(number)
            print('Your password has been encoded and stored!')

        if Select == 2:
            decoded_password = decoder(encoded_password)
            print('The encoded password is', encoded_password, 'and the original password is', decoded_password, end='.\n')

        if Select == 3:
            exit()