# Diagnóstico de Code Smells — Aula 12

| # | Arquivo:linha | Smell (Nome Técnico) | Refactoring Proposto | Justificativa |
|---|---|---|---|---|
| 1 | `services/servico_emprestimo.py` | Primitive Obsession | Replace Primitive with Object | Substituição de dicionário genérico pela `@dataclass Evento`. |
| 2 | `services/servico_emprestimo.py:12` | Mysterious Name | Rename | Ajuste dos nomes de variáveis para revelar a intenção das regras. |
| 3 | `services/servico_emprestimo.py:65` | Long Method | Extract Function | Isolamento da emissão de e-mail de atraso no método privado `_notificar_atraso`. |
| 4 | `services/servico_emprestimo.py:70` | Comments | Rename / Extract Function | Remoção de comentários redundantes que descreviam o comportamento do código. |
| 5 | `models/equipamentos.py` | Data Class (Smell Aparente) | *Não refatorar* | As subclasses `Notebook`, `Projetor` e `Cabo` atuam como rótulos de tipo após o Strategy. Aplicar *Inline Class* quebraria o OCP. |