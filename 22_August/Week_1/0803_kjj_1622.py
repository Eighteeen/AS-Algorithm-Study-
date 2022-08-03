while True:
    try:
        a = input()
        b = input()
        answer = []
        for i in range(a):
            if i in b:
                answer.append(i)
                b = b.replace(i,"",1) ## 아 이생각을 못했네..
        answer.sort
        print(''.join(answer))
    except:
        break
        
