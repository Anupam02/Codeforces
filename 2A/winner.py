
def main():
    n = int(raw_input())
    names_score = {}
    score_list = []
    
    for turn in xrange(1, n+1):
        name, score = raw_input().split()
  
        names_score[name] = names_score.get(name, 0) + int(score)
  
        score_list.append( (name, names_score[name]) )

  
  
    max_score = max( names_score.values() )
    winner_candidates = [ name for name, score in names_score.items() if score == max_score ]
    
    winner = ""
    for name, score in score_list:
        if score >= max_score and name in winner_candidates:
            winner = name
            break

    print winner
    


if __name__ == '__main__':
    main()
        
            
        


