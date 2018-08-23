WEB框架:
	MVC
		Model       View       Controller
		数据库   模板文件    业务处理
	
	MTV
		Model    Template     View
		数据库   模板文件    业务处理



Django	MTV框架

	pip install django
	
	D:\ProgramData\Anaconda3\Scripts
	 
	# 创建Django工程
	django-admin startproject 【工程名称】
	
		mysite
			- mysite        # 对整个程序进行配置
				- init
				- settings  # 配置文件
				- url       # URL对应关系
				- wsgi      # 遵循WSIG规范，uwsgi + nginx
			- manage.py     # 管理Django程序：
					- python manage.py 
					- python manage.py startapp xx
					- python manage.py makemigrations
					- python manage.py migrate	
		
	# 运行Django功能
	python manage.py runserver 127.0.0.1:8001