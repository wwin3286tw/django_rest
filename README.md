[![Build Status](https://travis-ci.org/wwin3286tw/django_rest.svg?branch=master)](https://travis-ci.org/wwin3286tw/django_rest)
# django_rest
## 說明
### 測試Django API功能，並整合heroku與travis-ci，以達成持續整合
 - 由於在heroku需要引入專用的django_heroku，而在travis-ci上，此引入則會造成錯誤，經過使用
```bash
heroku run python
```
有網路查過一些資料，該方法已經不可用：https://github.com/heroku/django-heroku/issues/39
用該方法修改後，變成heroku平台不可用，又輾轉
進入遠端終端機後，使用下面腳本得出heroku的特徵，來辨識是否為在heroku建置中
```python
import os
if '/app' in os.environ['HOME']:
    import django_heroku
    django_heroku.settings(locals())
```
