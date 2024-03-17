class Func_userLoginMethod(object):
    def setupFunc(self):
        self.bind()
    
    def bind(self):
        self.pbtn_reset.clicked.connect(self.reset)
    def reset(self):
        self.ledt_userName.clear()
        self.ledt_password.clear()
    # self.driver = webdriver.Chrome()
    # self.driver.implicitly_wait(10)
    # self.driver.maximize_window()
    # self.driver.get("http://192.168.1.100:8080/pttlCrm/")
    # self.driver.find_element_by_id("userName").send_keys("admin")