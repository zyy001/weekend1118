#1.之前的resdcsv文件不能被其他测试调用,所以给这段代码封装到一个方法里
#2.每个测试用例的路径不同,所以path应该作为参数传入这个方法中
#3.我们打开了一个文件,但是并没有关闭,最终可能会造成内存泄露
import csv
import os


def read(file_name):
    #所有重复代码的出现,都是程序设计的不合理
    #重复代码应该封装到一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/"+file_name)
   # file=open(path,'r')
    #因为file文件一旦关闭里面的数据也随之消失,所以单独声明一个列表result,来保存里面的数据
    result=[]
    with open(path,'r') as file:
        data_table=csv.reader(file)
        for row in data_table:
            #把遍历的数据都添加到result里
            result.append(row)
    return result
#如果在打开和关闭程序的代码之间发生了异常,导致后面的代码不能正常执行,file.close()也不能执行,这时文件仍然不能关闭,应该用with...as...语句实现文件的关闭
        #with代码块可以自动关闭with中声明的变量file
    #file.close()
if __name__ == '__main__':
    #path = r"C:\Users\51Testing\PycharmProjects\weekend1118\data\member_info.csv"
#3.这个路径是绝对路径,我们工作中一个项目不止一个人编写代码,所以应该在代码中,通过当前代码文件的路径,根据相对路径,找到csv文件,所以首先要找到当前文件的路径
#os是操作系统,path是路径,dir是directory目录__file__是python内置的变量,是指当前文件
    #我们真正想要的是csv文件路径
#print(path)
    member_info=read('member_info.csv')
    print(member_info)
#5.读出数据不是目的,目的是通过数据驱动测试,所以应该把数据作为方法的返回值方便进一步调用
