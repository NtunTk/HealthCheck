import time
import requests



def main():
    while True:
        start = time.time()
        r = requests.get(str(input('Enter url: ')))
        if r.status_code == 200:
            print('Healthy!')
        else:
            print('Oops! Something is wrong.')
            print(r)
        stop = time.time()
        print('')
        print('Runtime = ' + str(stop - start))

if __name__ == '__main__':
    main()
