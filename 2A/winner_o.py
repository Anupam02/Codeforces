import time
def main():
    n = int(raw_input())
    names_score = {}
    score_list = []
    start = time.time()
    for turn in xrange(1, n+1):
        name, score = raw_input().split()
        names_score[name] = names_score.get(name, []) + [int(score)]
        score_list.append( (name, sum( names_score[name] ) ) )
    ## what is the scenario where time takes while giving input
    ## for an instance here we are taking input by for turn in xrange(1, n+1)
    ## and all other additional time overhead is consumed by dictionary append and list append , does it really matters?

    first_player , second_player = names_score.keys()
    final_score_f_player = sum(names_score[first_player])
    final_score_s_player = sum(names_score[second_player])

    if final_score_f_player > final_score_s_player:
        print first_player
    elif final_score_s_player > final_score_f_player:
        print second_player
    else:
        winner = first_player
        for player, comm_score in score_list:
            if comm_score == final_score_f_player:
                winner = player
                break
    print winner
    end = time.time()
    print ' ---- %s seconds -----' %(end - start)
    


if __name__ == '__main__':
    main()
        
            
        


