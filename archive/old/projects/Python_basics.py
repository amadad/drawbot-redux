if 0:
    # Integer
    print 12, 23, 34
    print 2323 * 23

if 0:
    # Float
    print 23.23 * 23.23

if 0:    
    # String
    print 'This is a string'
    print "This is a string"
    print 'This is a "quoted" string'
    print """This 'is' a "quoted" string"""


# List
if 0:
    print [12, 23, 'AAA', 23, 14] + [5,5]
    aa = [12,12,12]
    aa.append(77)
    print aa
    print aa[1], len(aa), aa[2:5]

    hugeList = []
    for n in range(10000):
        hugeList.append(n)
    print hugeList[233:-600]
    
# Tuple
if 0:
    print (12, 23, 'AAA', 23, 14) + (5,5)*3
    aa = (12,12,12)
    #aa.append(77)
    print aa
    print aa[1], len(aa), aa[2:5]
    bb = list(aa)
    bb.append(77)
    print bb
    
# Dictionary
if 0:
    d = {'ccc': 666, 'aaa':123, 'bbb': 345}
    print d
    print d['aaa']
    print d.keys()
    print d.values()
    for key, value in d.items():
        print key, '-->', value
    
# Set
if 0:
    s = set([34,34,34,34,34,34,45])
    print s

    print d.items()

    a = (23,34,45,65)
    print a
    qq,ww,ee,rr = a
    print qq,ww,ee,rr

# Swap
a = 10
b = 20

a, b = b, a
print a, b