import sys
sys.path.append('C:\\Users\Paulitos\\Documents\\Apresentações\\Aula de Git E GitHub\\design-patterns-python\\Singleton')
from controllers import SingletonOwner


single = SingletonOwner()


single2 = SingletonOwner()


print(single)

print(single2)
