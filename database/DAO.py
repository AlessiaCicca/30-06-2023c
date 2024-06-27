from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getSquadre():
        conn = DBConnect.get_connection()

        result = []


        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.name as squadra
from teams t
 order by t.name"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["squadra"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(squadra):
        conn = DBConnect.get_connection()

        result = []
        dizio={}

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.`year` as anno, AVG(P.weight) as peso
from appearances a , teams t , people p 
where t.ID =a.teamID  and t.name =%s
and p.playerID =a.playerID 
group by a.`year` """

        cursor.execute(query,(squadra,))

        for row in cursor:
            result.append(row["anno"])
            dizio[row["anno"]]=row["peso"]

        cursor.close()
        conn.close()
        return result,dizio

