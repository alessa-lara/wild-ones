Projeto de conclusão da disciplina de tecnologia orientada a objetos.

Este programa é um simulador de ecossistema em que analisamos diversas espécies em um ambiente comum ao longo de um determinado
tempo.

Este projeto tem como intuito aplicar conceitos de programação orientada a objetos e, portanto, não tem como prioridade a simulação
acurada.

```mermaid
classDiagram
    class Creature {
	+int sede
	+int fome
        +float reproducao
        +FeedingBehaviour dieta
	+AgeState idade

        -reproduzir()
    }

    class AgeState {
	+Creature creature

	-advance_age()
    }

    AgeState <|-- StateYoung
    AgeState <|-- StateMature
    AgeState <|-- StateDead

    class Area {
        +float kmQuadrado
        +int populacaoMaxima

        +Water RecursosAgua
        +Set[Plant] recursosPlantas
        +Set[Creature] recursosAnimais

        +arr[Weather] climas
	+Season estacao
    }

    class Weather {
        +tuple(float, float) temperaturaFaixa
        +float umidade
        +float precipitacao

        -variar()
        -mudancaClima()
    }

    class FeedingBehaviour {
        +Set[Resources] canEat
    }

    FeedingBehaviour <|-- Carnivore
    FeedingBehaviour <|-- Omnivore
    FeedingBehaviour <|-- Herbivore
```

Foram utilizados os seguintes padrões de projeto:
- State: Separamos a lógica da idade de uma criatura, fazendo com que dependendo do estado de vida dela (jovem, adulto, morto),
  suas necessidades de água e comida sejam afetados.
- Dependency Injection: Ao invés da propria classe criar suas dependências, deixamos isto como um requisito para a
  inicialização.
