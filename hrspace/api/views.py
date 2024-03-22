from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse


from api.serializers import (CitySerializer, LineOfBusinessSerializer,
                             OrderSerializer)
from orders.models import City, LineOfBusiness, Order


@extend_schema(tags=('City',),)
@extend_schema_view(
    list=extend_schema(
        summary='Для получения списока городов',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=CitySerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    create=extend_schema(
        summary='Для добавления города',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                response=CitySerializer,
                description='201: Успешно создан'
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос ',
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=None,
                description='Ошибка 404: Требуется авторизация',
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=None,
                description='Ошибка 403: Доступ запрещен',
            ),
        },),
    retrieve=extend_schema(
        summary='Детальная информация о городе',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=CitySerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос ',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    update=extend_schema(
        summary='Обновление информации о городе',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=CitySerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=None,
                description='Успех 204: Пустое тело сообщения',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    partial_update=extend_schema(
        summary='Для частичного обновления города',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=CitySerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=None,
                description='Успех 204: Пустое тело сообщения',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    destroy=extend_schema(
        summary='Удаление города по id',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=CitySerializer,
                description='Успех 204: Запись удалена',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },)
)
class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


@extend_schema(tags=('LineOfBusiness',),)
@extend_schema_view(
    list=extend_schema(
        summary='Для получения списока сфер дейтельности',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=LineOfBusinessSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    create=extend_schema(
        summary='Для добавления сферы дейтельности',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                response=LineOfBusinessSerializer,
                description='201: Успешно создан'
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=None,
                description='Ошибка 401: Требуется авторизация',
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=None,
                description='Ошибка 403: Доступ запрещен',
            ),
        },),
    retrieve=extend_schema(
        summary='Детальная информация о сфере дейтельности',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=LineOfBusinessSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос ',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    update=extend_schema(
        summary='Обновление информации о сфере дейтельности',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=LineOfBusinessSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=None,
                description='Успех 204: Пустое тело сообщения',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    partial_update=extend_schema(
        summary='Для частичного обновления сферы дейтельности',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=LineOfBusinessSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=None,
                description='Успех 204: Пустое тело сообщения',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    destroy=extend_schema(
        summary='Удаление сферы дейтельности по id',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=LineOfBusinessSerializer,
                description='Успех 204: Запись удалена',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },)
)
class LineOfBusinessViewSet(ModelViewSet):
    queryset = LineOfBusiness.objects.all()
    serializer_class = LineOfBusinessSerializer


@extend_schema(tags=('Order',),)
@extend_schema_view(
    list=extend_schema(
        summary='Для получения списока заявок',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=OrderSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    create=extend_schema(
        summary='Для добавления заявки',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                response=OrderSerializer,
                description='201: Успешно создан'
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=None,
                description='Ошибка 404: Требуется авторизация',
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=None,
                description='Ошибка 403: Доступ запрещен',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
        },),
    retrieve=extend_schema(
        summary='Детальная информация о заявке',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=OrderSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос ',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    update=extend_schema(
        summary='Обновление информации о заявке',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=OrderSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=None,
                description='Успех 204: Пустое тело сообщения',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    partial_update=extend_schema(
        summary='Для частичного обновления заявки',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response=OrderSerializer,
                description='Успех 200: Запрос успешно выполнен'
            ),
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=None,
                description='Успех 204: Пустое тело сообщения',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },),
    destroy=extend_schema(
        summary='Удаление заявки по id',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                response=OrderSerializer,
                description='Успех 204: Запись удалена',
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=None,
                description='Ошибка 400: Неправильный, некорректный запрос',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Ошибка 404: Не найден, не существует',
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=None,
                description='Ошибка 500: Сервис временно не доступен',
            )
        },)
)
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
