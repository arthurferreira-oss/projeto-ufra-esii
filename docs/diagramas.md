# Diagramas do Sistema

## Diagrama de classes — v2.0

```mermaid
classDiagram
    class IRepositorioEmprestimo {
        <<interface>>
        +buscar_equipamento(id: int) Equipamento
        +salvar_emprestimo(emprestimo: Emprestimo) void
        +buscar_emprestimo(id: int) Emprestimo
        +marcar_indisponivel(equip_id: int) void
        +marcar_disponivel(equip_id: int) void
        +marcar_devolvido(emprestimo_id: int) void
        +listar_em_atraso() List
        +proximo_id_emprestimo() int
    }

    class INotificador {
        <<interface>>
        +notificar_emprestimo(email: str, data_devolucao: Date) void
        +notificar_devolucao(email: str, multa: float) void
        +notificar_atraso(email: str) void
    }

    class RepositorioEmprestimo {
        -_equipamentos: List
        -_emprestimos: List
        +buscar_equipamento(id: int) Equipamento
        +salvar_emprestimo(emprestimo: Emprestimo) void
    }

    class Notificador {
        +notificar_emprestimo(email: str, data_devolucao: Date) void
    }

    class ServicoEmprestimo {
        -repositorio: IRepositorioEmprestimo
        -notificador: INotificador
        +__init__(repositorio: IRepositorioEmprestimo, notificador: INotificador)
        +registrar(equipamento_id: int, usuario: str, email: str, dias: int) bool
        +devolver(emprestimo_id: int) void
    }

    class Equipamento {
        <<abstract>>
        +id: int
        +nome: str
        +tipo: str
        +disponivel: bool
        +calcular_multa(dias: int)* float
    }

    class Notebook { +calcular_multa(dias: int) float }
    class Projetor { +calcular_multa(dias: int) float }
    class Cabo { +calcular_multa(dias: int) float }

    class Emprestimo {
        +id: int
        +equipamento_id: int
        +usuario: str
        +email: str
        +data_devolucao: Date
        +devolvido: bool
    }

    ServicoEmprestimo --> IRepositorioEmprestimo : usa
    ServicoEmprestimo --> INotificador : usa
    RepositorioEmprestimo ..|> IRepositorioEmprestimo : implementa
    Notificador ..|> INotificador : implementa
    Equipamento <|-- Notebook
    Equipamento <|-- Projetor
    Equipamento <|-- Cabo
    RepositorioEmprestimo o-- Equipamento : agrega
    RepositorioEmprestimo o-- Emprestimo : agrega