from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:\\Study\\Python\\python.exe"
os.environ['HADOOP_HOME'] = "C:\Study\hadoop_heima\hadoop-3.0.0"
#定义spark对象（入口）
conf = SparkConf().setMaster('local[*]').setAppName('spark_test1')
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)
data_rdd = sc.textFile("D:\\dirs\\Work\\python_study\\resorce\\第15章资料\\资料\\search_log.txt")\
    .map(lambda x:x.split('\t'))

#需求1：输出热门搜索时间段TOP3
rdd1 = data_rdd.map(lambda x:(x[0][:2],1))\
    .reduceByKey(lambda a,b:a+b)\
    .sortBy(lambda x:x[1],ascending=False,numPartitions=1)\
    .take(3)
print(rdd1)

#需求2：输出热门搜索词TOP3
rdd2 = data_rdd.map(lambda x:(x[2],1))\
    .reduceByKey(lambda a,b:a+b)\
    .sortBy(lambda x:x[1],ascending=False,numPartitions=1)\
    .take(3)
print(rdd2)

#需求3：输出黑马程序员在哪个时间段被搜索最多
rdd3 = data_rdd.filter(lambda x:x[2] == '黑马程序员')\
    .map(lambda x:(x[0][:2],1))\
    .reduceByKey(lambda a,b:a+b)\
    .sortBy(lambda x:x[1],ascending=False,numPartitions=1)\
    .take(5)
print(rdd3)

#需求4：将数据转换为JSON格式，写出为文件
rdd4 = data_rdd.map(lambda x:{'time':x[0],'user_id':x[1],'key_word':x[2],'rank1':x[3],'rank2':x[4],'url':x[5]})\
    .saveAsTextFile('D:\\dirs\\Work\\python_study\\resorce\\test\\unit15_test')