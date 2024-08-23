## 简介

在护网时，需要对恶意IP进行封禁，但有时候一些IP不能封禁，如负载均衡IP、CDN IP，对于这些IP封禁后可能会影响业务，所以需要对需要封禁的IP进行白名单过滤，对于批量需要封禁的IP手动筛查麻烦又费力，**IP WhitePass** 是一个旨在解决批量过滤的小工具

**功能特色**

+ 支持网段格式，如`122.194.278.0/24`

+ 支持IPV6，以及IPV6网段格式，如`2001:0db8:85a3:0000:0000:8a2e:0370:7334/56`
+ 支持IP过滤后高亮显示（将过滤掉的IP进行高亮显示，方便查看）
+ 支持IP去重
+ 支持从Excel文件中读取IP进行过滤
+ 支持自动复制（过滤后自动将结果复制到粘贴板）
+ 支持监控粘贴板，开启后将自动读取复制的IP并进行自动过滤（不稳定，不推荐使用）

## 版本

经过几个版本迭代，提供了以下两个版本，功能一致，只是底层不同

+ V2.2版本：需要将白名单IP放入`whitelist.txt`中进行过滤
+ V3.1版本：不在采用文件读写的方式，底层使用SQLlite数据库进行存储白名单IP，提高性能

两个版本功能一致，只是习惯原因，如果习惯在文件中直接打开加入白名单可以使用V2.2版本，如果不喜欢文件操作，喜欢简洁一些，选择V3.1版本即可

## 使用演示

### V2.2版本使用演示

文件配置如下：

+ config.ini：配置文件
+ whitelist.txt：白名单文件
+ WhitePass.exe：主程序

先打开`whitelist.txt`将白名单IP添加进去

![image-20240823190838548](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231908577.png)

再打开`WhitePass.exe`进行操作即可（注：修改文件后需要重新打开主程序）

**过滤功能**

将待过滤IP输入在左边输入框中，点击底部`Filter IPs`即可过滤，效果如图

![image-20240823191207947](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231912016.png)

**IP去重功能**

点击输出IP去重，即可对输出的IP结果进行去重处理，也可以点击`开启自动去重`按钮，所有结果将自动去重

![image-20240823191348136](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408240133087.png)

**高亮IP功能**

点击`排序IP并高亮`，已经被过滤掉的功能将在左侧显示

![image-20240823191442220](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231914288.png)

**添加白名单**

会将IP添加到`whitelist.txt`中

![image-20240823191628815](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231916880.png)

**从Excel文件中读取IP**

只能读取第一列，从第一列中读取IP到待过滤区域

**监控剪切板**

开启后将自动检测复制到的IP，会抢占粘贴板，不推荐使用

![image-20240823191853670](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231918733.png)



### V3.1版本使用演示

文件配置如下：

+ config.ini：配置文件
+ WhitePass.exe：主程序
+ white_ips.db：运行后产生的数据库文件，无需操作该文件

**操作白名单IP**

现在所有添加、删除、查看白名单等一些操作均在此操作

![image-20240823192159175](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231921238.png)

可供操作：

![image-20240823192227717](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231922775.png)

**插入**

插入有三种：

+ 直接插入，在输入框中插入，选择`插入白名单IP`按钮即可
+ 从txt插入白名单IP：和文件插入一样的格式
+ 从Excel插入白名单IP：第一列为IP，第二列可对IP添加描述

**查看白名单**

![image-20240823192451946](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231924008.png)

**导出白名单**

会导出到程序根目录下的`whitelit.csv`文件

![image-20240823192508371](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231925431.png)

![image-20240823192549764](https://yunyinanquan.oss-cn-beijing.aliyuncs.com/202408231925817.png)

其他功能操作同V2.2版本





















