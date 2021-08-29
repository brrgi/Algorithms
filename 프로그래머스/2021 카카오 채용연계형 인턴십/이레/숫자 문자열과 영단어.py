# 1시 42 -> 1시 58 (16분)
def solution(s):
    nums={'0','1','2','3','4','5','6','7','8','9'}
    strs = {'four', 'three', 'zero', 'six', 'nine', 'one', 'eight', 'two', 'five', 'seven'}
    dic=dict()
    dic['zero'] = '0'
    dic['one']='1'
    dic['two']='2'
    dic['three'] = '3'
    dic['four'] = '4'
    dic['five'] = '5'
    dic['six'] = '6'
    dic['seven'] = '7'
    dic['eight'] = '8'
    dic['nine'] = '9'

    answer = 0
    result=[]
    start=''
    for i in s:
        if i in nums:
            if start!='':
                result.append(dic[start])
                start=''
            result.append(i)
        else:
            if start in strs:
                result.append(dic[start])
                start=i
            else:
                start+=i
    if start!='':
        result.append(dic[start])
    answer=''.join(result)
    print(answer)
    return answer


s="123"
solution(s)
