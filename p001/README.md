# 1、请求头部参数加密MD5

可以根据关键字搜索；或者hook  JSON.stringify()进行定位

![Snipaste_2024-09-23_21-49-58](images/Snipaste_2024-09-23_21-49-58.png)

![Snipaste_2024-09-23_21-52-33](images/Snipaste_2024-09-23_21-52-33.png)

进入到  f.getSign()

![Snipaste_2024-09-23_21-54-53](images/Snipaste_2024-09-23_21-54-53.png)

通过简单的s("1")   此时已经确定s()是md5加密函数，不必再进入s()函数，

# 2、响应数据解密AES

![Snipaste_2024-09-23_21-56-53](images/Snipaste_2024-09-23_21-56-53.png)

通过descrypt(  进行全局搜索；或者hook JSON.parse()进行定位

![Snipaste_2024-09-23_22-00-12](images/Snipaste_2024-09-23_22-00-12.png)



![Snipaste_2024-09-23_22-02-19](images/Snipaste_2024-09-23_22-02-19.png)

![Snipaste_2024-09-23_22-04-01](images/Snipaste_2024-09-23_22-04-01.png)
