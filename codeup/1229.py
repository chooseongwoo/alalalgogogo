cm, kg = map(float, input().split())
avgKg = 0

if cm >= 160:
    avgKg = (cm - 100) * 0.9
elif cm >= 150:
    avgKg = (cm - 150) / 2 + 50
else:
    avgKg = cm - 100

obesity = (kg - avgKg) * 100 / avgKg

if obesity > 20:
    print('비만')
elif obesity > 10:
    print('과체중')
else:
    print('정상')