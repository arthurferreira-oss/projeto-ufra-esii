# main.py
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from services.servico_emprestimo import ServicoEmprestimo

if __name__ == "__main__":
    repo = RepositorioEmprestimo()
    notif = Notificador()
    srv = ServicoEmprestimo(repo, notif)
    srv.registrar(1, "Arthur", "arthur@ufra.edu.br", 7)
    print("Código base rodando perfeitamente v2.0!")