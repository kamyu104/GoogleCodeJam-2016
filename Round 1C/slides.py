def slides():
    B, M = map(int, raw_input().strip().split())
    if M > (2 ** (B - 2)):
        return []
    res = [[0 for _ in xrange(B)] for _ in xrange(B)]
    for i in xrange(1, B - 1):
        for j in xrange(i + 1, B):
            res[i][j] = 1

    if M == 2 ** (B - 2):
        for j in xrange(1, B):
            res[0][j] = 1
    else:
        j = B - 2
        while M:
            res[0][j] = M % 2
            M /= 2
            j -= 1
    return res

for case in xrange(input()):
    res = slides()
    if not res:
        print 'Case #%d: %s' % (case+1, "IMPOSSIBLE")
    else:
        print 'Case #%d: %s' % (case+1, "POSSIBLE")
        for row in res:
           print "".join(map(str, row))