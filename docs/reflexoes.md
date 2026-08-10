## Aula 08 — Testes de Unidade vs. Integração

O teste de integração captura a interação viva e as conexões de contratos entre dependências reais do software, mapeando erros de acoplamento estrutural e efeitos colaterais globais que os dublês de testes (como Fakes e Spies) naturalmente mascaram.

Por outro lado, ele falha em mapear com precisão fluxos complexos de exceções e tratamentos granulares. É aí que o teste de unidade se sobressai, isolando componentes para exatidão lógica sob controle total de dados.



## Aula 10 — Factory e Facade

Na implementação da FabricaEquipamento, o uso de um dicionário para mapear o tipo de equipamento à sua classe concreta ainda concentra uma decisão baseada em tipo. Embora o Princípio Aberto/Fechado (OCP) busque evitar estruturas condicionais espalhadas, centralizar essa lógica na fábrica é perfeitamente aceitável. Como aponta Valente (Capítulo 6), a fábrica assume a responsabilidade de "pagar o preço" desse acoplamento em um único ponto isolado do sistema. Dessa forma, o repositório e as demais camadas ficam completamente protegidos e livres de conhecer as subclasses concretas, simplificando futuras extensões de novos tipos de equipamentos.

Por outro lado, a introdução da fachada SistemaDeEmprestimos não desfaz o Princípio da Inversão de Dependência (DIP) consolidado na Aula 6. A Facade atua estritamente como a "raiz de composição" do ambiente de produção, onde os componentes concretos (repositório real e notificador) são finalmente conectados para uso do main.py. O desacoplamento do core do sistema permanece intacto, o que é demonstrado pelo fato de que a suíte de testes de unidade e integração continua injetando diretamente os dublês de teste (como RepositorioFake) no ServicoEmprestimo, rodando de forma isolada e sem qualquer dependência ou modificação na fachada.

## Aula 12 — Refactoring e Code Smells

A presença de uma suíte automatizada de testes (`pytest`) atuou como a principal rede de segurança durante o processo de refatoração. A cada pequeno ajuste mecânico — como a transição do `dict` genérico para a `@dataclass Evento` e as extrações de métodos —, a execução do `pytest -v` confirmou a preservação do comportamento observável do sistema. Como aponta Valente (Cap. 9), refatorar sem testes é um risco elevado, pois não há garantias imediatas de que a qualidade interna melhorou sem introduzir regressões ao comportamento público.

Além disso, foi necessário reconhecer falsos positivos na estrutura. As subclasses `Notebook`, `Projetor` e `Cabo`, embora pareçam esvaziadas (*Data Class* ou *Lazy Class*) após a introdução do padrão Strategy na Aula 11, mantêm-se cruciais para a identidade de tipo do domínio e para a aplicação do Princípio Aberto/Fechado (OCP). Aplicar *Inline Class* ou mover a lógica de volta para elas desestruturaria o padrão Strategy e reverteria os gains arquiteturais já consolidados.