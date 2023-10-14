from usecase import Usecase
from databases import MysqlRepository

class MySqlFactory:
    
    @staticmethod
    def create() -> Usecase:
        return  Usecase(MysqlRepository())
        
    
        