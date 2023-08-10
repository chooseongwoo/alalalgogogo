cm, kg = map(float, input().split())

avgkg = (cm - 100) * 0.9
obesity = (kg - avgkg) * 100 / avgkg

if obesity > 20:
    print('비만')
elif obesity >= 10:
    print('과체중')
else:
    print('정상')