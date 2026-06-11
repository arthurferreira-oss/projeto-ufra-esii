## Aula 08 — Testes de Unidade vs. Integração

O teste de integração captura a interação viva e as conexões de contratos entre dependências reais do software, mapeando erros de acoplamento estrutural e efeitos colaterais globais que os dublês de testes (como Fakes e Spies) naturalmente mascaram.

Por outro lado, ele falha em mapear com precisão fluxos complexos de exceções e tratamentos granulares. É aí que o teste de unidade se sobressai, isolando componentes para exatidão lógica sob controle total de dados.



## Aula 10 — Factory e Facade

Na implementação da FabricaEquipamento, o uso de um dicionário para mapear o tipo de equipamento à sua classe concreta ainda concentra uma decisão baseada em tipo. Embora o Princípio Aberto/Fechado (OCP) busque evitar estruturas condicionais espalhadas, centralizar essa lógica na fábrica é perfeitamente aceitável. Como aponta Valente (Capítulo 6), a fábrica assume a responsabilidade de "pagar o preço" desse acoplamento em um único ponto isolado do sistema. Dessa forma, o repositório e as demais camadas ficam completamente protegidos e livres de conhecer as subclasses concretas, simplificando futuras extensões de novos tipos de equipamentos.

Por outro lado, a introdução da fachada SistemaDeEmprestimos não desfaz o Princípio da Inversão de Dependência (DIP) consolidado na Aula 6. A Facade atua estritamente como a "raiz de composição" do ambiente de produção, onde os componentes concretos (repositório real e notificador) são finalmente conectados para uso do main.py. O desacoplamento do core do sistema permanece intacto, o que é demonstrado pelo fato de que a suíte de testes de unidade e integração continua injetando diretamente os dublês de teste (como RepositorioFake) no ServicoEmprestimo, rodando de forma isolada e sem qualquer dependência ou modificação na fachada.