# 팀 구성 리스트 초기화
team = ["나명흠", "박소진", "윤준열", "김성광", "임재훈"]
navi_list = []
obs_list = []
driver_list = []
# 옵저버 역할을 맡을 팀원 선택 (매일 한명씩 돌아가며)
obs_index = 0

# 14일간의 팀 구성 리스트 작성
for day in range(14):
    # 팀 구성
    navi_list.append([team[(obs_index+1)%5], team[(obs_index+2)%5]])
    driver_list.append([team[obs_index], team[(obs_index+3)%5]])
    obs_list.append(team[(obs_index+4)%5])
    # 옵저버 인덱스 업데이트
    obs_index = (obs_index+1) % 5

# 결과 출력
print("14일간의 팀 구성 리스트:")
for day in range(14):
    print(f"Day {day+1}: 네비게이터 {navi_list[day]}, 드라이버 {driver_list[day]}, 옵저버 {obs_list[day]}")