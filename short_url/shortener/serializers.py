from rest_framework import serializers

from shortener.models import ShortURL


# 클라이언트로부터 ShortURL 생성에 필요한 original_url을 넘겨받는 Serializer
class ShortURLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL            # ShortURL 모델을 참조해서 Serializer를 만들어라
        fields = ["original_url"]   # original_url만 입력을 받겠다

# 서버에서 ShortURL 데이터를 응답할 때 사용할 Serializer
class ShortURLResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = "__all__"  # 모든 필드
