# _*_coding:utf-8_*_
"""
@ProjectName: AntiSARI
@Author:  liyong
@File: controller.py
@Software: PyCharm
@Time :    2020/1/28 下午11:50
"""
from abc import ABC
from web.apps.base.controller import BaseRequestHandler
from web.apps.base.status import StatusCode
from web.apps.user.libs import get_user, get_company, add_user, add_company


class CompanyHandler(BaseRequestHandler, ABC):

    async def get(self):
        response = dict(code=StatusCode.success.value)
        name = self.get_argument('companyName', None)
        if name:
            result = await get_company(self, name)
        else:
            result = await get_company(self)
        response['code'] = result['code']
        response['message'] = result['msg']
        if result['status']:
            response['data'] = result['data']
        return self.write_json(response)

    async def post(self):
        response = dict()
        payload = self.get_payload()
        result = await add_company(self, **payload)
        response['code'] = result['code']
        response['msg'] = result['msg']
        return self.write_json(response)


class UserHandler(BaseRequestHandler, ABC):

    async def get(self):
        response = dict(code=StatusCode.success.value)
        _id = self.get_argument('id', None)
        if _id:
            result = await get_user(self, _id)
        else:
            result = await get_user(self)
        response['code'] = result['code']
        response['message'] = result['msg']
        if result['status']:
            response['data'] = result['data']
        return self.write_json(response)

    async def post(self):
        response = dict()
        payload = self.get_payload()
        result = await add_user(self, **payload)
        response['code'] = result['code']
        response['msg'] = result['msg']
        return self.write_json(response)





