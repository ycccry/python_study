f1 = open('D:\\dirs\\Work\\python_study\\resorce\\test\\bill.txt','r',encoding='UTF-8')
f2 = open('D:\\dirs\\Work\\python_study\\resorce\\test\\bill_cope.txt','w',encoding='UTF-8')

for line in f1:
    data = line.split(',')
    if data[-1].strip() != '测试':
        f2.write(line)
    continue
f1.close()
f2.close()
