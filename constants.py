from os import path


class Constants:
    PATH_COUNTRY = path.join(path.dirname(__file__), 'data', 'country.json')
    PATH_REGION = path.join(path.dirname(__file__), 'data', 'region.json')
    PATH_CITY = path.join(path.dirname(__file__), 'data', 'city.json')
    PATH_DB = path.join(path.dirname(__file__), 'data', 'IP2LOCATION-LITE-DB5.IPV6.BIN')
    INDEX_COUNTRY = 1
    INDEX_REGION = 2
    INDEX_CITY = 3
    INDEX_LATITUDE = 4
    INDEX_LONGITUDE = 5
