import re


def solution(play_time, adv_time, logs):
    answer = ''
    first = list(map(int, split_time_string(play_time)))  # 시 분 초 시 분 초
    second = list(map(int, split_time_string(adv_time)))
    play_time = first[0] * 3600 + first[1] * 60 + first[2]
    adv_time = second[0] * 3600 + second[1] * 60 + second[2]
    visit=[0 for i in range(play_time)]
    sums=[0 for i in range(play_time)]


    for log in logs:
        three=list(map(int, split_time_string(log)))
        for i in range(three[0] * 3600 + three[1] * 60 + three[2], three[3] * 3600 + three[4] * 60 + three[5]):
            visit[i]+=1

    sums[0] = sum(visit[:adv_time])
    for i in range(1, play_time - adv_time + 1):
        sums[i] = sums[i - 1] + visit[i + adv_time - 1] - visit[i - 1]

    max_val=0
    start=0
    for i in range(0, play_time-adv_time+1):
        if sums[i]>max_val:
            max_val=sums[i]
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
