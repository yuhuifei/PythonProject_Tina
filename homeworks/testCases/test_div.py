#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Tina Yu
# @Time    : 2021-4-11 12:36
import pytest
import yaml

from homeworks.Calculator import Calculator


class TestDiv:
    def setup_class(self):
        print("\n***************开始除法测试**************")
        self.cal_div = Calculator()

    def teardown_class(self):
        print("\n\n***************结束除法测试**************")


    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("./data_div.yaml")))
    def test_div(self, a, b, expect):
        try:
            assert expect == round(self.cal_div.div(a,b),5)
        except Z:
            print("这里存在异常！")

