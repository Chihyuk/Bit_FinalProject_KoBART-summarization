# CategorySql.py
from SqlCon import SqlCon

class CategorySql():
    @staticmethod
    def insertCat(c_id, c_name):
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_category (c_id, c_name) values({0}, '{1}')", c_id, c_name)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False

    @staticmethod
    def insertCatDet(cd_id, c_id, cd_name):
        cursor = SqlCon.Cursor()
        query = str.format("insert into N_category_detail (cd_id, c_id, cd_name) values({0}, {1}, '{2}')", cd_id, c_id, cd_name)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False

