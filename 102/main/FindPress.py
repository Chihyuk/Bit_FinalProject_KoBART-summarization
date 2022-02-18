# FindPress.py

import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from WebRobot import WebRobot
from EHHelper import EHHelper
import re

class FindPress:
    def __init__(self, press_num, press_name):
        self.press_num = press_num
        self.press_name = press_name

    @staticmethod
    def findPress():
        # 기사 가져오기
        res = WebRobot.CollectHtml("https://news.naver.com/main/officeList.naver")
        i = 0   # tr tag 돌리기
        j = 0   # li tag 돌리기

        # 빈 리스트 생성
        press_name = []
        press_num = []
        press = FindPress()
        oid = re.compile('(oid=)([0-9]*)')

        while(True):
            try:
                j += 1
                # 언론사 추출
                tags_press_name = res.select(f'#groupOfficeList > table > tbody > tr:nth-child({i}) > td > ul > li:nth-child({j}) > a')
                tags_press_num = res.select(f'#groupOfficeList > table > tbody > tr:nth-child({i}) > td > ul > li:nth-child({j}) > a')[0]['href'] 

                # 제목 추출
                for tag_press_name in tags_press_name:
                    press_name.append(tag_press_name.text.strip())

                # 언론사 번호만 따오기
                press_num.append(int(oid.search(tags_press_num).group(2)))

            except:
                i += 1          # tr 번호 증가
                j = 0           # li 번호 초기화
                if i > 10:      # 네이버에서 제공하는 언론사 카테고리는 총 10개
                    break
                else:
                    continue
        return FindPress(press_num, press_name)

# 테스트
#press = FindPress.findPress()
#print("언론사 :", len(press.press_name), type(press.press_name))
#print("언론사 번호 :", len(press.press_num), type(press.press_num))
