from pyspark import SparkConf,SparkContext
import json
import os
os.environ['PYSPARK_PYTHON'] = "C:\\Study\\Python\\python.exe"
#定义spark对象（入口）
conf = SparkConf().setMaster('local[*]').setAppName('spark_test1')
sc = SparkContext(conf=conf)

#读取数据
city_rdd=sc.textFile('D:\\dirs\\Work\\python_study\\resorce\\第15章资料\\资料\\orders.txt')
dict_rdd = city_rdd.flatMap(lambda x:x.split('|')).map(lambda x:json.loads(x))

#需求1：各个城市销售额排名，降序
rdd1 = ((dict_rdd.map(lambda x:(x['areaName'],int(x['money'])))
        .reduceByKey(lambda a,b:a+b))
        .sortBy(lambda x:x[1],ascending=False,numPartitions=1))
print('需求1结果：',rdd1.collect())

#需求2：全部城市，有哪些商品类别在售卖
rdd2 = dict_rdd.map(lambda x:x['category']).distinct()
print('需求2结果：',rdd2.collect())

#需求3：北京有哪些商品类别在售卖
rdd3 = (dict_rdd.filter(lambda x:x['areaName'] == '北京')
        .map(lambda x:x['category'])).distinct()
print('需求3结果：',rdd3.collect())