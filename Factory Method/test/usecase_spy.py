from interface import DatabaseInterface
from typing import Type, Dict, Union

class UsecaseSpy:

    def __init__(self, repository: Type[DatabaseInterface]) -> None:
        self.__repository = repository
        self.entry = dict()
    
    def do_something(self, data: bool) -> Union[Dict, None]:
        self.entry['data'] = data
        self.entry['repository'] = self.__repository
        if data is True:
            repositoryResponse = self.__repository.select_one()
            return repositoryResponse
        return None