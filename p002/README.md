# 1、响应数据解密DES

![Snipaste_2024-09-23_22-34-01](images/Snipaste_2024-09-23_22-34-01.png)



![Snipaste_2024-09-23_22-36-45](images/Snipaste_2024-09-23_22-36-45.png)

# 2、解密过程混淆

![Snipaste_2024-09-23_22-37-55](images/Snipaste_2024-09-23_22-37-55.png)

完成基本解密 之后 调试发现需要  补充环境    userAgent

~~~javascript
//补环境
navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
~~~



![Snipaste_2024-09-23_22-40-38](images/Snipaste_2024-09-23_22-40-38.png)



![Snipaste_2024-09-23_22-43-15](images/Snipaste_2024-09-23_22-43-15.png)

因为是混淆情况下，不方便使用  crypto-js构造解密方法，可以直接copy 混淆的代码 进行执行
