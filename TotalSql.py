# NewsCatSql.py

from SqlCon import SqlCon

class TotalSql():
    # 기사 내용 전체 가져오기
    @staticmethod
    def findContent(order="asc"):
        cursor = SqlCon.Cursor()
<<<<<<< HEAD
        if order == "desc":             # 인자 값을 desc를 받으면 오름차순 정렬 시키기
            query = str.format("select n_id, n_content from N_content order by n_id desc")
        else:
            query = str.format("select n_id, n_content from N_content where n_id > 26500 order by n_id")
            #query = str.format("select n_id, n_content from N_content")
=======
        query = str.format("select n_id, n_content from N_content where n_id > 26500 order by n_id")
        #query = str.format("select n_id, n_content from N_content")
>>>>>>> 8eb897c93e9b5e6b1ddd327c0dd203f5abfa1f45
        try: 
            cursor.execute(query)
            row = cursor.fetchall()
            SqlCon.Commit()
        except:
            return None
        else:
            return row


    # 기사 전체 내용 insert
    # 앞에서 가져온 기사 넣는 경우 exist 인자를 받아 처리하기
    @staticmethod
    def insertSum(nid, nsc, exist=0):
        cursor = SqlCon.Cursor()

        temp_content = nsc
        temp_content = temp_content.replace("\'", "\\\'")       # 작은따옴표 처리
        temp_content = temp_content.replace("\"", "\\\"")       # 큰따옴표 처리
        # temp_content = temp_content.replace("\n", ". ")
        # temp_content = temp_content.replace("\t", " ")
        query = str.format("insert into N_summarization (n_id, ns_content) values({0}, '{1}')", nid, temp_content)

        try: 
            cursor.execute(query)
            SqlCon.Commit()
        except:
            exist += 1                                          # 에러가 발생한 경우 이미 값이 들어갔다고 판단해 exist 변수 +1
            return exist
        else:
            print(nid)
            exist = 0                                           # 값이 들어간 경우 exist 변수 초기화를 위해 0을 넣어줌
            return exist

    # 한 줄 요약
    def insertSum_One(nid, nsc):
        cursor = SqlCon.Cursor()
        
        temp_content = nsc
        temp_content = temp_content.replace("\'", "\\\'")
        temp_content = temp_content.replace("\"", "\\\"")
        # temp_content = temp_content.replace("\n", ". ")
        # temp_content = temp_content.replace("\t", " ")
        query = str.format("insert into N_summarization_one (n_id, nso_content) values({0}, '{1}')", nid, temp_content)

        try: 
            cursor.execute(query)
            SqlCon.Commit()
        except:
            return None
        else:
            print(nid)
            return True
