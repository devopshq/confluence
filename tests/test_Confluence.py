# -*- coding: utf-8 -*-


import pytest
from exampleproject import Main


class TestConfluence():

    @pytest.fixture(scope='class', autouse=True)
    def init(self):
        print("This is start of test example.")

    def test_Main(self):
        assert Main.Main() == "This is Main module for Confluence Project that do nothing.\nRead more about DevOpsHQ Community here: https://github.com/devopshq/ExampleProject"
