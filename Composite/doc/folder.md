# Folder


A classe **Folder** tem os seguintes atributos:

```python
    def __init__(self, name, size):
        self._name: str = name
        self._size: float = size
```

- **Name**: Nome do arquivo

- **Size**: Tamanho do arquivo

Essa classe tem os seguintes métodos:

```python
def get_size(self) -> float:
```

- Essa função serve para dizer qual é o tamanho da pasta, somando todos os arquivos que existem dentro da mesma.

