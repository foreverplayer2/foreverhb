import random

def hb(num):
    ans = str(random.randint(10 ** (num - 1), 10 ** (num) - 1))
    print(ans)
    
    ans1 = [ans[i:i+1] for i in range(num)]
    print(ans1)
    
    ans2 = ''.join(ans)
    
    print(f'数あてゲームを始めるよ! 答えだと思う{num}桁の数値を入れてね!')
    for _ in range(100): 
        image = input()
        image1 = [image[i:i+1] for i in range(num)]
        
        if ans1 == image1:
            print(f'正解、すごい!')
            break
        
        elif ans1 != image1:
            n = 0
            m = 0
            j = 0
            for j in range(num):
                if image1[j] in ans1:
                    index1 = ans1.index(image1[j])
                    
                    if index1 == j:
                        n += 1
                    
                    
                        
                    elif index1 != j:
                        m += 1
                        
                else:
                    pass
            print(f'{n}ヒット, {m}ブローだよ!')
    
    print(f'答えは{int(ans)}でした！')     
    print('merge1の練習')     
                   
        
hb(3)
