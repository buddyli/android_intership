android_intership
=================

android实训项目服务器端代码

1,本工程使用Python开发， 后台的数据使用的MongoDB。因此如果想要运行本程序，需要安装Python2.7和MongoDB。
2，连接数据库。本地启动mongodb数据库之后，需要修改程序连接数据的字符串，位置在model/__init__.py，中，直接修改IP地址和端口号即可。
3,本工程依赖了若干Pyhon第三方的库。请在本地先安装pip，然后使用pip install 安装bottle, marko, pymongo, mongoengine四个依赖包。
4,上述步骤都执行完毕后，执行代码根目录下的index.py文件，服务器默认使用的端口号是8888。启动后，浏览器访问https://localhost:8888即可。

任何疑问，请联系，李传宝，15210078395, 13126092@bjtu.edu.cn, QQ:381885958
