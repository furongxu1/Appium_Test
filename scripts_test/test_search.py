import sys, os, pytest
sys.path.append(os.getcwd())

from Base_Obj.init_driver import init_driver_search
from Page_Obj.Page_obj import Page_O
from Base_Obj.Read_Data import ret_yaml_data

def yaml_data():
    data_list = []
    data = ret_yaml_data("search_data").get("Search_Data")
    for i in data.keys():
        data_list.append((i, data.get(i).get("test")))
    return data_list

class Test_Search:
    def setup_class(self):
        # 实例化driver
        self.driver = init_driver_search()
        # 统一页面对象管理类
        self.po = Page_O(self.driver).re_search_page()

    def teardown_class(self):
        # 点击返回按钮
        self.po.return_search_btn()
        self.driver.quit()

    @pytest.fixture(scope="class")
    def click_serach_operation(self):
        # 点击搜索按钮
        self.po.click_search_btn()

    @pytest.mark.usefixtures("click_serach_operation")
    @pytest.mark.parametrize("test_num, text", yaml_data())
    def test_search_page(self, test_num, text):
        print("用例编号", test_num)
        # 输入操作
        self.po.input_search(text)
        self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)


