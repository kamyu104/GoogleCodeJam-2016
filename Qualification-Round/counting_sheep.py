# Time:  O(P), P is the smallest power of 10 greater than N
# Space: O(1)

def counting_sheep():
    N = int(input())
    if N == 0:
        return "INSOMNIA"

    digits = set([])
    cnt = 0
    while len(digits) != 10:
        cnt += N
        tmp = cnt
        while tmp:
            digits.add(tmp % 10)
            tmp /= 10
    return cnt

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, counting_sheep())
