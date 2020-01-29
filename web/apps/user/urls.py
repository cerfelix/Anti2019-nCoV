# _*_coding:utf-8_*_
"""
@ProjectName: AntiSARI
@Author:  liyong
@File: urls.py
@Software: PyCharm
@Time :    2020/1/28 下午11:58
"""
from web.apps.user.controller import CompanyHandler, UserHandler

urlpatterns = [
    (r'/enterprise', CompanyHandler),
    (r'/employee', UserHandler)
]
