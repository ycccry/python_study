from Heima_python.P124_CombinedTrain.file_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

#读取文件
text_reader = TextFileReader( "D:\\dirs\\Work\\python_study\\resorce\\test\\2011年1月销售数据.txt" )
json_reader = JsonReader( "D:\\dirs\\Work\\python_study\\resorce\\test\\2011年2月销售数据JSON.txt" )
data_list = text_reader.read_date()
json_list = json_reader.read_date()
all_data = data_list + json_list
dict_data = {}
for i in all_data:
    if i.date in dict_data.keys():
        dict_data[i.date] += i.money
    else:
        dict_data[i.date] = i.money
print(dict_data)

#可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(dict_data.keys()))
bar.add_yaxis("销售额",list(dict_data.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")