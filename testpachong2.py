import requests #发送请求
import re #正则表达式，用于提取网页数据
import winsound #提醒程序运行结束
import time #计算程序运行时间

Dishkeys=["sucai1","yuecai","chuancai","lucai","xiangcai","mincai","zhecai","huicai","jingcai","hucai","yucai","hubeicai","dongbeicai","xibeicai","yunguicai","gangtaicai","guangxicai","shanxicai","huaiyangcai","jiangxicai"]
Dishval=["苏菜","粤菜","川菜","鲁菜","湘菜","闽菜","浙菜","徽菜","京菜","沪菜","豫菜","湖北菜","东北菜","西北菜","云贵菜","港台菜","广西菜","山西菜","淮扬菜","江西菜"]
#all_url = [] #创建一个数组用于存储网页地址

"""def get_all_url(n,dish): #这个函数用于获得网页中的菜的全部网址
    if(n==1):
        url = "https://m.meishij.net/caixi/%s/"%dish
    else:
        url='https://m.meishij.net/caixi/%s/p%s/'%(dish,n) #%s相当于C语言中的%s，表示格式化一个对象为字符，同理%d表示格式化一个对象为整数
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" }
    response = requests.get(url,headers=headers) #访问网页
    response.encoding = "utf-8" #设置接收编码格式

    pattern = re.compile(r'<a target="_blank" href="([a-zA-z]+://[^\s]*)">', re.S)
    #正则表达式提取网页中的网址，re.S表示在整个文本中进行匹配，如果不加re.S，将只在一行进行匹配
    result = pattern.findall(response.text) #获取的网页结果存储到result里
    all_url.append(result[0:10])#由于每页只有十道菜，result中只有前十条对应的是菜的网址，故我们只添加前十条
    return all_url #作为返回值返回这个列表"""
total_url=[]
def url_iters(n,d):
    
    for dish in d:
        all_url = [] #创建一个数组用于存储网页地址
        for i in range(1,n):#逐页获取菜谱网页信息
            if(i==1):
                url = "https://m.meishij.net/caixi/%s/"%dish
            else:
                url='https://m.meishij.net/caixi/%s/p%s/'%(dish,i) #%s相当于C语言中的%s，表示格式化一个对象为字符，同理%d表示格式化一个对象为整数
                print(i)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" }
            response = requests.get(url,headers=headers) #访问网页
            response.encoding = "utf-8" #设置接收编码格式

            pattern = re.compile(r'<a target="_blank" href="([a-zA-z]+://[^\s]*)">', re.S)
    #正则表达式提取网页中的网址，re.S表示在整个文本中进行匹配，如果不加re.S，将只在一行进行匹配
            result = pattern.findall(response.text) #获取的网页结果存储到result里
            all_url.append(result[0:10])#由于每页只有十道菜，result中只有前十条对应的是菜的网址，故我们只添加前十条
        total_url.append(all_url)
    return total_url


def get_info(resp,output,D,i,url_now):
    name_pattern = re.compile(r'<h1>(.*)</h1>')# 正则表达式获取菜名信息
    food_pattern = re.compile(r'<span class="t">(.*)</span><span class="a">')
    #(.*)</span></a></div>')# 正则表达式获得主料信息
    #fixing_pattern = re.compile(r'<div class="c_mtr_li"><span class="t1">(.*)</span><span class="a">(.*)</span></div>') # 正则表达式获得辅料信息
    fearture1_pattern = re.compile(r'<div class="cpargs cpargs2"><div class="i"></div>(.)</div>')# 正则表达式获得特征_1
    fearture2_pattern = re.compile(r'<div class="cpargs cpargs3"><div class="i"></div>(.*)</div>')# 正则表达式获得特征_2

    name = name_pattern.findall(resp.text) # 提取菜名信息
    food = food_pattern.findall(resp.text)# 提取主料信息
    #fixing = fixing_pattern.findall(resp.text)#提取辅料信息
    fearture1 = fearture1_pattern.findall(resp.text) #提取特征_1
    fearture2 = fearture2_pattern.findall(resp.text)#提取特征_2

    output.write(str(name))#将菜名写入output文件，write函数不能写int类型的参数，所以使用str()转化
    output.write('\t')#进入下一个单元格
    output.write(str(D[i]))#将菜系
    output.write('\t')#进入下一个单元格
    output.write(str(fearture1))#将特征_1写入output文件
    output.write('\t')#进入下一个单元格
    output.write(str(fearture2))#将特征_2写入output文件
    output.write('\t')#进入下一个单元格
    
    output.write(str(food))
    output.write('\t')

    # for i in range(len(food)):
    #     for j in range(len(food[i])):
    #         output.write(str(food[i][j]))    #写入主料
    #         output.write('\t')
            
    #if(len(food)<11):
        #out.write('\t'*2*(11-len(food))) #每道菜的主料数目不同，该行代码可使表格内容对齐

    # for i in range(len(fixing)):
    #     for j in range(len(fixing[i])):
    #         output.write(str(fixing[i][j]))    #写入辅料
    #         output.write('\t')
    output.write(url_now)#将url
    output.write('\t')#进入下一个单元格
    output.write('\n')    #换行


def spider(dish):
    output = open('C:\\code field\\c code\\菜谱库.xls','w',encoding='utf-8')#创建一个excel文件，编码格式为utf-8
    output.write('名称\t菜系\t做法\t特色\t主料\turl')#写入标题栏
    output.write('\t'*22)#使内容对齐
    #output.write('辅料\n')#写入标题栏
    
    for i in range(len(total_url)):
         for j in range(len(total_url[i])):
            for k in range(len(total_url[i][j])):
                url2=total_url[i][j][k]
                response = requests.get(url2)#逐个访问网页，获得数据
                response.encoding = "utf-8" #设置接收编码格式
                get_info(response,output,dish,i,url2)#处理数据，提取信息
    output.close()#关闭文件

time_start = time.time()#记录程序开始时间


url_iters(10,Dishkeys)
spider(Dishval)#进行提取处理并导出

duration = 1000#提示音时长，1000毫秒 = 1秒
freq = 440 #提示音频率
time_end=time.time()#记录程序结束时间
print('totally cost',time_end-time_start)#打印程序运行时间
winsound.Beep(freq,duration*10) #响铃提示程序结束