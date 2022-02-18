# WebRobot.py

import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
import threading

class WebRobot:
    # 웹 페이지를 수집만을 위한 메소드
    # url : 수집할 사이트 주소
    @staticmethod
    def Collect(url):
        try:
            # 웹 페이지 수집 객체 생성
            request = ureq.Request(url)
            # 웹 페이지 요청 (반환값은 요청 결과 웹 페이지)
            response = ureq.urlopen(request)
        except:                             # 요청 실패하였을 때
            return None 
        else : 
            if response.getcode() != 200:   # 요쳥 결과 값이 성공이 아닐 때
                return None
            return response                 # 요청 성공하였을 때

    # html 웹페이지 수집 메소드
    # url : 수집할 웹페이지 주소
    @staticmethod
    def CollectHtml(url):                   # HTML 파싱을 하기 위함
        # 웹 페이지 수집 요청
        response = WebRobot.Collect(url)
        if response == None:                # 결과가 없을 때
            return None
        try :
            # html로 파싱
            html = BeautifulSoup(response,'html.parser')
        except :                            # 파싱 예외 발생할 때
            return None
        else :                              # 파싱 성공했을 때
            return html
