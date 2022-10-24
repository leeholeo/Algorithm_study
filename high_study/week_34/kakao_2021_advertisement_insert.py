'''
누적합 + 구간합
'''
HOUR_TO_SECOND = 3600
HOUR_TO_MINUTE = 60
MINUTE_TO_SECOND = 60


def time_to_second(time: str) -> int:
    return HOUR_TO_SECOND * int(time[:2]) + MINUTE_TO_SECOND * int(time[3:5]) + int(time[6:])


def second_to_time(second: int) -> str:
    return ':'.join((f'{second//HOUR_TO_SECOND:0>2}', f'{(second//MINUTE_TO_SECOND)%HOUR_TO_MINUTE:0>2}', f'{second%MINUTE_TO_SECOND:0>2}'))


def solution(play_time, adv_time, logs):
    play_second = time_to_second(play_time)
    user = [0] * (play_second+2)
    adv_second = time_to_second(adv_time)
    for log in logs:
        user[time_to_second(log[:8])] += 1
        user[time_to_second(log[9:])] -= 1
    user_now = 0
    user_accum = user
    for s in range(adv_second-1):
        user_now += user[s]
        user_accum[s] = user_accum[s-1] + user_now
    max_accum = 0
    end_second = adv_second
    for s in range(adv_second-1, play_second):
        user_now += user[s]
        user_accum[s] = user_accum[s-1] + user_now
        accum_second = user_accum[s] - user_accum[s-adv_second]
        if accum_second > max_accum:
            max_accum = accum_second
            end_second = s
    start_second = end_second - adv_second + 1
    start_time = second_to_time(start_second)
    return start_time


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
solution(play_time, adv_time, logs)
