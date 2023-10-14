# Interface Shipping

```python
class IShipping(ABC):
    @abstractmethod
    def calculate(self, order: Order) -> float:
        pass
```

É uma interface que quando herdada faz com que o método receba um *order* da classe `Order`