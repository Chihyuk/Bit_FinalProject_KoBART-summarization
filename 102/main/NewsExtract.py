# NewsExtract.py

from WebRobot import WebRobot
from Article import Article
from NewsSql import NewsSql
import re

class NewsExtract():
    # 원하는 항목 다 가져오기
    # 완성된 기사 url을 input 사용
    @staticmethod
    def extract(url, cd_id, c_id):
        try :
            # 생성자 만들기
            art = Article()
            art.cd_id = cd_id
            art.c_id = c_id
            # 기사 가져오기
            res = WebRobot.CollectHtml(url)

            # 제목 추출
            tags_title = res.select('#articleTitle')
            # 내용 추출
            tags_content = res.select('#articleBodyContents')
            # 날짜 추출
            tags_time = res.select('#main_content > div.article_header > div.article_info > div > span:nth-child(1)')
            # 원문 링크 추출
            tags_link = res.select('#main_content > div.article_header > div.article_info > div > a:nth-of-type(1)')[0]['href'] 
            # 사진 링크 추출
            try:
                tags_pic_link = res.select("#articleBodyContents > .end_photo_org > img")[0]['src']
            except:
                tags_pic_link = 'None'
            finally:
                # 언론사 이름 추출
                tags_media = res.select('#main_content > div.article_header > div.press_logo > a > img')[0]['alt']

                # 제목 추출
                temp_title = tags_title[0].text
                temp_title = temp_title.replace("\'", "\\\'")
                temp_title = temp_title.replace("\"", "\\\"")
                art.title = temp_title.strip()

                # 내용 추출
                temp_content = tags_content[0].text
                temp_content = temp_content.replace("\xa0", " ")
                #temp_content = temp_content.replace("\n", " ")
                #temp_content = temp_content.replace("\r", " ")
                temp_content = temp_content.replace("  ", "\n")
                temp_content = temp_content.replace("\t", "\n")
                temp_content = temp_content.replace("\'", "\\\'")
                temp_content = temp_content.replace("\"", "\\\"")
                art.content = temp_content.strip()
                
                # 날짜 추출
                time_temp = tags_time[0].text.strip()
                time_compile_D = re.compile('([0-9]*[.][0-9]*[.][0-9]*[.])')
                time_compile_H = re.compile('([0-9]*)(:)')
                time_compile_M = re.compile('(:)([0-9]*)')
                time_compile_AM = re.compile('오전')
                time_compile_PM = re.compile('오후')

                try:
                    D = time_compile_D.search(time_temp).group(1)
                    H = time_compile_H.search(time_temp).group(1)
                    M = time_compile_M.search(time_temp).group(2)

                    # 날짜 오전 오후 처리
                    if time_compile_AM.search(time_temp):
                        art.time = D+" "+H+":"+M
                    elif time_compile_PM.search(time_temp):
                        art.time = D+" "+str(int(H)+12)+":"+M
                except:
                    art.time = '9999-12-31'

                # 원문 링크 추출
                art.link = tags_link.strip()
                
                # 사진 추출
                art.pic_link = tags_pic_link.strip()

                # 언론사 이름 추출
                art.press_name = tags_media.strip()

                # 언론사 번호 추출
                oid = re.compile('(oid=)([0-9]*)')
                art.press_num = oid.search(url).group(2)

                return art

        except:
            return False


#a1 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=119&aid=0002566181", 226,105)
#NewsSql.insertNews(a1)
#NewsSql.insertDescNews(a1)

#NewsSql.insertDescNews(a1)
# a2 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=018&aid=0005123091", 100,100)
# a3 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=025&aid=0003165201", 100,100)
# a4 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=277&aid=0005027916", 100,100)
# print("오전1자리",a1.time)
# print("오전2자리",a2.time)
# print("오후1자리",a3.time)
# print("오후2자리",a4.time)

#NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LPOD&mid=sec&oid=009&aid=0004906767", 100,100)