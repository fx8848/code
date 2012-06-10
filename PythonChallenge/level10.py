#http://www.pythonchallenge.com/pc/return/bull.html
import re  
  
if __name__ == '__main__':  
    counter = 0  
    def fun(s):  
        result = ''  
        char = s[0]  
        count = 0  
        for x in s:  
            if x == char:  
                count += 1  
            else:  
                result += str(count) + char  
                count = 1  
                char = x  
        result += str(count) + char  
        print(len(result))  
        global counter  
        counter += 1  
        if counter < 30:  
            fun(result)  
    fun('1')  
    #solution 2 Start  
    def describe(s):  
        sets = re.findall("(1+|2+|3+)", s)  
        return ''.join(str(len(x)) + x[0] for x in sets)  
    s = '1'  
    for dummy in range(30):  
        s = describe(s)  
    print(len(s))  
    #solution 2 End  
