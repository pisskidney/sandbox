def is_centered_palindrom(l):
    half = len(l) / 2
    max_l = 0
    comps = 0
    for i in range(1, half + 1):
        comps += 1
        if l[half - i] == l[half + i - 1]:
            max_l += 2
        else:
            break
    return max_l, comps


def palindrom2(l, left, right):
    # always check for middle
    comps = 0
    m, c = is_centered_palindrom(l)
    comps += c
    max_l = m
    if max_l == len(l):
        return max_l, comps
    for x in range(1, max(left / 2, right / 2) + 1):
        if x <= left / 2:
            m, c = is_centered_palindrom(l[:-2 * x])
            comps += c
            max_l = max(max_l, m)
            if max_l == len(l) - 2 * x:
                return max_l, comps
        if x <= right / 2:
            m, c = is_centered_palindrom(l[2 * x:])
            comps += c
            max_l = max(max_l, m)
            if max_l == len(l) - 2 * x:
                return max_l, comps
    return max_l, comps


def palindrom(l):

    if len(l) == 2:
        if l[0] == l[1]:
            return 2, 1
        return 0, 1

    half = len(l)/2
    max_left, c1 = palindrom(l[:half])
    max_right, c2 = palindrom(l[half:])
    max_middle, c3 = palindrom2(l, max_left, max_right)

    return max(max_left, max_right, max_middle), c1 + c2 + c3


import random

i = [random.randint(0, 3) for a in range(2**8 - 200)]
p = list(range(100, 200)) + list(range(100, 200))[::-1]
i[10:10] = p
p, c = palindrom(i)
print 'input size:', len(i), 'palindrom size:', p, 'computations:', c


i = 'a' * 2**10
p, c = palindrom(i)
print 'input size:', len(i), 'palindrom size:', p, 'computations:', c

i = 'a' * 2**18
p, c = palindrom(i)
print 'input size:', len(i), 'palindrom size:', p, 'computations:', c

i = [random.randint(0, 3) for a in range(2**18)]
p, c = palindrom(i)
print 'input size:', len(i), 'palindrom size:', p, 'computations:', c

i = [random.randint(0, 15) for a in range(2**18-300)]
i[10000:10000] = [4] * 100
i[23000:23000] = range(1, 101) + range(100, 0, -1)
p, c = palindrom(i)
print 'input size:', len(i), 'palindrom size:', p, 'computations:', c
