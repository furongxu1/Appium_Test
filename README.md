# Appium_Test  
## 项目简介：
框架使用Pytest 运行 Yaml 来驱动 Appium 进行 AppUI 自动化测试，该框架实现了用例失败自动截图功能，自动生成allure报告以及自动邮件发送测试报告。 
## 目录结构介绍：
**Base_Obj：** appium基础定位方法目录

**Page_Obj:** 页面元素目录，使用Page Object模式将页面定位和业务操作分开，分离元素对象和用例脚本，一个页面建一个对象类。

**Data:** 测试数据目录，使用yaml文件管理页面控件元素数据和测试用例数据。

**Sripts_test:** 测试脚本目录

**Report：**测试报告目录
 
**Screen:** 截图目录。

二、编辑基本语法  
1、字体格式强调
 我们可以使用下面的方式给我们的文本添加强调的效果
*强调*  (示例：斜体)  
 _强调_  (示例：斜体)  
**加重强调**  (示例：粗体)  
 __加重强调__ (示例：粗体)  
***特别强调*** (示例：粗斜体)  
___特别强调___  (示例：粗斜体)  
2、代码  
`<hello world>`  
3、代码块高亮  
```
@Override
protected void onDestroy() {
    EventBus.getDefault().unregister(this);
    super.onDestroy();
}
```  
4、表格 （建议在表格前空一行，否则可能影响表格无法显示）
 
 表头  | 表头  | 表头
 ---- | ----- | ------  
 单元格内容  | 单元格内容 | 单元格内容 
 单元格内容  | 单元格内容 | 单元格内容  
 
5、其他引用
图片  
![图片名称](https://www.baidu.com/img/bd_logo1.png)  
链接  
[链接名称](https://www.baidu.com/)    
6、列表 
1. 项目1  
2. 项目2  
3. 项目3  
   * 项目1 （一个*号会显示为一个黑点，注意⚠️有空格，否则直接显示为*项目1） 
   * 项目2   
 
7、换行（建议直接在前一行后面补两个空格）
直接回车不能换行，  
可以在上一行文本后面补两个空格，  
这样下一行的文本就换行了。
或者就是在两行文本直接加一个空行。
也能实现换行效果，不过这个行间距有点大。  
 
8、引用
> 第一行引用文字  
> 第二行引用文字   
