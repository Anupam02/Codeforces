import time 
import sys

def main():
    n, m, a = map(int, raw_input().split())
    start = time.time()
    l = b = 1
    if n % a == 0:
        l = n/a
    else:
        l = n/a + 1
    if m % a == 0:
        b = m/a
    else:
        b = m/a + 1
    print l*b
    end = time.time()
    execution_time = end-start
    print "---- % seconds -----" %execution_time

def Petr_Version_Codeforces():
 
    # lines = [ [ int(x) for x in line.strip().split() ] for line in sys.stdin ]
    # inputs = lines[0]
    # n = inputs[0]
    # m = inputs[1]
    # a = inputs[2]
    n, m, a = map(int , raw_input().split())
    start = time.time()
    answer = ( ( n + a - 1) / a ) * ( ( m + a - 1) / a)
    print answer
    end = time.time()
    print " ------- %s seconds ------- " %( end -start)
    
if __name__ == '__main__':
    main()
    Petr_Version_Codeforces()
