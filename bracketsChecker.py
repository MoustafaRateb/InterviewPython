

# Complete the isBalanced function below.
def isBalanced(s):
    br = []
    opens = ['(','{','[']
    for c in s:
        if c in opens:
            br.append(c)
            continue
        if br:
            last_br = br[-1]
            if last_br == '(' and c ==')':
                br.pop()
            elif  last_br == '{' and c =='}':
                br.pop()
            elif last_br == '[' and c ==']':
                br.pop()
            else:
                return 'NO'
        else:
            return 'NO'
    if br:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    inputFile =open('largeSample.txt','r')
    t = int(inputFile.readline())
    expected = ['YES','NO','NO','NO','NO','YES','NO','YES','NO','YES','NO','YES','YES','NO','NO','NO','YES','YES','YES','YES','YES','NO','NO','NO','NO','YES','YES','YES','YES','YES','YES','NO','NO','YES','YES','NO','NO','YES','NO','NO','NO','NO','NO','YES','NO','NO','NO','NO','NO','YES','YES','YES','NO','YES','YES','NO','NO','NO','YES','YES','YES','YES','NO','NO','NO','YES','NO','NO','NO','YES','YES','NO','NO','YES','YES','NO','NO','NO','YES','YES','NO','NO','NO','NO','YES','YES','NO','YES','NO','YES','NO','NO','YES','YES','YES','NO','NO','YES','YES','NO','YES','YES','NO','NO','YES','NO','YES','NO','NO','NO','NO','NO','NO','NO','YES','NO','NO','NO','YES','NO','YES','NO','NO','YES','YES','YES','NO','YES','YES','NO','YES','NO','NO','NO','NO','NO','NO','YES','NO','NO','NO','YES','NO','NO','NO','NO','YES','YES','YES','YES','YES','YES','NO','YES','NO','NO','YES','NO','NO','NO','YES','YES','NO','NO','NO','NO','NO','NO','YES','NO','NO','NO','YES','YES','YES','YES','YES','NO','YES','YES','NO','YES','YES','YES','NO','YES','YES','NO','YES','YES','YES','YES','YES','NO','YES','YES','NO','NO','YES','YES','NO','NO','NO','YES','YES','YES','NO','NO','NO','YES','NO','YES','NO','NO','NO','YES','NO','NO','YES','YES','NO','YES','NO','NO','NO','YES','NO','NO','NO','NO','NO','YES','YES','YES','YES','YES','YES','YES','NO','YES','NO','NO','YES','NO','NO','NO','NO','YES','NO','YES','NO','YES','YES','NO','YES','YES','YES','YES','NO','YES','YES','YES','NO','NO','NO','NO','YES','YES','YES','YES','NO','NO','YES','NO','NO','NO','YES','NO','YES','NO','NO','NO','YES','YES','NO','YES','NO','NO','NO','YES','YES','YES','NO','YES','YES','NO','YES','NO','NO','YES','YES','NO','YES','YES','NO','YES','NO','YES','NO','YES','YES','YES','NO','NO','NO','NO','NO','YES','YES','YES','NO','YES','NO','YES','NO','NO','NO','YES','NO','NO','NO','YES','YES','NO','YES','NO','NO','YES','YES','YES','YES','YES','YES','NO','NO','NO','YES','NO','NO','YES','NO','NO','YES','NO','YES','YES','NO','NO','NO','NO','NO','YES','YES','YES','YES','YES','NO','YES','NO','NO','YES','NO','YES','NO','NO','NO','NO','YES','NO','NO','YES','NO','NO','YES','YES','YES','NO','YES','YES','NO','NO','NO','YES','NO','YES','YES','NO','NO','NO','YES','NO','YES','NO','NO','YES','YES','YES','NO','NO','YES','NO','NO','NO','NO','NO','YES','NO','YES','NO','NO','NO','NO','NO','YES','YES','YES','YES','YES','YES','YES','YES','NO','YES','YES','NO','NO','YES','NO','YES','NO','NO','NO','YES','YES','NO','YES','YES','YES','NO','NO','YES','YES','NO','YES','YES','NO','YES','YES','NO','NO','YES','YES','NO','YES','NO','NO','NO','NO','YES','NO','YES','NO','YES','NO','NO','NO','YES','NO','NO','YES','NO','YES','NO','NO','NO','NO','YES','NO','NO','YES','NO','YES','YES','YES','YES','YES','YES','NO','YES','NO','YES','NO','NO','NO','NO','YES','YES','NO','NO','YES','YES','YES','YES','NO','YES','NO','NO','YES','YES','NO','NO','YES','YES','YES','YES','YES','YES','NO','NO','YES','YES','YES','YES','NO','YES','NO','NO','NO','NO','YES','YES','NO','NO','NO','YES','YES','NO','YES','NO','NO','YES','YES','NO','YES','NO','YES','YES','YES','YES','YES','YES','NO','NO','NO','YES','YES','NO','YES','NO','YES','YES','YES','NO','YES','YES','YES','YES','NO','NO','YES','NO','NO','NO','NO','NO','YES','YES','NO','YES','YES','YES','NO','YES','NO','YES','YES','YES','NO','NO','YES','YES','YES','YES','NO','NO','YES','YES','YES','NO','NO','YES','YES','NO','NO','NO','YES','YES','NO','NO','YES','YES','NO','YES','NO','NO','NO','YES','YES','NO'] 
    for t_itr in range(t):
        s = inputFile.readline()

        result = isBalanced(s)
        check = result == expected[t_itr]
        print(result,check,t_itr)