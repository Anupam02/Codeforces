import sys

def main( *args, **kwargs):
    chessboard = []
    for line in sys.stdin:
        chessboard.append( [ w for w in  filter( lambda x: x != '\n' ,line)
 ])
    count = 0
    for x in xrange(len(chessboard)):
        if all ( map ( lambda w : w == 'B' ,chessboard[x] ) ):
            count += 1
        if all ( map ( lambda w : w == 'B' , ( y for w in xrange(8) for y in chessboard[w][x]) ) ):
            count += 1
    if count == 16:
        print '8\n'
    else:
        print count
    
if __name__ == '__main__':
    main()
