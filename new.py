import os
import time

def main():
    with open('source') as file:
        newfile = read_file()
        start = time.time()
        if newfile:
            os.system('ping -c 2 ' + newfile)

        elif read_file() == '':
            dump = file.read()
            dump = dump.splitlines()

            for ip in dump:
                os.system('ping -c 2 ' + ip)
            newfile = read_file()
            os.system('ping -c 2 ' + newfile)
        stop = time.time()
        print('')
        print('Runtime: ' + str(stop - start))


def read_file():
    ifile = input('Input IP to check: ')
    return ifile


if __name__ == '__main__':
    main()
