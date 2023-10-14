from .file import File
from faker import Faker

fake = Faker()

def test_get_size():
    file_size = fake.random_int()
    f = File("test.txt", file_size)

    assert f.get_size() == file_size