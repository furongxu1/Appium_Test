from Base_Obj.Base import Base
import Page_Obj


class Send_Mes(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 输入号码和发送内容
    def send_mes(self, number, text):
        # 点击添加信息按钮
        self.click_element(Page_Obj.add)
        # 输入收件人号码
        self.input_element(Page_Obj.num, number)
        # 点击发送到收件人号码按钮
        self.click_element(Page_Obj.send_num)
        # 输入要发送的信息
        self.input_element(Page_Obj.input, text)
        # 点击发送按钮
        self.click_element(Page_Obj.send)
        # 点击返回按钮
        self.click_element(Page_Obj.return_btn)

    def get_user_list(self):
        # 获取发送信息人列表
        user_data = self.find_elements(Page_Obj.user_text)
        return [i.text for i in user_data]



