## Aula 05 — OCP

A reestruturação do sistema de empréstimos aplicou o Princípio Aberto/Fechado (OCP) ao substituir estruturas condicionais por polimorfismo. Ao transformar a classe Equipamento em uma classe abstrata e delegar o cálculo da multa para subclasses específicas (como Notebook e Projetor), o código tornou-se aberto para extensão, mas fechado para modificação. Isso significa que novos tipos de equipamentos podem ser adicionados ao repositório sem a necessidade de alterar a lógica central no serviço de empréstimo.

Entretanto, essa decomposição possui limites claros. Se surgisse um requisito radicalmente novo, como multas cobradas por hora ou baseadas em políticas variáveis pelo dia da semana, a hierarquia atual baseada apenas no tipo de objeto seria insuficiente. Como destaca Valente no Capítulo 5, o OCP não confere imunidade total contra mudanças, pois "não é possível projetar um sistema que seja 100% aberto a qualquer tipo de mudança". Para suportar variações tão profundas, seria necessário evoluir o design para padrões mais flexíveis, como o Strategy, que separa a regra de cálculo do objeto em si. Portanto, o OCP protege o sistema contra mudanças previstas no eixo de evolução atual, mas exigiria reestruturação caso o eixo de variação mudasse drasticamente.

## Aula 06 — Verificação de LSP

Análise das subclasses de Equipamento (Notebook, Projetor, Cabo):

* **calcular_multa(0) retorna 0.0?** Sim. Para todas as subclasses, se os dias de atraso forem zero, o cálculo resulta em 0.0, respeitando o limite inferior do contrato.
* **calcular_multa(-5) retorna 0.0?** Sim. As regras de negócio implementadas tratam dias negativos (ou barram através de condicionais como `max(0, dias)`), garantindo que dias inválidos não gerem multas negativas ou incoerentes.
* **Alguma pode lançar exceção inesperada?** Não. Nenhuma das subclasses lança exceções (como `ValueError` ou `TypeError`) para argumentos numéricos válidos dentro do escopo do método.

**Conclusão:** O LSP (Princípio da Substituição de Liskov) está satisfeito. Todas as subclasses honram estritamente o contrato da classe base (`Equipamento`), que promete um retorno do tipo `float >= 0.0` sem o lançamento de exceções. O `ServicoEmprestimo` pode interagir com qualquer subclasse de forma genérica sem risco de quebras inesperadas de contrato.

## Aula 06 — DIP

A aplicação do Princípio de Inversão de Dependência (DIP) altera radicalmente a dinâmica de acoplamento entre os módulos do sistema. Antes, o `ServicoEmprestimo` controlava o ciclo de vida de suas dependências, criando diretamente instâncias concretas de repositórios e notificadores. Com o DIP, essa relação é invertida: o serviço deixa de ser um criador autônomo para se tornar um consumidor passivo, que dita os contratos (interfaces) que os provedores externos devem satisfazer.

Essa mudança transcende a mera alteração técnica de passagem de parâmetros no construtor; ela é essencialmente conceitual. Como bem define Marco Tulio Valente em *Engenharia de Software Moderna* (Cap. 5), "módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações". 

Quem passa a deter o controle arquitetural é a camada de negócio (alto nível). O repositório e o notificador de baixo nível tornam-se detalhes de implementação intercambiáveis. Essa inversão de controle desfaz o engessamento do código, isolando as regras de negócio de efeitos colaterais externos. Como demonstrado na prática com os objetos falsos, o DIP é o mecanismo que viabiliza a testabilidade isolada (RNF04), permitindo simular cenários de teste sem infraestrutura real.