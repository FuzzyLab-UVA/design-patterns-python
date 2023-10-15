from test import UsecaseSpy
from faker import Faker 
from controllers import MysqlRepository


def test_usecase():
    usecase = UsecaseSpy(MysqlRepository())

    assert usecase.do_something(True) is not None
    assert usecase.entry['data'] is not None
    assert usecase.entry['repository'] is not None
