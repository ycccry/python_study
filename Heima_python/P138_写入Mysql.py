from Heima_python.P124_CombinedTrain.file_define import *
from pymysql import Connection
#读取数据
text_reader = TextFileReader( "D:\\dirs\\Work\\python_study\\resorce\\test\\2011年1月销售数据.txt" )
json_reader = JsonReader( "D:\\dirs\\Work\\python_study\\resorce\\test\\2011年2月销售数据JSON.txt" )
data_list = text_reader.read_date()
json_list = json_reader.read_date()
all_data = data_list + json_list

#链接数据库
conn = Connection(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "123456",
    autocommit = True
)
print(conn.get_server_info())

#获得游标对象
cur = conn.cursor()
conn.select_db("study")

#组织SQL语句
for record in all_data:
    sql = (f"INSERT INTO orders VALUES"
             f"('{record.date}','{record.order_id}',{record.money},'{record.province}')")
    # print(sql)
    # 执行SQL语句
    cur.execute(sql)

#关闭MYSQL链接对象
conn.close()



