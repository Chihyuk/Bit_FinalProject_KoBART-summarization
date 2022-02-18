# FindNewsCat.py
# 카테고리 별 번호
# 경제 sid1=101
# 금융 sid2=259
# 증권 sid2=258

# input url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=' 

from CategorySql import CategorySql
from NewsCatSql import NewsCatSql
from WebRobot import WebRobot
import re

class FindNewsCat:
    # 카테고리 찾아 DB에 넣기
    @staticmethod
    def findNewsCat():
        # cat_name = []

        for i in range(6):
            url = f'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{i}'
            res = WebRobot.CollectHtml(url)
            # 대분류 추출
            tags_cat = res.select('#lnb > ul > li.on > a > span.tx')
            cat_num = 100+i
            # 대분류명 추출
            for tag_cat in tags_cat:
                cat_name = (tag_cat.text.strip())

            CategorySql.insertCat(cat_num, cat_name)     # 쿼리 넣기

            j = 1
            sid2 = re.compile('(sid2=)([0-9]*)')

            # 소분류 추출
            while(True):
                try:
                    tags_cat_d = res.select(f'#snb > ul > li:nth-child({j}) > a')
                    tags_cat_d_id = res.select(f'#snb > ul > li:nth-child({j}) > a')[0]['href']

                    tag_cat_d_id = int(sid2.search(tags_cat_d_id).group(2))
                    
                    if not tags_cat_d:
                        break

                    j += 1

                    # 소분류명 추출
                    cat_d_name = (tags_cat_d[0].text.strip())

                    CategorySql.insertCatDet(tag_cat_d_id ,cat_num, cat_d_name)
                except:
                    break

    # url에 카테고리 합치기 
    @staticmethod
    def catInsert(url):
        # 모든 카테고리
        # sids = ['sid2=259&sid1=101', 'sid2=258&sid1=101', ...]
        sids = []
        cat = NewsCatSql.findnidNumber()
        for i in range(len(cat)):
            sids.append('sid2='+str(cat[i][0])+'&sid1='+str(cat[i][1]))
        sidurls = []
        for n in range(len(sids)):
            sidurls.append(url+sids[n]+'&mid=shm&date=')
        return sidurls, sids    # 카테고리가 포함된 주소와 카테고리 번호 리턴

    # sid1을 넣어 url에 카테고리 합치기 
    @staticmethod
    def catInsertbySID1(url, sid1):
        # 모든 카테고리
        # sids = ['sid2=259&sid1=101', 'sid2=258&sid1=101', ...]
        sids = []
        cat = NewsCatSql.findnidSelectSID1(sid1)
        for i in range(len(cat)):
            sids.append('sid2='+str(cat[i][0])+'&sid1='+str(cat[i][1]))
        sidurls = []
        for n in range(len(sids)):
            sidurls.append(url+sids[n]+'&mid=shm&date=')
        return sidurls, sids    # 카테고리가 포함된 주소와 카테고리 번호 리턴

