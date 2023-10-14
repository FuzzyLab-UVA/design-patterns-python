# Composite

O Composite ele tem seguinte diagrama de classes.

![Diagram de Classes Composite](../../Image/diagrama_composite.jpg)

Ele é muito utilizado no SOLI**D**, sendo o **D** de Dependence Inversion (Inversão de Dependências).

Aqui nós temos 2 classes herdando de *IComponent*, onde essas classes precisam implementar o método *get_size()*, usando a inversão de dependências quem fica responsavél por delegar o que a função vai realizar são as *sub-classes*.

> Nesse exemplo estamos usando o conceito de pastas do seu computador, onde uma pasta pode ter várias pastas, mas um arquivo só pode ter uma pasta.


## Interface

- [IComponent](./component.md)

## Model

- [Folder](./folder.md)
- [File](./file.md)

---

# Refêrencias

- [Desgin Patterns in Python: Composite Pattern](https://python.plainenglish.io/design-patterns-in-python-composite-pattern-2fa89a026564)

- [Composite em Python](https://refactoring.guru/design-patterns/composite/python/example#:~:text=Composite%20is%20a%20structural%20design,require%20building%20a%20tree%20structure.)