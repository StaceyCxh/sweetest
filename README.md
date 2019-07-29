# sweetest
#### 基于喜文测试-sweetest，进行重构后的自动化测试框架，同时支持 Web UI、Http 接口、Android/IOS等自动化测试。

## 一、背景
测试自动化是软件行业一个不可逆转的趋势，目前大多数自动化测试采用录制回放或直接调用selenium/appnium接口来编写测试代码的方式实现，主要存在以下不足：
- 代码即用例，用例越多，代码量越大，维护越困难；
- 受UI变化影响大，测试对象的页面结构变化，需要修改对应的代码；
- 对编码能力要求高；

为了解决以上问题，sweetest应运而生，有以下特点：
- 用例与代码隔离、元素定位与代码隔离；
- 在 Excel 中以文本编写测试用例；
- 元素定位表格化，采用“变量定位法”；
- 使用简单，没有编码基础也能快速上手；

## 二、方案
- 开发语言：python3
- 底层工具：selenium + unittest
- 用例工具：excel
- 报告模式：excel、html
- 日志模式：log
- 错误截图：png
- 消息通知：钉钉群消息、邮件
- 快速使用：
    - 在element/XX-Elements.xlsx文件中书写测试页面中各测试元素的定位信息；
    - 在testcase/XX-TestCase.xlsx文件中书写测试用例；
    - 若有全局变量，可保存在data/XX-YY.csv文件中；
    - 可在sweetest/config.py文件中修改邮件及钉钉相关配置信息；
    - 修改sweetest/globals.py文件中的g.project_name(项目名称)、g.sheet_name（本次需执行的测试用例集）、g.conditions(用例筛选条件)及环境信息（平台、浏览器）; 
    - 运行start.py启动本次自动化测试；

## 三、目录结构
![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)

<table cellspacing="0" border="0">
	<colgroup width="148"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">目录</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">说明</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="left" valign=middle><font face="Calibri,DejaVu Sans" color="#000000">data<br>&nbsp;&nbsp;xx.csv</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">测试数据，文件名称格式为：project_name-sheet_name.csv <br>每个testsuite对应一份数据文件</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="38" align="left" valign=middle><font face="宋体" color="#000000">element<br>&nbsp;&nbsp;xx.xlsx</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>元素定位表，文件名称格式为：project_name-Elements.xlsx</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="left" valign=middle><font face="宋体" color="#000000">testcase<br>&nbsp;&nbsp;xx.xlsx</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>测试用例，文件名称格式为：project_name-Testcase.xlsx<br>excel文件中每个sheet相当于testsuite</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="38" align="left" valign=middle><font face="宋体" color="#000000">template<br>&nbsp;&nbsp;Template.html</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>Html格式测试报告的模板</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="68" align="left" valign=middle><font face="宋体" color="#000000">report<br>&nbsp;&nbsp;xx.xlsx</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">Excel格式测试报告，每次自动化测试结束后自动生成一份，名称格式为：project_name-Report@yyyymmdd_HHMMSS.xlsx<br>report目录可以不存在，程序运行后会自动创建</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="68" align="left" valign=middle><font face="宋体" color="#000000">htmlreport<br>&nbsp;&nbsp;xx.html</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">Html格式测试报告，每次自动化测试结束后自动生成一份，名称格式为：project_name-Report@yyyymmdd_HHMMSS.html<br>htmlreport目录可以不存在，程序运行后会自动创建</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="62" align="left" valign=middle><font color="#000000">log<br>&nbsp;&nbsp;xx.log</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>运行日志，每次自动化测试会自动生成一份，名称格式为：yyyymmdd_HHMMSS.log<br>log目录可以不存在，程序运行后会自动创建</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="62" align="left" valign=middle><font color="#000000">snapshot<br>&nbsp;&nbsp;xx.png</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>错误截图图片，文件名称格式为：project_name-sheet_name-yyyymmdd_HHMMSS#testcase_title-testcase_step.png<br>snapshot目录可以不存在，程序运行后会自动创建</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="left" valign=middle><font face="Calibri,DejaVu Sans">requirements.txt</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>依赖包清单</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="left" valign=middle><font face="Calibri,DejaVu Sans">start.py</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>启动文件</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="left" valign=middle><font face="Calibri,DejaVu Sans">sweetest</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>主程序代码</td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-left: 1px solid #000000" height="24" align="left" valign=middle><font face="Calibri,DejaVu Sans">&nbsp;&nbsp;keywords</font></td>
		<td style="border-top: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>关键字</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" height="24" align="left" valign=middle><font color="#000000">&nbsp;&nbsp;lib</font></td>
		<td style="border-right: 1px solid #000000" align="left" valign=middle>辅助模块</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" height="68" align="left" valign=middle><font color="#000000">&nbsp;&nbsp;config.py</font></td>
		<td style="border-right: 1px solid #000000" align="left" valign=middle>配置文件<br>配置关键字、文件名后缀、元素/用例属性的中英文对照、元素超时时间、页面刷新超时时间、钉钉及邮件相关信息等</td>
	</tr>
	<tr>
		<td style="border-left: 1px solid #000000" height="68" align="left" valign=middle><font color="#000000">&nbsp;&nbsp;globals.py</font></td>
		<td style="border-right: 1px solid #000000" align="left" valign=middle>全局变量文件<br>定义浏览器对象、测试项目名称、要执行的测试用例集名称、环境配置信息、用例筛选条件等 </td>
	</tr>
	<tr>
		<td style="border-bottom: 1px solid #000000; border-left: 1px solid #000000" height="24" align="left" valign=middle><font color="#000000">&nbsp;&nbsp;autotest.py</font></td>
		<td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle>测试类</td>
	</tr>
