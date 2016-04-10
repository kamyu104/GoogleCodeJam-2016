# Time:  O(N)
# Space: O(1)

def revenge_of_the_pancakes():
    stack = raw_input().strip()
    # The best strategy is to flip between
    # two pancakes facing opposite directions 
    return stack.count('-+') + stack.count('+-') + int(stack.endswith('-'))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, revenge_of_the_pancakes())
