from  __future__ import print_function
def main():
    s = raw_input()
    d = raw_input()

    left_2_right = ord(d[0]) - ord(s[0])
    top_2_bottom = int(s[1]) - int(d[1])

    if left_2_right > 0:
        step = 'R'
    elif left_2_right < 0:
        step = 'L'
    else:
        step = ''
    
    if top_2_bottom > 0:
        step_next = 'D'
    elif top_2_bottom < 0:
        step_next = 'U'
    else:
        step_next = ''

    ## chanding to absolute values
    left_2_right = abs(left_2_right)
    top_2_bottom = abs(top_2_bottom)
    max_iter = max( left_2_right, top_2_bottom )
    print(max_iter)
    walk = []
    for itr in xrange(1, max_iter + 1):
        walk.append('')
        if itr <= left_2_right:
            walk[itr-1] += step 
        if itr <= top_2_bottom:
            walk[itr-1] += step_next
    # print( walk)
    for s in walk:
        print(s)
    

if __name__ == '__main__':
    main()
