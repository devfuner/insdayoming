# Django를 사용한 웹 프로젝트

### 사용 툴
- Pycharm 2018.2
- Python 3.7
- Django 2.0.7
- Pillow 5.2.0


### 장고 기본 사용법
Django 프로젝트 만들기
> (venv) ~$ django-admin startproject myweb

or

> (venv) ~$ django-admin startproject myweb path

> 본 프로젝트의 예  
> (venv) D:\PycharmProjects django-admin startproject insdayoming D:\PycharmProjects\insdayoming

서버 실행하기
> (venv) ~$ manage.py runserver

포트 변경하기
> (venv) ~$ manage.py runserver 변경할 포트

> 포트 변경 예  
> (venv) ~$ manage.py runserver 8080

App 만들기
> (venv) ~$ manage.py startapp home

App을 만들고 해야할 일
1. settings.py : INSTALLED_APPS 리스트에 Django App명 (home) 추가
2. urls.py : urlpatterns 리스트에 사용할 URL 패턴 추가
3. home/views.py : urlpatterns에 추가한 URL 패턴을 처리할 함수 추가

Model을 만들고 해야할 일
1. manage.py makemigrations
2. manage.py migrate


### 참고사이트
[django 초보 가이드 실습을 통해 알아보는 장고 입문](https://inflearn.com/course/django-초보-가이드-실습을-통해-알아보는-장고-입문/)  
[예제로 배우는 Python 프로그래밍](http://pythonstudy.xyz/python/django)    
[장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/)  
[장고걸스 튜토리얼 GitHub](https://github.com/DjangoGirls/tutorial/tree/master/ko)    
[bootstrap](https://getbootstrap.com)  
[django Documentation](https://docs.djangoproject.com/ko/2.0/intro/)  
[날로 먹는 Django 웹프레임워크 강좌](https://blog.hannal.com/category/start-with-django-webframework/)  
