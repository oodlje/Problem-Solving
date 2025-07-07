import sys
get=sys.stdin.readline().strip()
group={"M":"MatKor","W":"WiCys","C":"CyKor","A":"AlKor","$":"$clear"}
print(group[get])