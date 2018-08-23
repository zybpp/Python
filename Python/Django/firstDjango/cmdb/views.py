from django.shortcuts import render

# Create your views here.

from django.views import View
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def login(request):
	error_msg = ""
	if request.method == "POST":
		user = request.POST.get("user",None)
		pwd = request.POST.get("pwd",None)
		if user == "root" and pwd == "123456":
			return redirect("/home/")
		else:
			error_msg = "用户名或密码错误"
	return render(request,"login.html",{"error_msg" : error_msg})

USER_LIST = [
	{"username":"zhangheting","email":"zht@wind-mobi.com","gender":"男"},
	{"username":"lishunbo","email":"lsb@wind-mobi.com","gender":"男"},
	{"username":"liuyang","email":"ly@wind-mobi.com","gender":"女"},
]

def home(request):
	error_add = ""
	error_delete = ""
	idex=None
	if request.method == "POST":
		username = request.POST.get("username",None)
		email = request.POST.get("email",None)
		gender = request.POST.get("gender",None)
		add = request.POST.get("add",None)
		delete = request.POST.get("delete",None)
		print("username = %s,email = %s,gender = %s" %(username,email,gender))
		if add is not None:
			if username != "" and email != "" and gender != "":
				temp = {"username":username,"email":email,"gender":gender}
				USER_LIST.append(temp)
			else:
				error_add = "信息输入不正确"
		elif delete is not None:
			for user in USER_LIST:
				if user["username"] == username:
					idex = USER_LIST.index(user)
			if idex is not None:
				USER_LIST.pop(idex)
			else:
				error_delete = "用户名不存在"
	return render(request,"home.html",{"user_list":USER_LIST,"error_add":error_add,"error_delete":error_delete})

def detail(request,*args,**kwargs):
	return HttpResponse("Hello world!!")