#!/usr/bin/env python3


from .test_internet import TestInternetResult
from typing import List, Tuple


class CheckFailed:
    def __init__(self, data: List[Tuple[int,str, str]]) -> None:
        self.result: TestInternetResult = self.__get_status(data)

    def __get_status(self, data) -> TestInternetResult:
        failed: List[str] = [
                status
                for id, time_stamp, status in iter(data)
                if status == TestInternetResult.FAILED.value
            ]
        
        if len(failed) > 0:
            return TestInternetResult.FAILED
        
        else:
            return TestInternetResult.PASSED