</table>

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
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>元素所在页面<br>所有页面通用的元素（如title等 ）可放于页面“通用”下面</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">element/元素</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>需定位进行操作的元素，不同page下的元素可同名</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">by/定位方式</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>定位方式，常用的有id、name、xpath等</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">value/定位值</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>定位值</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">custom/自定义</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>若元素在frame/iframe中，则填写相应的frame id或frame name</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">remark/备注</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>注释说明</font></td>
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

在excel中书写测试用例，将测试用例与代码分隔开，方便维护，可读性高。

excel文件中每个表单表示1个测试用例集，表单名sheet_name是测试用例集名称（test_suite）; 
执行哪些测试用例集，需要在globals.py中指定g.sheet_name;

- sheet_name是str字符串，支持多种匹配方式
    - ^放开头，表示以此值开头；
    - $放结尾，表示以此值结尾；
    - *放开头或结尾，表示模糊匹配；
    - 非^ *开头，非$ *结尾，表示精确匹配；
- sheet_name是list列表，则excel表单名在列表中的用例都需要执行；

![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B.png)

<table cellspacing="0" border="0">
	<colgroup width="143"></colgroup>
	<colgroup width="482"></colgroup>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="18" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">字段</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#ADC5E7"><font color="#000000">说明</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">id/用例编号</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>用例/用例片段的id</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">title/用例标题</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>用例/用例片段的名称</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">condition/前置条件</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>取值：base、end、setup、teardown、snippet</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">step/测试步骤</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>测试执行步骤的编号 <br>所编号前可用逻辑控制符号，取值：^、&gt;、&lt;</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">keyword/操作</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>测试操作/关键字</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">page/页面</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>测试元素所在页面<br>为空时，自动沿用上个步骤的page值</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">element/元素</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">必填字段<br>需进行操作的元素，不同page下的元素可同名</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">data/测试数据</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>测试数据，用键值对表示<br>多个data用 英文逗号 或 双英文逗号 隔开</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">expected/预期结果</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>预期结果，用键值对表示<br>为空时，则data列充当expected的内容</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">output/输出数据</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>输出数据，用键值对表示</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">priority/优先级</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>测试用例的优先级，取值：H/高、M/中、L/低</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">designer/设计者</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>测试用例设计者名称</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">flag/自动化标记</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>标记是否是自动化测试用例<br>值为Y，表示是自动化测试用例<br>值为N，表示不是自动化测试用例<br>值为空，默认为自动化测试用例</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">score/步骤结果</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>测试步骤的执行结果记录</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">result/用例结果</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>测试用例的执行结果记录</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="24" align="center" valign=middle><font color="#000000">remark/备注</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000">选填字段<br>注释说明</font></td>
	</tr>
</table>

- 前置条件 / condition
    - base：相当于setUpClass，每个用例集前执行一次; 
    - end：相当于tearDownClass，每个用例集后执行一次; 
    - setup：相当于setUp，每个用例前执行一次; 
    - teardown：相当于tearDown，每个用例后执行一次; 
    - snippet：共用的用例片段，可供调用; 

- 测试步骤 / step
    - ^：相当于if语句; 
    - <：相当于else语句;
    - \>：相当于then语句;
      
