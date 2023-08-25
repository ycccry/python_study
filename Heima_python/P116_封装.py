class Phtone():
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G已开启！")
        else:
            print ("5G已关闭,使用4g")

    def call_by_5g(self):
        self.__check_5g()
        print ("正在通话")

phone = Phtone()
phone.call_by_5g()
