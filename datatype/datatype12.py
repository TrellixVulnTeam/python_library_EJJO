from graphlib import TopologicalSorter

ts = TopologicalSorter()
# 규칙1
ts.add("영어 중급", "영어 초급")  # 영어 중급의 선수 과목은 영어 초급
ts.add("영어 고급", "영어 중급")  # 영어 고급의 선수 과목은 영어 중급

# 규칙2
ts.add("영어 문법", "영어 중급")  # 영어 문법의 선수 과목은 영어 중급
ts.add("영어 고급", "영어 문법")  # 영어 고급의 선수 과목은 영어 문법

# 규칙3
ts.add("영어 회화", "영어 문법")  # 영어 회화의 선수 과목은 영어 문법

print(list(ts.static_order()))
