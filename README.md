# django-2.2-learn

# 运行程序

 python manage.py runserver
 
# 创建 app

python manage.py startapp partapp

 修改 views.py, 增加 urls.py,修改 settings.py, urls.py,然后重启 服务即可
 
## 模型

- 修改models.py
- python manage.py makemigrations partapp
- python manage.py migrate


## 操作

- from partapp.models import Person
- 





# 常用方法

- from datetime import datetime, date
- proxy model出现的理由： Sometimes, however, you only want to change the Python behavior of a model – perhaps to change the default manager, or add a new method.