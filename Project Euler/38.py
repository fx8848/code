def f1(n):
    strNum = str(n)
    for i in range(1,5):
        tmpStr = strNum
        num = int(strNum[:i])
        index = 1
        flag = False
        while True:
            str1 = str(num*index)
            len1 = len(str1)
            if str1 == tmpStr[:len1]:
                if len(tmpStr)>len1:
                    tmpStr=tmpStr[len1:]
                elif len(tmpStr) == len1:
                    flag = True
                    break
            else:
                break
            index += 1
        if flag:
            return True
    return False

numList=[1,['','12345678']]
while True:
    if numList[0]==40320:
    #8!=362880
        break
    for i in range(1,numList[0]+1):
        left = numList[i][0]
        right= numList[i][1]
        l = left+right[0]
        r = right.replace(right[0],'')
        numList[i] = [l,r]
        for j in right[1:]:
            l = left+j
            r = right.replace(j,'')
            numList.append([l,r])
            numList[0] += 1
numStrList = []
for i in numList[1:]:
    numStrList.append('9'+i[0]+i[1])
del numList
# print numStrList
# print len(numStrList)
result = 0
for i in numStrList:
    if f1(int(i)):
        if int(i) > result:
            result = int(i)
print result
