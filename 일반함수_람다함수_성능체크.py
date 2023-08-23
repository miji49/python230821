def getEvent(i): 
    return i % 2 == 0

lst = list(range(1,100))

def a():
    iterL = filter(getEvent, lst)
    for i in iterL:
        print(i**2)

def b():
    print([i**2 for i in lst if i % 2 ==0])


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("a()", number=10, globals=globals()))
    print(timeit.timeit("b()", number=10, globals=globals()))