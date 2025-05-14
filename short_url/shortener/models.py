import random
import string

from django.db import models


class ShortURL(models.Model):
    code = models.CharField(max_length=8, unique=True)  # 중복 불가
    original_url = models.URLField(max_length=255)  # 원본 URL
    access_count = models.PositiveIntegerField(default=0)  # 접속 횟수 기록
    created_at = models.DateTimeField(auto_now_add=True)  # 생성된 시간

    def __str__(self):
        return f"{self.code} -> {self.original_url}"

    # 랜덤한 코드 생성
    def generate_code(self):
        characters = string.ascii_letters + string.digits

        code = ""
        for _ in range(8):
            code += random.choice(characters)

        self.code = code
