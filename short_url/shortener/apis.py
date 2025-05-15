from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.models import ShortURL
from shortener.serializers import ShortURLCreateSerializer, ShortURLResponseSerializer


class ShortURLAPIView(APIView):
    # 전체 ShortURL 조회
    def get(self, request):
        short_urls = ShortURL.objects.all()
        response_serializer = ShortURLResponseSerializer(short_urls, many=True)
        return Response(data=response_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1) 클라이언트가 보낸 데이터를 읽어서 serializer로 검사
        serializer = ShortURLCreateSerializer(data=request.data)  # request body

        # 2) 데이터 유효성 검사
        # -> 데이터 조건(타입, 길이, ...)에 맞는지 검사
        if serializer.is_valid():
            code = ShortURL.generate_code_two()

            # 3) 데이터를 DB에 저장
            short_url = serializer.save(code=code)  # instance를 생성 -> DB 저장

            # 4) 응답을 반환
            response_serializer = ShortURLResponseSerializer(short_url)
            return Response(
                data=response_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortURLGenericAPIView(ListAPIView):
    queryset = ShortURL.objects.all()  # 어떤 데이터 모델을 쓸지
    serializer_class = ShortURLResponseSerializer  # serializer
