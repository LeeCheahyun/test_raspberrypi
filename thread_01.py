import threading

def firstfunc(age):
    while True:
        print("I'm first child", age)
    return

def secondfunc(age):
    while True:
        print("I'm second child", age)
    return

if __name__ == '__main__' :
    first = threading.Thread(target=firstfunc, args=(5,))
    second = threading.Thread(target=secondfunc,args=(3,))
    first.start()
    second.start()
    first.join()
    second.join()

    while True:
        print("I'm perents")
    pass