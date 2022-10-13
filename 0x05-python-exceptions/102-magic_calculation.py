#!/usr/bin/python3


def magic_calculation(a, b):
    answer = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                answer += a ** b / item
        except:
            answer = b + a
            break
    return (answer)

