class Config:
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskdb.sqlite'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/project2'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False