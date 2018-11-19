'''
001、测试机器的磁盘太小，经常报警，要写一个清理日志的脚本，每次运行就把三天之前的日志删除，日志名的格式是xxx-20170623.log。

读取文件夹内的所有文件名
将文件名解析为日期
判断日志是否距离当前日期三天
如果是删除
'''
from datetime import datetime
from datetime import timedelta
import os

class logCleaner():
    def test_init(self,dir):
        # 获取距离现在15天的所有日期，保存到list中
        today = datetime.today()
        for i in range(15):
            d = today - timedelta(days=i)
            file_name = 'log'+str(d.year)+str(d.month).zfill(2)+str(d.day).zfill(2)+'.log'
            open(os.path.join(dir,file_name),'w')

    def set_dir(self,path):
        self.path = path

    def start_clean(self):
        # 获取所有的文件名
        # 这里我们也可以采用print(os.listdir(r'D:\study\someIntresting\001日志清理\logs'))的方式，但是listdir会将文件夹的名称也获取下来
        file_list = list(os.walk(self.path))[0][2]
        for file_name in file_list:
            if self.is_needed_log(log_name=file_name) == False:
                os.remove(os.path.join(self.path,file_name))

    def is_needed_log(self,log_name):
        # 获取文件名中的文件名log20181118.log
        log_name = log_name[3:-4]
        # 将文件名转化为时间
        d1 = datetime.strptime(log_name,'%Y%m%d')
        # 获取当前时间
        d2 = datetime.today()
        # 获取时间差
        day = (d2 - d1).days
        # 判断文件时间-当前时间是否大于3，如果是返回False，如果否，返回True
        if day >= 2:
            return False
        else:
            return True


if __name__ == '__main__':
    path = r'D:\study\someIntresting\001日志清理\logs'
    lc = logCleaner()
    lc.test_init(dir=path)
    lc.set_dir(path)
    lc.start_clean()


