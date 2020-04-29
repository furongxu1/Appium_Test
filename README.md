# Appium_Test  
## 项目简介：
框架使用Pytest 运行 Yaml 来驱动 Appium 进行 AppUI 自动化测试，该框架实现了用例失败自动截图功能，自动生成allure报告以及自动邮件发送测试报告。 
## 目录结构介绍：
**Base_Obj:** Appium基础定位方法目录

**Page_Obj:** 页面元素目录，使用Page Object模式将页面定位和业务操作分开，分离元素对象和用例脚本，一个页面建一个对象类。

**Data:** 测试数据目录，使用Yaml文件管理页面控件元素数据和测试用例数据。

**sripts_test:** 测试脚本目录

**report:** 测试报告目录
 
**screen:** 截图目录

## 测试结果展示
**Allure测试报告**
![image](https://github.com/furongxu1/Appium_Test/blob/master/show_results/allure_report_1.png)
![image](https://github.com/furongxu1/Appium_Test/blob/master/show_results/allure_report_2.png)
![image](https://github.com/furongxu1/Appium_Test/blob/master/show_results/allure_report_3.png)
**自动截图存放指定的目录**
![image](https://github.com/furongxu1/Appium_Test/blob/master/show_results/screen.png)
**邮件测试报告**
![image](https://github.com/furongxu1/Appium_Test/blob/master/show_results/email.jpg)
