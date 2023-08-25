from pymysql import Connection
import json
conn = Connection(
    host="localhost",
    port=3306,
    user = "root",
    password="123456",
    autocommit=True
)
cur = conn.cursor()
conn.select_db("study")

sql = f"select * from orders;"
cur.execute(sql)
data = cur.fetchall()

def save_to_json(data,file_name):
    with open(file_name,'w') as f:
        for item in data:
            f.write(json.dumps(item)+'\n')

all_data = []
for d in data:
    jd = {
        "date":str(d[0]),
        "order_id":d[1],
        "money":d[2],
        "province":d[3]
    }
    all_data.append(jd)
save_to_json(all_data, 'data.json')
