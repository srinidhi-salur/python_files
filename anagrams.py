def anagrams(word, words):
    d={}
    for s in word:
        if s not in d.keys():
            d[s]=1 
        else:
            d[s]+=1 
    ls=[]
    for i in range(len(words)):
        e={}
        for s in words[i]:
            if s not in e.keys():
               e[s]=1 
            else:
               e[s]+=1
        if e==d:
            ls.append(words[i])
    return(ls)
  print(anagrams('abba',['aabb','abab','abcd','bbba']))
            
    
