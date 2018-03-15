import random,time
from card import Card
from user import User

class Atm:
	def __init__(self,allUserInfo):
		self.allUserInfo = allUserInfo

	#检测密码	
	def isExistPwd(self,inputCard):
		if self.allUserInfo.get(inputCard).cardInfo.status:
			 print("此卡已锁定，没有必要输入密码，请联系管理员!")
			 return False
		for i in range(3):
			inputPwd = input("请输入密码:")
			if inputPwd == self.allUserInfo.get(inputCard).cardInfo.cardPwd:
				return True	
			else:
				print("密码输入错误，还有%s次输入机会"%(2-i))

		else:
			self.allUserInfo.get(inputCard).cardInfo.status = True  #锁定卡
			print("此卡已锁定！")
			print(self.allUserInfo.get(inputCard).cardInfo.status)
			return False		
		
			
	#判断卡号是否存在	
	def isExistCard(self,cardNum):
		if not self.allUserInfo.get(cardNum):
			print("暂无此卡")
			return False
		return True	
			
	def randomCardNum(self):
		#print
		cardnum = ''
		#卡号一共6位
		for i in range(6):
			cardnum += str(random.randint(0,9))

		#判断生成卡号有没有重复	
		#{1212:user1,2323:user2,1213:user3}
		# for i in self.allUserInfo:   #字典遍历  下标（键）{'name':'zs'}  {cardnum:用户对象}
		# 
		# 
		# 	if i == cardnum:
		# 		self.randomCardNum()

		#通过get方法查找  生成的卡号是否有存在，若存在则重新生成（函数自调用）
		if self.allUserInfo.get(cardnum):
			self.randomCardNum()		
		
		return cardnum	

		
			
	#检测确认密码	
	def checkPwd(self,onePwd):
		#
		for i in range(3):

			two = input("请再次输入确认密码:")
			if two == onePwd:
				print("确认密码一致")
				return True	
			else:
				print("密码输入错误，还有%s次输入机会"%(2-i))

		else:
			print("确认密码三次用完")
			return False		

	#开卡
	def createUser(self):
		name = input('请输入姓名：')
		idCard = input('请输入身份证号：')
		phone = input('请输入电话号：')
		money = input('请输入预存金额：')

		#预存金额是否大于1
		if int(money) < 1:
			print("预存金额不足，开卡失败！")
			return False

		onePwd = input("请输入卡密码：")

		twoPwd = self.checkPwd(onePwd)  #调用检查确认密码	
		#确认密码三次机会用完
		if not twoPwd:
			print("开卡失败！")
			return False

		#以上没有问题，进行开卡
		
		#随机生成卡号  
		cardNum = self.randomCardNum()

		#创建卡对象
		card = Card(cardNum,onePwd,money)
		#用户对象
		self.allUserInfo[cardNum]=User(name,idCard,phone,card)

		# aa = {'name':'zs'}
		# aa['name']='12212' 

		time.sleep(1)
		print("开卡成功!请牢记您的卡号%s"%cardNum)
		return 	
			


	#解卡
	   #。。。。。status = False 
	def jiechusuooding(self):
		while True:
			idCard1=input("输入您所需要解锁的卡号")
			# print(self.allUserInfo.get(idCard1).cardInfo.status)
			#判断卡号是否存在
			if not self.isExistCard(idCard1):
				print("没有查询到%s的卡号"%(idCard1))
				continue
			if self.allUserInfo.get(idCard1).cardInfo.status==False:
				print("该卡没有锁定可以正常使用")
				return False
			self.allUserInfo.get(idCard1).cardInfo.status=False
			return True

	#查询
		#当前登录用户卡号， self.allUserInfo.get(inputCard).cardInfo.mone
	def allpeople(self,inputCard):
		print("姓名：%s"%(self.allUserInfo.get(inputCard).name))
		print("手机号：%s"%(self.allUserInfo.get(inputCard).phone))
		print("身份证：%s"%(self.allUserInfo.get(inputCard).idCard))
		print("账户还剩余的金额为%s"%(self.allUserInfo.get(inputCard).cardInfo.money))
	#存款
		#当前登录用户卡号  输入存款  0>(附加 0~2500)  余额+存入金额 
	def cunqian(self,inputCard):
		oldmaney=input("输入你存款的金额")
		oldmaney=int(oldmaney)
		if oldmaney>2500:
			print("您储存的金额过大,系统不能处理")
		elif oldmaney<=0:
			print("输入大于0的钱")
		else:
			self.allUserInfo.get(inputCard).cardInfo.money=str(int(self.allUserInfo.get(inputCard).cardInfo.money)+int(oldmaney))
			print("账户还剩余的金额为%s"%(self.allUserInfo.get(inputCard).cardInfo.money))
	#取款
		#当前登录用户卡号  输入取款 
	def nomony(self,inputCard):
		newmoney=input("请输入要取款的金额")
		newmoney=int(newmoney)
		if newmoney>int(self.allUserInfo.get(inputCard).cardInfo.money):
			print("您账户上有多少钱，你心里没点逼数")
			# return
		elif newmoney<=0:
			print("必须取的钱是大于1的")
		else:
			self.allUserInfo.get(inputCard).cardInfo.money=str(int(self.allUserInfo.get(inputCard).cardInfo.money)-int(newmoney))
			print("当前账户还剩余额%s"%(self.allUserInfo.get(inputCard).cardInfo.money))
			print("取款成功")
	#转账
	def transMoney(self,inputCard):
		transCard = input("请输入要转账的卡号：")
		#没有此卡
		if not self.isExistCard(transCard):
			self.transMoney(inputCard)


		if 	transCard == inputCard:
			print("不能给自己转账！")
			return	
		if self.allUserInfo.get(transCard).cardInfo.status:
			print("对方账号被锁定，无法转账！")
			return
		transmoney = input("请输入转账金额：")	 

		if int(self.allUserInfo.get(inputCard).cardInfo.money) > int(transmoney):
			self.allUserInfo.get(inputCard).cardInfo.money =str(int(self.allUserInfo.get(inputCard).cardInfo.money)-int(transmoney))
			self.allUserInfo.get(transCard).cardInfo.money =str(int(self.allUserInfo.get(transCard).cardInfo.money)+int(transmoney))
			print("转账成功！当前卡余额还剩%s"%(self.allUserInfo.get(inputCard).cardInfo.money))
			return
		else:
	 		print("卡内余额不足，请重新操作！")
#487560
	#修改密码
	def newpassword(self,inputCard):
		xinpassword=input("输入你的原密码")
		if xinpassword==self.allUserInfo.get(inputCard).cardInfo.cardPwd:
			newpass=input("输入成功，输入你的新密码吧")
			for i in range(3):
				oldpas=input("再次输入密码")
				if oldpas!=newpass:
					print("还能在失误%d"%(2-i))
				else:
					self.allUserInfo.get(inputCard).cardInfo.cardPwd=newpass
					return					
		else:
			print("输入的原密码有误")

		