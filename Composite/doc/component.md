# Component

Essa interface faz com que as sub-classes que a implementem obrigatóriamente utilizem esse método:

```python
class IComponent(ABC):

    @abstractmethod
    def get_size(self) -> float:
        pass
```