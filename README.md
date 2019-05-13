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

## 五、测试用例



## 六、关键字 / keyword / 操作

#### 1、open / 打开

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">打开</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">通用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">百度搜索链接</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">标签页名=百度搜索页面,,清理缓存=是,,打开方式=新标签页</font></td>
	</tr>
</table>

注意：
- open /打开 关键字对应的元素必须定义在“通用”page下；
- 可以设置打开的页面名称：标签页名=xxx、新窗口=xxx、tabname=xxx，该新页面的元素则定义在该page下；
- 可以设置清缓存：清理缓存=是、cookie=yes；
- 可以设置在浏览器中新开tab打开链接：打开方式=新标签页、mode=tab；
- 可以设置新开浏览器窗口打开链接：打开方式=新浏览器、mode=browser；

#### 2、检查 / check

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">检查</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">百度搜索页面</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">页面title</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">百度一下，你就知道</font></td>
	</tr>
</table>

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">检查</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">首页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">欢迎文案</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">text=欢迎</font></td>
	</tr>
</table>

注意：
- check / 检查 关键字用于配合做结果断言检查；
- 常用于检查跳转页面title是否正确、某元素的text属性是否正确等 ；
- 若用例中data列有值，则取data列的值做检查；否则取expected列的值做检查；
- 检查时可以使用多种匹配方式：^放开头，表示以此值开头；$放结尾，表示以此值结尾；*放开头或结尾，表示模糊匹配；非^ *开头，非$ *结尾，表示精确匹配；

#### 3、输入 / INPUT

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">输入</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">登录页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">账号</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">tester</font></td>
	</tr>
</table>

注意：
- 代码默认先清空文本再输入对应内容；
- 可以设置不清空文本：清除文本=否、clear=no
- 可以输入文本：tester
- 也可以进行按键操作：<Keys.ENTER>、<Keys.CONTROL,'a'>

#### 4、点击 / CLICK

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">点击</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">登录页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">登录按钮</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- click / 点击 关键字，通常用于操作按钮或链接文字；
- 点击操作若会打开新页面/新窗口，可以设置新页面/新窗口的名称：标签页名=xxx、新窗口=xxx、tabname=xxx，该新页面的元素则定义在该page下；

#### 5、右击 / CONTEXT_CLICK

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">右击</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">列表页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">操作列</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- context_click / 右击 关键字，通常用于操作按钮或链接文字；

#### 6、双击 / DOUBLE_CLICK'

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">双击</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">列表页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">图片</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- double_click / 双击 关键字，通常用于操作按钮或链接文字；
- 双击操作若会打开新页面/新窗口，可以设置新页面/新窗口的名称：标签页名=xxx、新窗口=xxx、tabname=xxx，该新页面的元素则定义在该page下；

#### 7、移动到 / MOVE

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">移动到</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">列表页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">名称</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- move / 移动到 关键字，通常用于鼠标悬浮于某元素上、显示更多内容的场景；

#### 8、拖拽 / DRAG AND DROP

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">拖拽</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">列表页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">记录1|记录2</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- drag and drop / 拖拽 关键字，常用于将元素移动到另一元素处；
- 测试用例中element列使用|号分隔开多个元素；

#### 9、滑动 / SWIPE

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">滑动</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">解锁页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">滑动条</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">x=500,,y=100</font></td>
	</tr>
</table>

注意：
- swipe / 滑动 关键字，常用于拖动元素移动一段距离；

#### 10、刷新 / REFRESH

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">刷新</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">列表页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意:
- refresh / 刷新 关键字，常用于刷新当前页面；

#### 11、获取 / OBTAIN

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">output</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">获取</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">列表页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">名称</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">name=text</font></td>
	</tr>
</table>

注意：
- obtain / 获取 关键字，常用于获取元素某些属性值，以便进行结果检查；
- 获取的值保存在用例output列的变量中；
- 应用场景：新建用户后，获取列表中该新记录的“名称”字段值，与新建时的输入作对比检查；

#### 12、判断 / JUDGE

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">判断</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">首页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">欢迎文案</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- judge / 判断 关键字，常用于检查元素是否存在/不存在; 
- 用例中data列为空，则默认判断元素是否存在；
- 可设置判断元素是否不存在：存在=否、exist=no

#### 13、脚本 / SCRIPT

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">脚本</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">通用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">window.alert('这是一个测试Alert弹窗');</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- script / 脚本 关键字，常用于执行Js脚本；
- js脚本写在用例element列；

#### 14、调用 / CALL

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">output</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">调用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">通用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	    <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">mytime=time.getTime()</font></td>
	</tr>
</table>

注意：
- call / 调用 关键字，常用于调用自定义方法；
- 具体调用的方法，写在用例中output列，以 模块.方法 的格式进行调用，模块必须位于sweetest.lib目录下；
- 应用场景：在测试用例中获取当前时间作为测试数据；

#### 15、执行 / EXECUTE

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">执行</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">用例片段</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">SNIPPET_001</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">name=tester,,pwd=123456</font></td>
	</tr>
</table>

注意：
- 测试用例中可以把公共部分单独抽离出来定义为用例片段，后续可使用execute / 执行 关键字调用用例片段；
- 用例片段中的测试数据可以先用变量赋值，外层用例执行用例片段时再把具体的变量值放在用例data列传进去；
- 可设置用例片段循环执行次数：用 SNIPPET_ID 表示运行1次用例片段；用 SNIPPET_ID*N 表示循环运行N次用例片段； 
- 可设置用例片段循环结束条件：循环结束条件=成功、condition=pass、循环结束条件=失败、condition=fail；
- 循环结束条件 优先级高于 循环执行次数：只要满足循环结束条件，即使未到达循环执行次数，也结束循环；若到达循环执行次数，但没有满足循环结束条件，则结束循环；
- 可设置中断测试策略：用 SNIPPET_ID*N* 表示某次循环失败后继续运行，否则某次循环失败后直接退出；
- execute / 执行 关键字还可以用于变量赋值，变量可用于后续的测试数据中；

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">执行</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">通用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">变量赋值</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">name=tester,,pwd=123456</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">输入</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">登录页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">用户名</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">&lt;name&gt;</font></td>
	</tr>
</table>

#### 16、对话框 / MESSAGE

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">对话框</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">通用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">确认</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">keyword</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">page</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">element</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">data</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">对话框</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">通用</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">输入</font></td>
        <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">审核通过</font></td>
	</tr>
</table>

注意：
- web测试过程中经常会遇到弹窗，包括alert、confirm、prompt弹窗；
- message / 对话框 关键字，对应的page=通用，element取值：确认、取消、关闭、输入
- prompt弹窗的输入操作，会自动点击确认按钮，故无需再写确认步骤；