- 测试数据 / data
    - 可为空; 
    - data中以=分隔键值对; 
    - 多个data用 英文逗号 或 双英文逗号 隔开; 
    - 若data中本身带有英文逗号，需转义\; 
    - 若data中没有=号，直接赋值给text; 
    - data中可带变量，用<>括起部分为变量；
    - data中直接带+、-、*、/、%、(、)、<、>，即运算符 和 变量定界符，需转义；
    - data中+、-、*、/、%、(、)左边或右边字符 非数字，也可不转义；
    - data中可以带按键操作，如：text=<Keys.ENTER>、<Keys.CONTROL\,'a'>；
    - data中可带运算表达式，代码自动执行计算;
    - data中可带list，支持或模糊匹配；
      
      举例说明：
      - key=['v1'\,'v2'\,'v3']，则检查key=v1 或 key=v2或 key=v3都表示用例通过；
      - key=['^v'\,'v$'\,'*a'\,'v4']，则检查key 以v开头 或 以v结尾 或 包含a 或 等于v4 都表示用例通过；
    - data中设置等待时间=x，可强制先等待x秒再执行操作；
    
- 预期结果 / expected
    - 测试数据(data)为空时，可以将预期结果（expected）放在测试数据(data)列
    - 满足测试数据(data)的一切规则
    - 支持多种匹配方式
        - ^放开头，表示以此值开头
        - $放结尾，表示以此值结尾
        - *放开头或结尾，表示模糊匹配
        - 非^ *开头，非$ *结尾，表示精确匹配
        
- 输出数据 / output
    - 以=分隔键值对，key是自定义的变量，value是具体值; 
    - 若value为text，则取element的text值赋值给变量key；
    - value中可带变量，用<>括起部分为变量；
    - 若value中带变量，则将替换变量后的value值赋值给变量key；
    - 若value中不带变量、且不为text，则取element对应的属性值赋值给变量key；
    
- 元素 / element
    - 多个element用 | 隔开，比如拖拽操作涉及2元素；
    - element中可带变量，用<>括起部分为变量；
    - element中带#号，表示写用例时，后面需带元素定位值；
    - element可为用例片段ID（用例片段ID以"SNIPPET"开头）；


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
- open /打开 关键字对应的元素可以为 浏览器 或 browser,表示打开浏览器；
- open /打开 关键字对应的其它元素 必须定义在“通用”page下；
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
- 检查时可以使用多种匹配方式：
    - ^放开头，表示以此值开头；
    - $放结尾，表示以此值结尾；
    - *放开头或结尾，表示模糊匹配；
    - 非^ *开头，非$ *结尾，表示精确匹配；
- 若用例中data/expected列是列表，则支持“或”模糊匹配，举例如下：
    - key=['v1','v2','v3']，则检查key=v1 或 key=v2或 key=v3都表示用例通过；
    - key=['^v','v$','*a','v4']，则检查key 以v开头 或 以v结尾 或 包含a 或 等于v4 都表示用例通过；

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
- 测试用例中可以把公共部分单独抽离出来定义为用例片段（ID以"SNIPPET"开头），后续可使用execute / 执行 关键字调用用例片段；
- 用例片段中的测试数据可以先用变量赋值，外层用例执行用例片段时再把具体的变量值放在用例data列传进去；
- 可设置用例片段循环执行次数：
    - 用 SNIPPET_ID 表示运行1次用例片段；
    - 用 SNIPPET_ID*N 表示循环运行N次用例片段； 
- 可设置用例片段循环结束条件：循环结束条件=成功、condition=pass、循环结束条件=失败、condition=fail；
- 循环结束条件 优先级高于 循环执行次数：
    - 只要满足循环结束条件，即使未到达循环执行次数，也结束循环；
    - 若到达循环执行次数，但没有满足循环结束条件，则结束循环；
- 可设置中断测试策略：
    - 用 SNIPPET_ID*N* 表示某次循环失败后继续运行; 
    - 用 SNIPPET_ID*N 表示某次循环失败后直接退出；
- 允许嵌套调用用例片段；
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
- message / 对话框 关键字，对应的page=通用，element取值：确认、取消、关闭、输入; 
- prompt弹窗的输入操作，会自动点击确认按钮，故无需再写确认步骤；

#### 17、close / 关闭

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
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">关闭</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000"></font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">标签页</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">关闭</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="left" valign=middle><font color="#000000"></font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000">浏览器</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="46" align="center" valign=middle><font color="#000000"></font></td>
	</tr>
</table>

注意：
- close /关闭 关键字对应的元素可以为 浏览器 或 browser,表示关闭浏览器；
- close /关闭 关键字对应的元素可以为 标签页 或 tab,表示关闭浏览器；


## 七、外部数据文件

- csv格式文件；
- 可存放全局变量；
- 最后字段!=flag：变量值全部读取使用；
- 最后字段=flag：本次测试读取flag!=Y的变量值使用，读取值后置flag=Y，下次自动化测试时不再使用该值，适用于数据需唯一的场景；需及时维护添加数据；
- 若最后字段=flag且不存在flay!=Y的记录，则本次测试没有数据可以使用，用例执行会失败；


