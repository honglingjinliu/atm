import pickle
import time
from view import View
from atm import Atm

def main():
	allUserInfo = {}
	
	try:
		f = open("peoplelist.txt","rb")
		if len(f.read())>0:
			f.seek(0,0)
			allUserInfo = pickle.load(f)
	except Exception as msg:
		print(msg)
		f = open("peoplelist.txt","wb")
		print(msg)
	finally:
		f.close()

		
	adminview = View()
	adminview.printSysUI()

	atm = Atm(allUserInfo)

	#选择角色
	print("请选择角色:")
	print("1：管理员")
	print("2：普通用户")
	roleNum = input()  #角色序号
	if roleNum == '1':
		if not adminview.adminlogin():
			print("管理员登录失败")
			return
		time.sleep(1)	
		print("管理员登录成功！请稍候...")	

	elif roleNum == '2':
		#验证卡号是否存在
		while True:
			inputCard = input("请输入您的卡号:")
			isExist = atm.isExistCard(inputCard)
			if isExist:
				break

		#验证密码是否正确
		if not atm.isExistPwd(inputCard):
			#文件中写入所有用户信息
			f = open("peoplelist.txt","wb")
			pickle.dump(atm.allUserInfo,f)
			f.close()
			return

	while True:
		adminview.printUI(roleNum)
		inputNum = input("请输入操作选项（数字）:")
				

		if inputNum == '1' and roleNum == '1':
			print(atm.allUserInfo)
			atm.createUser()
			print(atm.allUserInfo)

		elif inputNum == '2' and roleNum == '2':
			#取款操作
			atm.nomony(inputCard)
		elif inputNum == '3' and roleNum == '2':
			atm.cunqian(inputCard)
		elif inputNum == '4' and roleNum == '2':
			atm.transMoney(inputCard)
		elif inputNum == '5' and roleNum == '2':
			atm.allpeople(inputCard)
		elif inputNum == '6' and roleNum == '2':
			atm.newpassword(inputCard)	
		elif inputNum == '7' and roleNum == '1':
			if atm.jiechusuooding():
				print("解卡成功")			
		elif inputNum == '0':
			exit()
		else:
			print("您操作有误，请重新操作！")		

		#文件中写入所有用户信息
		f = open("peoplelist.txt","wb")
		pickle.dump(atm.allUserInfo,f)	
		f.close()	
if __name__ == '__main__':
	main()