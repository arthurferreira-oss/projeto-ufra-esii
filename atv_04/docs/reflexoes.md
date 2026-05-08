**Reflexões sobre a Refatoração e SRP**

Nesta atividade, substituir o script monolítico emprestimos.py por uma estrutura em camadas ajudou a visualizar, na prática, os conceitos de Coesão e Acoplamento. O maior desafio foi definir o limite entre o que é regra de negócio e o que é suporte, como no caso das notificações.

Ao criar a classe Notificador, o ServicoEmprestimo ficou muito mais limpo e focado. Antes, uma única parte do código cuidava de dados e de avisos no console; agora, o serviço apenas coordena o processo. Isso diminui o acoplamento: se amanhã precisarmos trocar o print por um envio de e-mail real, mexeremos apenas no notificador.py, sem o risco de quebrar a lógica principal do sistema.

A introdução dos Repositórios também foi essencial para acabar com as variáveis globais, que tornavam o código instável e difícil de manter. Além disso, trocar dicionários genéricos por Dataclasses trouxe "contratos" claros para o Equipamento e o Emprestimo, o que evita erros de tipagem e deixa o código mais seguro. No fim das contas, aplicar o SRP não é só uma questão de organização, mas de preparar o software para crescer com qualidade.