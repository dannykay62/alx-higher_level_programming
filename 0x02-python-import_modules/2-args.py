#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of arguments in a list"""
    from sys import argv

argc = len(argv)
if argc < 2:
    print("{} arguments.".format(argc - 1))
else:
    if argc == 2:
        print("{} arguments:".format(argc - 1))
    else:
        print("{} arguments:".format(argc -1))
    for i in range(1, argc):
        print("{}: {}".format(n, argv[n]))
