# NewsCatSql.py

from SqlCon import SqlCon

class NewsCatSql():
    # 언론사 전체 가져오기
    @staticmethod
    def findnidNumber():
        cursor = SqlCon.Cursor()
        query = str.format("select cd_id, c_id, cd_name from N_category_detail")
        try: 
            cursor.execute(query)
            row = cursor.fetchall()     # 검색 결과 중에 하나의 Row를 fetch하시오.
            SqlCon.Commit()
        except:
            return None
        else:
            return row

    # sid1 선택해서 가져오기
    @staticmethod
    def findnidSelectSID1(sid1):
        cursor = SqlCon.Cursor()
        query = str.format("select cd_id, c_id, cd_name from N_category_detail where c_id = {0}", sid1)
        try: 
            cursor.execute(query)
            row = cursor.fetchall()     # 검색 결과 중에 하나의 Row를 fetch하시오.
            SqlCon.Commit()
        except:
            return None
        else:
            return row
