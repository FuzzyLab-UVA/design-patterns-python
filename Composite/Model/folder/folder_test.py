from .folder import Folder
from faker import Faker
from ..file import File

fake = Faker()

def test_get_size():
    file_size_1 = fake.random_int()
    file_size_2 = fake.random_int()
    file_size_3 = fake.random_int()

    f1 = File("test1.txt", file_size_1)
    f2 = File("test2.txt", file_size_2)
    f3 = File("test3.txt", file_size_3)


    folder = Folder("test_folder", [f1, f2, f3])

    assert folder.get_size() == file_size_1 + file_size_2 + file_size_3