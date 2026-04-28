# ADR 001: Arquitetura em Camadas

**Data:** 28 de Abril de 2026
**Status:** Aceito

## Contexto
O sistema original estava em um arquivo único, dificultando a manutenção (RNF03) e os testes (RNF04).

## Opções Consideradas
- **Arquivo Único:** Simples, mas desorganizado.
- **MVC:** Muito complexo para este caso.
- **Camadas:** Melhor equilíbrio para um sistema CLI (Linha de Comando).

## Decisão
Adotamos a Arquitetura em Camadas:
- `app/`: Interface com o usuário.
- `core/`: Regras de negócio e cálculos.
- `data/`: Armazenamento de informações.

## Consequências
Melhor organização e facilidade para testar as regras de multas sem depender do menu.
