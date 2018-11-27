

def main(*args, **kwargs):
    input_str = raw_input()
    pattern1 = raw_input()
    pattern2 = raw_input()
    
    main_ptr =  pattern1_ptr =  pattern2_ptr = 0
    is_forward =  is_pattern1 =  is_pattern2 = False
    
    while pattern1_ptr < len(pattern1) and main_ptr < len(input_str):
        if pattern1[pattern1_ptr] == input_str[main_ptr] :
            pattern1_ptr += 1
        main_ptr += 1
        
    if pattern1_ptr == len(pattern1):
        is_pattern1 = True

        
    while pattern2_ptr < len(pattern2) and main_ptr < len(input_str):
        if pattern2[pattern2_ptr] == input_str[main_ptr]:
            pattern2_ptr += 1
        main_ptr += 1
        
    if pattern2_ptr == len(pattern2):
        is_pattern2 = True

        
    if is_pattern1 and is_pattern2:
        is_forward = True

    

    rev_input_str = input_str[::-1]
    
    pattern1_ptr = pattern2_ptr = main_ptr = 0
    is_backward = is_pattern1 = is_pattern2 = False
    
        
    while pattern1_ptr < len(pattern1) and main_ptr < len(rev_input_str):
        if pattern1[pattern1_ptr] == rev_input_str[main_ptr] :
            pattern1_ptr += 1
        main_ptr += 1
        
    if pattern1_ptr == len(pattern1):
        is_pattern1 = True

        
    while pattern2_ptr < len(pattern2) and main_ptr < len(rev_input_str):
        if pattern2[pattern2_ptr] == rev_input_str[main_ptr]:
            pattern2_ptr += 1
        main_ptr += 1
        
    if pattern2_ptr == len(pattern2):
        is_pattern2 = True

        
    if is_pattern1 and is_pattern2:
        is_backward = True

        
    if is_forward and is_backward:
        print 'both'
    elif is_forward :
        print 'forward'
    elif is_backward:
        print 'backward'
    else:
        print 'fantasy'
    
    


if __name__ == '__main__':
    main()

    
    
