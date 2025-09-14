from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNazione():
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT DISTINCT(Country) FROM go_retailers"""
        listaCountry = []
        cursor.execute(query)
        for c in cursor:
            listaCountry.append(c["Country"])
        db.close()
        cursor.close()
        return listaCountry

    @staticmethod
    def getAnno():
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT DISTINCT(YEAR(Date)) AS anno FROM go_daily_sales 
                    WHERE YEAR(Date) > 2014 AND YEAR(Date) < 2019"""
        listaAnni=[]
        cursor.execute(query)
        for c in cursor:
            listaAnni.append(c["anno"])
        db.close()
        cursor.close()
        return listaAnni

    @staticmethod
    def getRetailerPerNazione(nazione):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT * FROM go_retailers WHERE Country=%s"""
        listaRetailer = []
        cursor.execute(query, (nazione, ))
        for c in cursor:
            listaRetailer.append(Retailer(**c))
        db.close()
        cursor.close()
        return listaRetailer

    @staticmethod
    def getListaProdotti(codiceRetailer, anno):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT DISTINCT(Product_number) FROM go_daily_sales 
                    WHERE Retailer_code=%s AND YEAR(date)=%s"""
        listaProdotti=[]
        cursor.execute(query, (codiceRetailer, anno))
        for c in cursor:
            listaProdotti.append(c["Product_number"])
        db.close()
        cursor.close()
        return listaProdotti
