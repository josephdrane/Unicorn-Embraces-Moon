#!/usr/bin/env python3

import datetime
import sqlite3
from typing import List, Tuple

from .test_internet import TestInternetResult


class Database:
    def __init__(self) -> None:
        self.the_date = datetime.datetime.now().isoformat()
        self.conn = sqlite3.connect("~/Unicorn-Embraces-Moon.db")
        self.c = self.conn.cursor()
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS status
                    (id integer primary key, date text, result text)"""
        )

    def add(self, test_result: TestInternetResult) -> None:
        try:
            with self.conn:
                self.conn.execute(
                    "insert into status(date, result) values (?, ?)",
                    (self.the_date, test_result),
                )

        except sqlite3.IntegrityError as error:
            print(f"Failed to commit to db with Error: {error}")

    def close(self) -> None:
        self.conn.close()

    def get_last_five_minutes(self) -> List[Tuple[int,str,str]]:
        now = datetime.datetime.now()
        now_iso = now.isoformat()

        fiveMinBack = now - datetime.timedelta(minutes=5)
        fiveMinBack_iso = fiveMinBack.isoformat()

        time_range_tuple = (fiveMinBack_iso, now_iso)
        sql_query = "select * from status where date between ? and ?"

        last_five_minutes = [row for row in self.c.execute(sql_query, time_range_tuple)]

        return last_five_minutes

    def get_failures(self) -> List[Tuple[int,str,str]]:
        sql_query = "select * from status where result == 'failed'"
        data = [row for row in self.c.execute(sql_query)]
        return data 