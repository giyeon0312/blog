from django.shortcuts import render
from .models import Blog

def home(request):
    blogs=Blog.objects #models.py에서 만든 Blog객체들(이름하야 쿼리셋!)을 전달받을 수 있다
    return render(request,'home.html',{'blogs':blogs})
#쿼리셋의 기능들을 처리,표시하는 방법은 "메소드"..!
#메소드를 사용하는 형식은
#모델.쿼리셋(objects).메소드
