
def main():
    input_list = map(int, raw_input().split())
    for i in xrange(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while ( input_list[j] > key and j >= 0):
            input_list[j+1] = input_list[j]
            j = j - 1
        input_list[j+1] = key
        # for k in xrange(i):
        #     print input_list[k],
        # print
    a, b , c , d = input_list
    if a + b > c or a + b >  d or b + c > d:
        print 'TRIANGLE'
    elif a + b == c or b + c == d :
        print 'SEGMENT'
    else:
        print 'IMPOSSIBLE'
        
    # if c + d > a :
    #     print 'TRIANGLE'
    # elif a + b == c or a + b == d  or b + c == d:
    #     print 'SEGMENT'
    # else:
    #     print 'IMPOSSIBLE'
            
    # # print input_list
    

if __name__ == '__main__':
    main()
