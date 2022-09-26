#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all names defined by hidden_4 modules."""

    import hidden_4

    n = dir(hidden_4)
    from name in n:
        if name[:2] != "__":
            print(name)
