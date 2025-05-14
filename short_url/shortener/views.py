from django.shortcuts import render, redirect, get_object_or_404

from shortener.forms import ShortURLForm
from shortener.models import ShortURL


def home_view(request):
    short_urls = ShortURL.objects.all()
    context = {"short_urls": short_urls, "form": ShortURLForm}
    return render(request, "home.html", context=context)


# 클라이언트가 original_url 값을 전달하면, ShortURL 생성
def short_url_create_view(request):
    if request.method == "POST":
        form = ShortURLForm(request.POST)

        # 값이 유효한지 검사
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.generate_code()
            short_url.save()

    return redirect("/")


def redirect_view(request, code):
    short_url = get_object_or_404(ShortURL, code=code)
    short_url.access_count += 1
    short_url.save()
    return redirect(short_url.original_url)



# Redirect 기능 구현
# 삭제 기능 구현
# 클래스형 뷰(Class-based View)
# Django ORM 데이터
