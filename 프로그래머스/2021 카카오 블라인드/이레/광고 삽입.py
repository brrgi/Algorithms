import re


def solution(play_time, adv_time, logs):
    answer = ''
    first = list(map(int, split_time_string(play_time)))  # 시 분 초 시 분 초
    second = list(map(int, split_time_string(adv_time)))
    play_time = first[0] * 3600 + first[1] * 60 + first[2]
    adv_time = second[0] * 3600 + second[1] * 60 + second[2]
    visit=[0 for i in range(360001)]
    sums=[0 for i in range(360001)]


    for log in logs:
        three=list(map(int, split_time_string(log)))
        start=three[0] * 3600 + three[1] * 60 + three[2]
        end=three[3] * 3600 + three[4] * 60 + three[5]
        visit[start]+=1
        visit[end]-=1

    for i in range(360001):
        visit[i]+=visit[i-1]
    sums[0] = sum(visit[:adv_time])

    max_val=sum(visit[:adv_time])
    start=0
    cur_val=max_val
    for i in range(0, play_time-adv_time+1):
        cur_val=cur_val-visit[i-1]+visit[i+adv_time-1]
        if cur_val>max_val:
            max_val=cur_val
            start=i


    answer=''
    answer+=str(start//3600).zfill(2)+":"
    start=start%3600
    answer+=str(start//60).zfill(2)+":"
    start=start%60
    answer+=str(start).zfill(2)
    return answer
def split_time_string(strs):
    return re.split(r'[-:]', strs)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))
