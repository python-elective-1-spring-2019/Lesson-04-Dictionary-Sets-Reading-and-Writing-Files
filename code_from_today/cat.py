import sys


def cat(filename):
    f = open(filename, 'r')
    text = f.read()
    print(text)
    
    #lines = f.readlines()
    #print(lines)
    #for line in f:
    #    print(line, end='')


def main():
    cat(sys.argv[1])


if __name__ == "__main__":
    main()
