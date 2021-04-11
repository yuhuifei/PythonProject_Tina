#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Tina Yu
# @Time    : 2021-4-11 11:54
from unicodedata import decimal

import pytest
import yaml

from homeworks.Calculator import Calculator


class TestAdd:
    def setup_class(self):
        print('\n***************开始加法测试**************\n')
        self.cal_add = Calculator()

    def teardown_class(self):
        print("\n\n***************结束加法测试**************")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("./data_add.yaml")))
    def test_add(self, a, b, expect):
        assert expect == round(self.cal_add.add(a, b),5)
