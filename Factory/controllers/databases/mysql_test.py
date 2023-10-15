from .mysql import MysqlRepository

def test_mysql_repository():
    mysql_repository = MysqlRepository()
    
    assert mysql_repository.select_one() != {}