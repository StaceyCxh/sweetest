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

## 四、元素定位
在excel中书写元素定位信息，将元素定位与代码分隔开，方便维护，可读性高。

![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/%E5%85%83%E7%B4%A0%E5%AE%9A%E4%BD%8D%E8%A1%A8.png)

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">字段</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">说明</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">page/页面</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">元素所在页面<br>所有页面通用的元素（如title等 ）可放于页面“通用”下面</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">element/元素</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">需定位进行操作的元素，不同page下的元素可同名</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">by/定位方式</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">定位方式，常用的有id、name、xpath等</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">value/定位值</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">定位值</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">custom/自定义</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">若元素在frame/iframe中，则填写相应的frame id或frame name</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">remark/备注</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">注释说明</font></td>
	</tr>
</table>

变量定位法：
- 元素定位表中element最后带#号，value的值中带#号
- 测试用例中element带上具体变量值
- 代码在进行元素定位时，自动把变量值填充到定位值相应的位置中

举例：

元素定位表设计：
<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">by</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">value</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">百度搜索页面</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">搜索结果#</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">xpath</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">//*[@id="#"]/h3/a</font></td>
	</tr>
</table>

测试用例设计：
<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">点击</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">百度搜索页面</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">搜索结果#1</font></td>
	</tr>
</table>

则最终代码进行元素定位时，使用的是：find_element_by_xpath('//*[@id="1"]/h3/a')



