
"""
https://github.com/arrenglover/openfabmap/wiki/Datasets
"""
datasets_path = "./datasets"


from mega import Mega
login = Mega().login()
p = login.download_url('https://mega.nz/file/XAZHgZYa#Rp83z96sc5iiSeV2LC1INyNTYt3JM2utQ8_9yms3Fg8')

