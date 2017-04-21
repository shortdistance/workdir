#-*-coding:utf-8-*-

import UserList
if __name__ == '__main__':
    ul1 = UserList.UserList()
    ul1.append('123')
    ul1.append(2)
    ul1.insert(0, 3)
    ul1.insert(1, 4)
    ul1.insert(2, 4)
    print ul1.count(4)

    print ul1

    ul2 = ('5', 6, 7, 8)
    ul1.extend(ul2)
    print ul1.index('5')
    print ul1
    ul1.pop()
    print ul1
    ul1.remove(4)
    print ul1
    ul1.reverse()
    print ul1

    ul1.sort()
    print ul1
    


    pass
