#!/usr/bin/env python3

import argparse
import sqlite3
from typing import List, Tuple

from lib.db import Database
from lib.check_failed import CheckFailed
from lib.pi_zero import PiZero
from lib.test_internet import TestInternet, TestInternetResult


parser = argparse.ArgumentParser(description="Test Internet and Powercycle w/ Pi Zero")

parser.add_argument("--test", action="store_true", help="Run Tests")
parser.add_argument("--view", action="store_true", help="Select * from status.db")

args = parser.parse_args()

if args.test:
    test: TestInternet = TestInternet("https://facebook.com")
    result: TestInternetResult = test.result.value
    
    db = Database()
    db.add(result)
    last_five: List[Tuple[int,str,str]] = db.get_last_five_minutes()
    db.close()

    from pprint import pprint
    pprint(last_five)

    check_failed = CheckFailed(last_five)
    if check_failed.result == TestInternetResult.FAILED:
        rebooter: PiZero = PiZero()
        rebooter.power_off()
        rebooter.power_on()

if args.view:
    db = Database()
    failures = db.get_failures()
    print('\n<--- Failures In DB --->\n')
    pprint(failures)
    print('\n<--- Failures In DB --->\n')


args = parser.parse_args()