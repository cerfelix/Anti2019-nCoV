# _*_coding:utf-8_*_
"""
@ProjectName: AntiSARI
@Author:  Javen Yan
@File: controller.py
@Software: PyCharm
@Time :    2019/12/5 上午11:50
"""
from abc import ABC
from web.apps.base.controller import BaseRequestHandler
from web.apps.base.status import StatusCode


class NoSariHandler(BaseRequestHandler, ABC):

    def get(self):
        response = dict(code=StatusCode.success.value, msg="no sari")
        return self.write_json(response)
