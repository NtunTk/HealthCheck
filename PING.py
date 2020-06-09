import os
import time



def main():
    with open('source') as file:
        dump = file.read()
        dump = dump.splitlines()

        start = time.time()
        for ip in dump:
            os.system('ping -c 2 ' + ip)
        stop = time.time()

        print('')
        print('Runtime: ' + str(stop - start))

if __name__ == '__main__':
    main()
