#在线校验模块By_LixVer
#引用 requests, os, socket, getpass, time文件
import requests, os, socket, getpass, time
print('欢迎使用LixVer联网校验系统')
print('下面是联网验证线路')
print('1.海外Github')
print('2.大陆托管服务器(暂不可用)')
choice=int(input('请选择线路:'))
os.system('cls')
print('开始线路测速...')
if choice == 1:
    ping=os.system('ping -n 1 raw.githubusercontent.com')
    if ping == 0:
        print('海外线路测速成功...')
        time.sleep(3)
        os.system('cls')

        #校验文件地址
        Download_addres='https://raw.githubusercontent.com/LixVer/CloudCertificate/main/Certificate.txt'
        #把校验文件地址发送给requests模块
        f=requests.get(Download_addres)
        #下载校验文件到本地
        with open("Certificate.txt","wb") as code:
             code.write(f.content)
        # 获取当前系统主机名
        host = socket.gethostname()
        # 获取当前系统用户名
        user = getpass.getuser()
        # 拼接形成识别码
        se = host + "_" + user
        certificate = str(se)                      #定义certificate为识别码变量
        #输出设备识别码到屏幕
        print('本设备识别码--> %s' % certificate)
        #将设备识别码与校验文件对比
        def check_string():
            with open('Certificate.txt') as certificate_f:
                datafile = certificate_f.readlines()
            for line in datafile:
                if certificate in line:
                    return True # The string is found
            return False  # The string does not exist in the file
        #校验成功执行后面内容
        if check_string():
            os.remove("Certificate.txt")
            print('True,联网验证成功,该设备已授权')
        
        
        #主程序
        
        
        
        
            input()
        #校验失败直接跳转到程序结束
        else:
            os.remove("Certificate.txt")
            print('Flase,联网验证失败,该设备未授权')
            input()        
        
        
        
           
    else:
        print('海外测速失败...')    
        print('请按回车关闭重新启动并选择线路')      
        input()
    
elif choice == 2:
    ping=os.system('ping -n 1 127.0.0.1')
    if ping == 0:
        print('大陆线路测速成功...') 
        
        
        
        
        
          
    else:
        print('大陆测速失败...')    
        print('请按回车关闭重新启动并选择线路') 
        input()           
        



input()
