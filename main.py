import argparse
from pprint import pprint
import sqlite3

from db import Database
from test_internet import TestInternet, TestInternetResult


parser = argparse.ArgumentParser(description="Test Internet and Powercycle w/ Pi Zero")
parser.add_argument("--test", action="store_true", help="Run Tests")
args = parser.parse_args()

if args.test:
    test: TestInternet = TestInternet("https://facebook.com")
    result: TestInternetResult = test.result.value
    db = Database()
    db.add(result)
    last_five = db.get_last_five_minutes()
    pprint(last_five)