## 八、页面/窗口管理 

- 打开(open) / 点击(click) / 双击(double_click) 操作若有新开窗口，将注册新窗口(将页面名字与窗口句柄绑定)；
    - 如果有提供新页面名字，则使用该名字，否则使用默认名字：HOME; 
    - 若存在同名窗口（页面名字相同，但窗口句柄不同），则关闭旧窗口，将页面名字与当前窗口绑定；
- 测试步骤中的非 对话框(message) 操作，会判断是否需要窗口切换；
    - 测试步骤中的 页面(page) 未绑定任何窗口，则绑定到当前窗口，不进行窗口切换；
    - 测试步骤中的 页面(page) 已绑定当前窗口，则不进行窗口切换；
    - 测试步骤中的 页面(page) 已绑定已有窗口且非当前窗口，则进行窗口切换；
- 页面“通用”是不绑定到任何窗口的，相关的测试步骤是直接在当前窗口操作的；


## 九、测试报告
![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/excel%E6%8A%A5%E5%91%8A1.png)

![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/excel%E6%8A%A5%E5%91%8A2.png)

![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/html%E6%8A%A5%E5%91%8A.png)


## 十、消息通知
![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/%E9%92%89%E9%92%89%E7%BE%A4%E9%80%9A%E7%9F%A5.png)

![image](https://github.com/StaceyCxh/sweetest/blob/master/sweetest/img/%E9%82%AE%E4%BB%B6%E9%80%9A%E7%9F%A5.png)


## 十一、测试结果数据接口

```
result = AutoTest.get_result()

print(result)

Output:

{
    "testAll": 6,                           #测试用例总数
    "testPass": 3,                          #测试通过的用例数
    "testFail": 0,                          #测试失败的用例数
    "testSkip": 3,                          #测试跳过的用例数
    "beginTime": "2019-06-12 16:43:31",     #测试开始时间
    "totalTime": "80.51s",                  #测试时长
    "testResult": [                         #测试结果
    {
            "testsuite": "baidu",           #测试用例集
            "testcases": [                  #测试用例
            {
                    "id": "BAIDU_001",                   #用例ID
                    "title": "搜索：自动化测试",            #用例标题
                    "result": "成功",                     #用例结果
                    "setup": {                           #用例准备工作（即setup用例内容）
                        "id": "HOME_001",
                        "title": "打开百度",
                        "result": "Pass",
                        "steps": [
                            {
                                "control": "",
                                "no": "1",
                                "keyword": "EXECUTE",
                                "page": "用例片段",
                                "element": "SNIPPET_003",
                                "data": {},
                                "expected": {},
                                "output": {},
                                "score": "OK",
                                "remark": "",
                                "custom": "",
                                "snippets": [
                                ]
                            }
                        ]
                    },
                    "steps": [
                        {
                            "control": "",                      #测试步骤逻辑控制符（if、else、then）
                            "no": "1",                          #测试步骤
                            "keyword": "INPUT",                 #关键字
                            "page": "百度搜索页面",               #测试页面
                            "element": "百度搜索页面^搜索框",      #测试元素    
                            "data": {                           #测试数据
                                "text": "自动化测试",
                                "text1": ""
                            },
                            "expected": {},                     #预期结果
                            "output": {},                       #输出数据
                            "score": "OK",                      #执行结果
                            "remark": "",                       #备注说明
                            "custom": ""                        #frame信息
                        },
                        {...},
                        ... 
                    ],
                    "teardown": {                           #用例清理工作（即teardown用例内容）
                        "id": "HOME_002",
                        "title": "打开百度",
                        "result": "Pass",
                        "steps": [
                            {
                                "control": "",
                                "no": "1",
                                "keyword": "EXECUTE",
                                "page": "用例片段",
                                "element": "SNIPPET_003",
                                "data": {},
                                "expected": {},
                                "output": {},
                                "score": "OK",
                                "remark": "",
                                "custom": "",
                                "snippets": [
                                ]
                            }
                        ]
                    },
            },
            {...},
            ...
    }
    {       "testsuite": "baidu",           #测试用例集
            "testcases": [  ]                #测试用例
    }]
}
```

## 十二、致谢

sweetest重构工具的产生，是在开源项目 喜文测试-sweetest 的基础上扩展、优化(功能上只有少数变化，更多的是代码细节的修改、源码中有注释)，受益匪浅，非常感谢！
- 喜文测试-sweetest: https://github.com/tonglei100/sweetest/