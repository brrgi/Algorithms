# [투 포인터]
N = int(input())
str = input()
def check():
    start = 0
    end = 0
    string_count = 0
    total_max = 0
    string_dict = {}
    
    while end < len(str):
        if str[end] not in string_dict.keys():
            string_dict[str[end]] = 0
        string_dict[str[end]] += 1

        if len(string_dict.keys()) > N:
            while len(string_dict.keys()) > N:
                string_dict[str[start]] -= 1
                # 만약에 하나를 제거했을 때, 0이면 dict에서 제거 
                if string_dict[str[start]] == 0:
                    del string_dict[str[start]]
                start += 1
        end += 1
        string_count = end - start
        total_max = max(total_max, string_count)
    return total_max

print(check())