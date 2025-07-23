import json
import os
from datetime import datetime, timedelta

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from Tong_django.settings import STATICFILES_DIRS, SERVER_PORT
from .models import User, Token
from app.models import Carousel, Vajra
from django.conf import settings

from . import utils


# Create your views here.

class CarouselView(View):
    def get(self, request):
        carousels = Carousel.objects.all()
        carousel_list = list(carousels.values())
        # carousels_lsit = []
        # for item in carousels:
        #     carousel = {
        #         "id":item.id,
        #         "title":item.description,
        #         "poster_url":item.poster_url,
        #         "target_url":item.target_url,
        #     }
        #     carousels_lsit.append(carousel)
        # carousel_json = json.dumps(carousels_lsit)
        # return HttpResponse(carousel_json)
        return JsonResponse(carousel_list, safe=False)


class VajraView(View):
    def get(self, request):
        vajras = Vajra.objects.all()
        vajra_list = list(vajras.values())
        return JsonResponse(vajra_list, safe=False)


def json_view(func):
    """ 反序列化装饰器，将JSON请求体转换为字典 """

    def wrapper(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        request.json_data = json.loads(body_unicode)
        return func(self, request, *args, **kwargs)

    return wrapper


class UserView(View):
    def get(self, request):
        data = request.headers.get('Authorization')
        print(data)
        return JsonResponse({"msg": "ok"}, safe=False)

    @json_view
    def post(self, request):
        data = request.json_data
        appid = settings.APPID
        appsecret = settings.APPSECRET
        wx_login_code = data['code']
        # 微信登录请求api
        wx_res = requests.get("https://api.weixin.qq.com/sns/jscode2session", params={
            "appid": appid,
            "secret": appsecret,
            "js_code": wx_login_code,
            "grant_type": "authorization_code"
        }).json()

        # 使用get_or_create 查询用户信息，判断用户是否存在

        user, create = User.objects.get_or_create(openid=wx_res['openid'])
        # 生成token
        token = utils.generate_token(wx_res['session_key'])

        """如果为True，说明用户不存在"""
        if create:
            Token.objects.create(user_id=user.id, token=token, expires=datetime.now() + timedelta(days=7))
            return JsonResponse({"code": 0, "token": token}, safe=False)

        # 如果用户存在，则更新token
        Token.objects.filter(user_id=user.id).update(token=token, expires=datetime.now() + timedelta(days=7))
        user_info = {
            "name": user.name,
            "avatar_url": user.avatar_url,
            "introduction": user.introduction

        }
        return JsonResponse({"code": 0, "token": token, "user_info": user_info}, safe=False)

class updateView(View):
    def post(self,request):

        # 保存图片
        avatar = request.FILES.get('avatar')
        avatar_path = os.path.join(STATICFILES_DIRS[0],'media',avatar.name)
        with open(avatar_path,'wb') as f:
            f.write(avatar.read())

        # 接受token，并且保存图片路径到数据库
        token = request.headers.get('Authorization')
        user_id = Token.objects.get(token=token).user_id
        user = User.objects.get(id=user_id)

        # 上传文件的文件夹
        upload_dir = f'http://127.0.0.1:{SERVER_PORT}/static/media/{avatar.name}'
        # 文件路径
        # upload_path =  os.path.join(upload_dir,avatar.name)
        user.avatar_url = upload_dir
        user.save()

        return JsonResponse({"avatar_url": upload_dir}, safe=False)

    def put(self,request):
        data = json.loads(request.body)
        user_name = data['name']
        avatar = data['avatar_url']
        introduction = data['introduction']

        # 通过token找到对应的用户
        token = request.headers.get('Authorization')
        user_id = Token.objects.get(token=token).user_id
        user = User.objects.get(id=user_id)
        user.name = user_name
        # user.avatar_url = avatar
        user.introduction = introduction

        user.save()
        return  JsonResponse({"code":0, "msg":"更新成功"},safe=False)
