# 리스트 첫번째 값을 맨 뒤로 보내고 첫번째 값 삭제하면 0번지가 1번지로 밀리지 않을까 생각했는데
# 첫번째 값 삭제되면 두번째 주소가 0번지로 변경됨.

p = [1,2,3,4]

p.append(p[0])
del p[0]

print(p)

print(p[0]) 