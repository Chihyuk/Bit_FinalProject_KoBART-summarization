# GetTime.py
import datetime 
from NewsExtract import NewsExtract
from NewsSql import NewsSql

class GetTime():
    # 시간 처리해서 가져오기
    @staticmethod
    def getTime(numdays) : # 나오게할 날짜 갯수
        baseDate = datetime.date.today() 
        d_list = [baseDate - datetime.timedelta(days=x) for x in range(numdays)]
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 

    # 2019년부터 가져오기
    @staticmethod
    def getTime_Past() : # 나오게할 날짜 갯수
        baseDate = datetime.date(2019, 1, 1)
        d_day = datetime.date.today() - baseDate
        d_day = int(str(d_day)[0:4])
        d_list = [baseDate + datetime.timedelta(days=x) for x in range(d_day)]
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 


    @staticmethod
    def compareTime(news):
        # 현재 기사의 시간
        nTime = news.time
        nTime_Sec = nTime[:10] + nTime[11:] + ":00"
        nTime_Sec = nTime_Sec.replace(".", "-")
        # DB에 저장된 마지막 시간
        try:
            lTime = NewsSql.findMaxTimeNews()
            lastTime = lTime.strftime("%Y-%m-%d %H:%M:%S")      # datetime.datetime 형식을 str로 변경ㅉ
        except:
            lastTime = '1900-01-01 12:30:00'
        finally:
            # 현재 기사 시간이 DB에 저장된 시간보다 이전인 경우 1, 아닐 경우 0 return
            if nTime_Sec < lastTime:
                return 1
            else:
                return 0