# -*- coding: utf-8 -*-
# main.py

from Function import Function
from FindNewsCat import FindNewsCat
import time
import threading
from datetime import datetime

def main():
    print("==================메뉴==================")
    print("1. bs4 선택")
    print("2. selenium 선택")
    select1 = input("숫자를 입력해주세요 : ")
    if int(select1) == 1:
        print("Beautifulsoup를 선택하였습니다.")
        print("1. 언론사 업데이트")
        print("2. 과거 뉴스 넣기")
        print("3. 최신 뉴스 넣기")
        print("4. 카테고리 넣기")
        select2 = input("숫자를 입력해주세요 : ")
        if int(select2) == 1:
            print("언론사 업데이트 중")
            Function.press()
            print("언론사 업데이트가 끝났습니다.")
        elif int(select2) == 2:
            print("과거 뉴스 정보를 DB에 넣습니다.")
            past()
        elif int(select2) == 3:
            print("최신 뉴스 정보를 DB에 넣습니다.")
            today()
        elif int(select2) == 4:
            print("카테고리 찾아 넣기")
            FindNewsCat.findNewsCat()
    elif int(select1) == 2:
        print("Selenium을 선택하였습니다.")

def past():
    sid1list = range(100, 106)
    for sid1 in sid1list:
        print("-------------------------------------------------------------------------------------------")
        print("sid1 = " + str(sid1) + "에 해당하는 기사 가져오기")
        Function.pastNewss_sid1(sid1)
        print("sid1 = " + str(sid1) + "에 해당하는 기사를 다 넣었습니다.")
        print("5분간 멈췄다 다음 카테고리 크롤링 시작")
        print("현재 시간 : ", datetime.now())
        time.sleep(300)

    print("모든 카테고리의 기사를 넣었습니다.")
    print("10분 후 다시 크롤링 시작합니다.")
    print("현재 시간 : ", datetime.now())
    threading.Timer(600, past).start()

def today():
    # sid1list = range(100, 106)
    # for sid1 in sid1list:
    sid1 = 102
    print("-------------------------------------------------------------------------------------------")
    print("sid1 = " + str(sid1) + "에 해당하는 기사 가져오기")
    Function.presentNews_sid1(sid1)
    print("sid1 = " + str(sid1) + "에 해당하는 기사를 다 넣었습니다.")
    print("5분간 멈췄다 다음 카테고리 크롤링 시작")
    print("현재 시간 : ", datetime.now())
    time.sleep(300)

    print("모든 카테고리의 기사를 넣었습니다.")
    print("10분 후 다시 크롤링 시작합니다.")
    print("현재 시간 : ", datetime.now())
    threading.Timer(600, today).start()


if __name__ == "__main__":
    main()
    #today()