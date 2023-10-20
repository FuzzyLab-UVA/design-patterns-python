# Factory Method

O Factory Method tem o seguinte diagrama de classes:

![Diagrama Factory](../../Image/diagrama_factory.jpg)

O Factory Method ele serve justamente para que não tenhamos re-trabalho ao trocar uma parte do nosso código, pois não vamos intanciar aquela parte diretamente, mas sim a `Factory` que vai trazer um objeto padrão com uma interface pradrão.

> Nesse exemplo estamos utilizando um caso muito comum que é troca de banco de dados.

## Interface

- [IDatabase](./idatabase.md)

## Controllers

- [Factory](./factory.md)

- [Database](./database.md)

## Models

- [UseCase](./usecase.md)

---

# Referências

- [Factory Method em Python](https://refactoring.guru/pt-br/design-patterns/factory-method/python/example#:~:text=O%20Factory%20method%20é%20um,ao%20construtor%20(operador%20new%20).)
