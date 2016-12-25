import inspect

def dump(obj):
    print("Type")
    print("====")
    print(type(obj))
    print()

    print("Documentation")
    print("=============")
    print(inspect.getdoc(obj))
    print()

    print("Methods")
    print("=======")
    # TODO
    print()


i = 10
dump(i)