# sweetest
#### 基于喜文测试-sweetest，进行重构后的自动化测试框架，同时支持 Web UI、Http 接口、Android/IOS等自动化测试。

## 一、背景
测试自动化是软件行业一个不可逆转的趋势，目前大多数自动化测试采用录制回放或直接调用selenium/appnium接口来编写测试代码的方式实现，主要存在以下不足：
- 代码即用例，用例越多，代码量越大，维护越困难；
- 受UI变化影响大，测试对象的页面结构变化，需要修改对应的代码；
- 对编码能力要求高；

为了解决以上问题，sweetest应运而生，有以下特点：
- 用例与代码隔离、元素定位与代码隔离
- 在 Excel 中以文本编写测试用例
- 元素定位表格化，采用“变量定位法”
- 使用简单，没有编码基础也能快速上手

## 二、方案
- 开发语言：python3
- 底层工具：selenium + unittest
- 用例工具：excel
- 报告模式：excel、html
- 日志模式：log
- 错误截图：png

## 三、目录结构
![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)

## 四、元素定位表

