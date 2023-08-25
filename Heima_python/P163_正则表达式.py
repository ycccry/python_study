import re

#搜索邮箱：qq
str_mail = "012865666@qq.comag602826423.16345151@qq.comadf86106595165.we46@#$51651612@qq.com"
#从头开始查找
r = r'[1-9][1-9]{6,9}@qq.com'
res1 = re.match(r,str_mail)
print(res1)

#查找满足条件的第一个
res2 = re.search(r,str_mail)
print(res2.group())

#查找满足条件的所有
res3 = re.findall(r,str_mail)
print(res3)


