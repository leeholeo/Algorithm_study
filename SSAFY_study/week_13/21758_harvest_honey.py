'''
greedy
뒤는 귀찮아서 적당히 짬 ㅎ
'''
N = int(input())
honeys = list(map(int, input().split()))
accum_forward = 0
maximum_forward = 0
for honey in honeys[2:-1]:
    accum_forward += honey
    maximum_forward = max(maximum_forward, honeys[1]-accum_forward-honey)
    if accum_forward > 10000:
        break
sum_forward = 2*sum(honeys[2:]) + maximum_forward

accum_backward = 0
maximum_backward = 0
for honey in honeys[N-3:0:-1]:
    accum_backward += honey
    maximum_backward = max(maximum_backward, honeys[-2]-accum_backward-honey)
    if accum_backward > 10000:
        break
sum_backward = 2*sum(honeys[:-2]) + maximum_backward

sum_mid = sum(honeys[1:-1]) + max(honeys[1:-1])

print(max(sum_forward, sum_backward, sum_mid))
