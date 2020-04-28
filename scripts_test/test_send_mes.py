import sys, os, pytest
sys.path.append(os.getcwd())

from Base_Obj.init_driver import init_driver_send
from Page_Obj.Page_obj import Page_O
from Base_Obj.Read_Data import ret_yaml_data

def read_test_data():
    data_list = []
    data = ret_yaml_data("send_mes_data").get("Send_Message_Data")
    for i in data.keys():
        data_list.append((i, data.get(i).get("number")
                          , data.get(i).get("text")
                          , data.get(i).get("expect")))
    return data_list


class Test_search_text:
    def setup_class(self):
        self.driver = init_driver_send()
        self.send_mes_obj = Page_O(self.driver).re_send_mes_page()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("test_num, number, text, expect", read_test_data())
    def test_send(self, test_num, number, text, expect):
        print(test_num)
        self.send_mes_obj.send_mes(number, text)
        assert expect in self.send_mes_obj.get_user_list()

