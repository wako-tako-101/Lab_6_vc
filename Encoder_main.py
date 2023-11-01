
#Warrick Brugal and Cesar Gonzales

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