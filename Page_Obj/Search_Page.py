from Base_Obj.Base import Base
import Page_Obj

class Search_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_search_btn(self):
        # 点击搜索按钮
        self.click_element(Page_Obj.search_btn)

    def input_search(self, text):
        # 搜索框输入内容
        self.input_element(Page_Obj.search_input, text)

    def return_search_btn(self):
        # 点击返回按钮
        self.click_element(Page_Obj.search_return)