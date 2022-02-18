# NewsCatSql.py

from SqlCon import SqlCon

class TotalSql():
    # 기사 내용 전체 가져오기
    @staticmethod
    def findContent():
        cursor = SqlCon.Cursor()
        c_id = 100
        query = str.format("select nc.n_id, n_content, c_id from N_content nc inner join News n on nc.n_id = n.n_id inner join N_category_detail ca on n.cd_id = ca.cd_id where nc.n_id > 6316 and c_id = {0}", c_id)
        try: 
            cursor.execute(query)
            row = cursor.fetchall()
            SqlCon.Commit()
        except:
            return None
        else:
            return row

    # 기사 전체 내용 insert
    @staticmethod
    def insertSum(nid, nsc):
        cursor = SqlCon.Cursor()
        
        temp_content = nsc
        temp_content = temp_content.replace("\'", "\\\'")
        temp_content = temp_content.replace("\"", "\\\"")
        # temp_content = temp_content.replace("\n", ". ")
        # temp_content = temp_content.replace("\t", " ")
        query = str.format("insert into N_summarization (n_id, ns_content) values({0}, '{1}')", nid, temp_content)

        try: 
            cursor.execute(query)
            SqlCon.Commit()
        except:
            return None
        else:
            print(nid)
            return True

    # 기사 내용 앞에서 가져오기
    @staticmethod
    def findContent_front():
        cursor = SqlCon.Cursor()
        c_id = 100
        query = str.format("select nc.n_id, n_content, c_id from N_content nc inner join News n on nc.n_id = n.n_id inner join N_category_detail ca on n.cd_id = ca.cd_id where nc.n_id > 6316 and c_id = {0}", c_id)
        try: 
            cursor.execute(query)
            row = cursor.fetchall()
            SqlCon.Commit()
        except:
            return None
        else:
            return row

    # 앞에서 가져온 기사 넣기
    @staticmethod
    def insertSum_front(nid, nsc, exist):
        cursor = SqlCon.Cursor()

        temp_content = nsc
        temp_content = temp_content.replace("\'", "\\\'")
        temp_content = temp_content.replace("\"", "\\\"")
        # temp_content = temp_content.replace("\n", ". ")
        # temp_content = temp_content.replace("\t", " ")
        query = str.format("insert into N_summarization (n_id, ns_content) values({0}, '{1}')", nid, temp_content)

        try: 
            cursor.execute(query)
            SqlCon.Commit()
        except:
            exist += 1
            return exist
        else:
            print(nid)
            exist = 0
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