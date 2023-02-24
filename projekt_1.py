#Numbers from 1 to scope=100 divisible by 8

def gen_list_divisable_by(scope=None,div=None):
    if not scope:
        scope = 100
    if not div:
        div = 8
    results = []
    for i in range(1,scope+1):
        if (i % div) == 0:
            results.append(i)
    return results

if __name__ == "__main__":
    scope=None
    div=None
    while True:
        try:
            scope=input("give range: ")
            scope=int(scope)
            break
        except ValueError:
            if not scope: break
            print("It's OK")
    while True:
        try:
            div=input("give divisable: ")
            div=int(div)
            break
        except ValueError:
            if not div: break
            print("It's OK")
    print("Found ", len(gen_list_divisable_by(scope,div)), "numbers")
    