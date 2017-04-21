#-*-coding:utf-8-*-

def coinChange (x):
    l1 = [25, 10, 5, 1]
    if 0<x<1:
        v1 = 100 * x
        l2 = []
        for key1 in l1:
            if v1 % key1 !=0:
                if v1>key1:
                    l2.append(int(v1/key1))
                    v1 = v1 % key1
                else:
                    l2.append(0)
                    continue;
            else:
                l2.append(int(v1/key1))
                return l2
        else:
            return []
    else:
        return []



    
    

if __name__ == '__main__':
    print coinChange(0.81)
    pass
