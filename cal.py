#예전에 만든 만년단력 재활용
#함수 호출시에 년도와 월을 전달
#율리우스력만 적용된 상태이므로 그레고리력을 적용하려면 보정이 필요
#미리 준비하는 데이터를 축소 20200108
def mycalendar(y,month):
    monthdays1=[31,28,31,30,31,30,31,31,30,31,30,31,31] #각 월의 일 수
    #monthdays2=[31,29,31,30,31,30,31,31,30,31,30,31,31] #윤년
    #monthdays3=[31,30,31,30,31,31,30,31,30,31,28,31] #과거 달력 계산을 위해 1을 뒤집음
    #monthdays4=[31,30,31,30,31,31,30,31,30,31,29,31] #과거 달력 계산을 위해 2를 뒤집음
    weekdays=[]
    iniday1=6 #2018.12.1 의 요일(6은 토요일)  2019년 이후의 각 월별 1일의 요일을 판정하기 위한 기초값
    iniday2=2 #2019.1.1 의 요일(2는 화요일)  2019년 이전의 각 월별 1일의 요일을 판정하기 위한 기초값
    if y >= 2019: #2019년 이후의 달력을 위한 요일 위치 계산
        dis=y-2019 #기준인 2019년 과의 차이
        iniday=iniday1 #요일 계산을 위한 기초값
        for i in range(dis+1): #평년 윤년을 판정하여 요일 계산시에 다른 날짜를 삽입 "+1"은 2019년을 처리하기 위함
            weekdays=[]#배열이 누적되므로 적절히 초기화
            if (i+3)%4==0:
                monthdays=monthdays1.copy()
                monthdays[1]=29
            else:
                monthdays=monthdays1
            for i in range(12):
                weekday=iniday+monthdays[i-1]%7
                if weekday>=7:
                    weekday=weekday-7
                weekdays.append(weekday)
                iniday=weekday
    if y < 2019: #2018년 이전의 각 월의 시작점을 계산하여 역순으로 저장
        dis=2019-y
        iniday=iniday2
        for i in range(dis):
            weekdays=[]#배열이 누적되므로 적절히 초기화
            monthdays=list(reversed(monthdays1.copy()))#최근 값 부터 거꾸로 계산해 들어가야 하므로 #월의 배열도 뒤집어진 것을 사용
            if (i+2)%4==0:
                monthdays[10]=29 
            else:
                pass
                #monthdays=monthdays3
            for i in monthdays:
                weekday=iniday-i%7
                if weekday<0:
                    weekday=weekday+7
                weekdays.append(weekday)
                iniday=weekday
        temp=[] #역순인 배열을 뒤집기
        for i in reversed(weekdays):
            temp.append(i)
        weekdays=temp
#여기서부터는 출력부
    if y%4==0:
        monthdays=monthdays1.copy()
        monthdays[1]=29
    else:
        monthdays=monthdays1
    print("\t\t",y,"년    ",month,"월\n\n일\t월\t화\t수\t목\t금\t토\n") #달력의 헤더
    count=0
    for i in range(weekdays[month-1]): #미리 선언한 배열에서 시작 요일의 위치를 가져와 공백 삽입
        print("\t",end="")
    for i in range(0,monthdays[month-1]): #미리 선언한 배열에서 날짜 수를 가져와서 반복
        print("{:>2}".format(i+1),end="\t")
        if ((i+weekdays[month-1])+1)%7 == 0: #시작 요일위치+반복시행수의 합이 7이 될때마다 개행
            count=count+1
            print("\n")
    print("\n")
    pass    
    if count<5:
        print("\n")