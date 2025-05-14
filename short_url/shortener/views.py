from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

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


# Function Based View = 함수형 뷰
def short_url_detail_view(request, code):
    # Redirect
    if request.method == "GET":
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.access_count = F("access_count") + 1
        short_url.save()
        return redirect(short_url.original_url)

    # 삭제 기능
    # HTTP 원칙대로면 DELETE로 처리해야 하지만,
    # HTML Form에서 DELETE 요청을 보낼 수 없기 때문에 POST로 처리
    elif request.method == "POST":
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return redirect("/")


class ShortURLDetailView(View):
    def get(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.access_count = F("access_count") + 1
        short_url.save()
        return redirect(short_url.original_url)

    def post(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return redirect("/")
