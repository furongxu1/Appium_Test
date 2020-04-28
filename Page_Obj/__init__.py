from selenium.webdriver.common.by import By

"""
    搜索页面的元素信息
"""

# 搜索按钮
search_btn = (By.ID, "com.android.settings:id/search")
# 搜索输入框
search_input = (By.ID, "android:id/search_src_text")
# 返回按钮
search_return = (By.CLASS_NAME, "android.widget.ImageButton")



"""
    发送短信页面元素信息
"""
# 添加信息按钮
add = (By.ID, "com.android.messaging:id/start_new_conversation_button")
# 收件人号码输入框
num = (By.ID, "com.android.messaging:id/recipient_text_view")
# 发送到收件人号码按钮
send_num = (By.XPATH, "//*[contains(@text,'常用联系人')]")
# 输入信息
input = (By.ID, "com.android.messaging:id/compose_message_text")
# 发送按钮
send = (By.ID, "com.android.messaging:id/self_send_icon")
# 返回按钮
return_btn = (By.XPATH, "//*[contains(@content-desc,'转到上一层级')]")
# 短信接收内容
user_text = (By.ID, "com.android.messaging:id/conversation_snippet")


