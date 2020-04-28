from Page_Obj.Search_Page import Search_Page
from Page_Obj.send_message_page import Send_Mes
"""
    统一管理页面的类对象，
    不用每次都导入每个页面的类对象，用一个类管理所有的类
"""
class Page_O:
    def __init__(self, driver):
        self.driver = driver

    def re_search_page(self):
        # 返回搜索页面对象
        return Search_Page(self.driver)

    def re_send_mes_page(self):
        # 返回发送短信页面对象
        return Send_Mes(self.driver)