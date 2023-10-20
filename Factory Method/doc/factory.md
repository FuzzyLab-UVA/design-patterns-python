# Factory

A Factory que nós estamos utilizando é para reutilizar o banco de dados sem ter que quebrar o código, assim retornando o banco de dados pelo método `create()`

```python
    @staticmethod
    def create() -> Usecase:
        return  Usecase(MysqlRepository())
```