class View:
	adminNum = '1'
	adminPwd = '1'

	#欢迎首页
	def printSysUI(self):
		print("*******************************************")
		print("*                                         *")
		print("*           欢迎进入本系统                *")
		print("*                                         *")
		print("*******************************************")

	def adminlogin(self):
		adminnum = input("请输入管理员账号：")
		if adminnum != self.adminNum:
			print("管理员账号错误！")
			return False
		adminpwd = input("请输入管理员密码：")
		if adminpwd != self.adminPwd:
			print("管理员账号错误！")
			return False
		return True	
	#根据角色打印的对应的操作页面	
	def printUI(self,rolenum):
		if rolenum == '1': #管理员
			print("*******************************************")
			print("*     开户（1）                 解卡（7） *")
			print("*                               退出（0） *")
			print("*******************************************")
		elif rolenum == '2': #普通用户
			print("*******************************************")
			print("*     取款（2）                 存款（3） *")
			print("*     转账（4）                 查询（5） *")
			print("*     改密（6）                 退出（0） *")
			print("*******************************************")		
	# #显示管理员操作页面
	# def printBackSysUI(self):
	# 	pass
	# #显示普通用户操作页面
	# def printUserSysUI(self):
	# 	pass