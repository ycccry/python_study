from pyspark import SparkConf,SparkContext
import os
#声明本地python解释器路径
os.environ['PYSPARK_PYTHON'] = "C:\\Study\\Python\\python.exe"
#定义spark对象（入口）
conf = SparkConf().setMaster('local[*]').setAppName('spark_test1')
sc = SparkContext(conf=conf)
#读取测试文件,分割字符
rdd1 = sc.textFile("D:\\dirs\\Work\\python_study\\resorce\\第15章资料\\资料\\hello.txt")
rdd2 = rdd1.flatMap(lambda x : x.split(' ')).map(lambda x : (x,1))
# print(rdd2.collect())
#分组求和
rdd3 = rdd2.reduceByKey(lambda a,b:a+b)
print(rdd3.collect())
sc.stop()
