import sys

def greeting(name):
    print(f"Hey, how are you? {name}")

if __name__ == '__main__':
    greeting(sys.argv[1])
