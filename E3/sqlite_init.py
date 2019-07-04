import sqlite3


def konekcija_ka_bazi():
    return sqlite3.connect('plugins/E3/e3Baza.db')
