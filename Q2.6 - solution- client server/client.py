import socket

IP = '127.0.0.1'
PORT = 1729
MAX_LEN_INPUT = 4


def print_instructions():
    print("|welcome                                            |\n" +
          "| Here are the server commands:                     |\n" +
          "| to print out the local time - Press 'time'        |\n" +
          "| to print out the name of the server - Press 'name'|\n" +
          "| to print out a random number(1,10) - Press 'rand'  |\n" +
          "| to exit of the program - Press 'exit'             |\n")


def check_input(the_input):
    # check if the input is not equal to 4 bytes
    if len(the_input) == MAX_LEN_INPUT:
        return True
    else:
        print("'" + the_input + "' is not recognized as an internal or external command\n try again")
        return False


def main():
    # print instructions
    print_instructions()

    # loop until user requested to exit
    to_exit = False
    while not to_exit:
        client = socket.socket()
        client.connect((IP, PORT))

        print('enter a command: ')

        # get the user's input
        while True:
            client_input = input()
            # check if input Length == 4 Bytes
            if check_input(client_input):
                break

        # send the command to the server
        client.send(client_input.encode())
        data = client.recv(1024)
        if data.decode().lower() != 'exit':
            print(data.decode())
        client.close()

        # if the command == 'exit', then the server will send to the client -> 'end'
        if data.decode() == 'exit':
            to_exit = True
            client.close()


if __name__ == '__main__':
    main()
