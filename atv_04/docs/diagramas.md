# Problemas do Sistema de Empréstimos

## 1. Revisão com Vocabulário Técnico (SRP e Coesão)

* **Baixa Coesão e Violação de SRP**: O arquivo original `emprestimos.py` mistura lógica de negócio, persistência de dados e notificações por e-mail. Isso força mudanças no código por motivos distintos, ferindo o Princípio da Responsabilidade Única.
* **Acoplamento por Estado Global**: O uso de listas globais para armazenar equipamentos e empréstimos gera um acoplamento alto e dificulta o ocultamento de informações.
* **Falta de Separação de Responsabilidades**: A interface de linha de comando (CLI) está acoplada às regras de negócio, impedindo a reutilização da lógica em outras interfaces.
* **Ausência de Contratos Tipados**: O uso de dicionários puros expõe a estrutura interna dos dados e facilita erros de tempo de execução por falta de tipagem formal.