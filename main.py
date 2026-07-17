def hanoi_solver(ite):
    l_1 = [x for x in range(ite, 0, -1)]
    l_2 = []
    l_3 = []

    return wswap(l_1, l_2, l_3, ite)


def swap(arr1, arr2):
    arr2.append(arr1[len(arr1) - 1])
    arr1.pop(len(arr1) - 1)





def wswap(arr1, arr2, arr3, ite):
    x = ""
    if ite % 2 != 0:
        for j in range(1, 2 ** ite + 1):
            x += f"{j-1}.{arr1} {arr2} {arr3}\n"
            arra = [arr1,arr2,arr3]
            y = 0
            oyayo(arra,j,y)
    else:
        for j in range(1, 2 ** ite + 1):
            x += f"{j-1}.{arr1} {arr2} {arr3}\n"
            arra = [arr1,arr2,arr3]
            y = 0
            oyaye(arra,j,y)

    return x.strip()


def get(arr):
    if len(arr) == 0:
        return -1
    return arr[-1]


def oyayo(arra,j,x):
    x += 1
    if j % 2 != 0:
        for i in range(3):
            p = arra[i]
            if get(p) == x:
                break
            
        if get(p) % 2 == 0:
            if i==0:
                swap(arra[0],arra[1])
            elif i == 1:
                swap(arra[1],arra[2])
            elif i == 2:
                swap(arra[2],arra[0])
        else:
            if i==0:
                swap(arra[0],arra[2])
            elif i == 1:
                swap(arra[1],arra[0])
            elif i == 2:
                swap(arra[2],arra[1])
        return arra
    else:
        j //= 2
        return oyayo(arra,j,x)
def oyaye(arra,j,x):
    x += 1
    if j % 2 != 0:
        for i in range(3):
            p = arra[i]
            if get(p) == x:
                break
            
        if get(p) % 2 != 0:
            if i==0:
                swap(arra[0],arra[1])
            elif i == 1:
                swap(arra[1],arra[2])
            elif i == 2:
                swap(arra[2],arra[0])
        else:
            if i==0:
                swap(arra[0],arra[2])
            elif i == 1:
                swap(arra[1],arra[0])
            elif i == 2:
                swap(arra[2],arra[1])
        return arra
    else:
        j //= 2
        return oyaye(arra,j,x)

        


print(hanoi_solver(6))
