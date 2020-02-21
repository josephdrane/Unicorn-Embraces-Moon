#!/usr/bin/env python3

from enum import Enum
import requests

#
# TODO : Need to create a type or checking the URL string provided
#


class TestInternetResult(Enum):
    PASSED = "passed"
    FAILED = "failed"


class TestInternet:
    def __init__(self, urls_to_test: str) -> None:
        self.urls_to_test: str = urls_to_test
        self.result: TestInternetResult = self.__test_urls()

    def __test_urls(self) -> TestInternetResult:
        try:
            req = requests.get("https://facebook.com")
            return TestInternetResult.PASSED
        except Exception as error:
            print(f"Got an Error {error}")
            return TestInternetResult.FAILED
