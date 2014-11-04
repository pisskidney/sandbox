#!/usr/bin/python


c = {
    0: '1111110',
    1: '0110000',
    2: '1101101',
    3: '1111001',
    4: '0110011',
    5: '1011011',
    6: '1011111',
    7: '1110000',
    8: '1111111',
    9: '1111011',
}


def sol(states):
    working = states[0]
    for i in xrange(1, len(states)):
        working = ''.join([
            str(int(working[j]) | int(states[i][j]))
            for j in xrange(len(working))
        ])

    res = [[] for _ in xrange(len(states))]

    for i in xrange(len(states)):
        for k, v in c.iteritems():
            if ''.join([str(int(v[j]) | int(states[i][j])) for j in xrange(7)]) == v:
                for j in xrange(7):
                    if v[j] == '1' and states[i][j] == '0' and working[j] == '1':
                        break
                res[i].append(k)

    ans = []
    for i in xrange(len(res[0])):
        current = res[0][i]
        ok = True
        for j in xrange(1, len(res)):
            if (current > 0 and (current - 1) not in res[j]) or (current == 0 and 9 not in res[j]):
                ok = False
                break
            else:
                current = current - 1 if current > 0 else 9
        if ok and ans:
            return 'ERROR'
        elif ok and not ans:
            ans.append(c[current - 1 if current > 0 else 9])
    return 'ERROR' if not ans else ''.join([ans[0][i] if bool(int(working[i])) else '0' for i in xrange(7)])


def main():
    f = open('easy.in', mode='r')
    f2 = open('easy.out', mode='w')
    t = int(f.readline())
    for x in xrange(t):
        states = f.readline().rstrip().split(' ')[1:]
        f2.write('Case #%s: %s\n' % (x + 1, sol(states)))


    
    '''
    print sol(('0100000', '0000111', '0000011'))
    print sol(('0000000', '0001010'))
    print sol(('1111111',))
    '''





                

            




if __name__ == "__main__":
    main()




