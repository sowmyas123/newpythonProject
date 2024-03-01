class SecureClass:
    def submit(self):
        self.__password = "123"
        self.__username = "admin"
        self.heading = "VWO Login"
        
chrome = SecureClass()
chrome.heading