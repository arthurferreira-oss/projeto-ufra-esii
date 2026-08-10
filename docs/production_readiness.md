# Production Readiness Checklist — Sistema de Empréstimo UFRA

## 1. Pipeline e Qualidade
| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Pipeline de CI (Lint + Testes + Cobertura) | ✅ OK | feito | Alta | Configurado no GitHub Actions com ruff e pytest. |
| Gate de Cobertura ≥ 80% | ✅ OK | feito | Alta | Cobertura atual em 88.11% configurada em `.coveragerc`. |
| Análise Estática de Tipos (Mypy) | ❌ FALTA | 1 dia | Média | Checagem de tipos estática a ser integrada em ciclo futuro. |

## 2. Containerização
| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Dockerfile Multiestágio | ❌ FALTA | 1 dia | Alta | Ausência de receita de build containerizada. |
| Execução sem usuário Root | ❌ FALTA | 0.5 dia | Alta | Mapear usuário não-privilegiado no container. |
| Arquivo `.dockerignore` | ❌ FALTA | 0.5 dia | Média | Necessário para excluir `.git`, `.pytest_cache` e venv do build. |

## 3. Persistência
| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Persistência de Dados (SGBD) | ⚠️ PARCIAL | 3 dias | Alta | Dados salvos em memória local; perdem-se ao reiniciar o processo. |
| Migrações de Banco de Dados | ❌ FALTA | 2 dias | Alta | Integração necessária via Alembic/SQLAlchemy. |
| Backups Automatizados | ❌ FALTA | 1 dia | Média | Requer infraestrutura externa de SGBD. |

## 4. Segurança
| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Dependências Fixadas e Auditadas | ✅ OK | feito | Alta | Arquivo `requirements-dev.txt` com versões fixadas. |
| Gestão de Credenciais / Variáveis de Ambiente | ⚠️ PARCIAL | 1 dia | Alta | Sem chaves hardcoded no código, mas requer `python-dotenv`. |
| Sanitização de Entradas de Usuário | ⚠️ PARCIAL | 1 dia | Média | Validações básicas aplicadas na CLI, sem suporte a sanitização robusta. |

## 5. Observabilidade
| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Logs Estruturados (Logging Módulo) | ⚠️ PARCIAL | 1 dia | Alta | Notificador utiliza `print()`; substituir pelo módulo `logging`. |
| Coleta de Métricas (Prometheus/OpenTelemetry) | ❌ FALTA | 2 dias | Baixa | Sem métricas de runtime ou contadores de requisição. |
| Healthcheck Endpoints | ❌ FALTA | 0.5 dia | Média | Aplicação CLI sem suporte a verificação de integridade HTTP. |

## 6. Deployment
| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Estratégia de Rollback Automático | ❌ FALTA | 2 dias | Alta | Depende de containerização e orquestrador. |
| Automação de CD (Deployment Pipeline) | ❌ FALTA | 2 dias | Média | Processo manual; sem esteira de CD implementada. |
| Documentação de Runbook / Operação | ❌ FALTA | 1 dia | Baixa | Guia de recuperação de falhas operacionais pendente. |

---

## Síntese executiva

### Ordem de Ataque Prioritária

1. **Persistência de Dados em SGBD (Persistência)**: É a maior vulnerabilidade do sistema. Atualmente, os empréstimos residem apenas em memória RAM e são perdidos a cada encerramento do programa. Sem uma base persistente (PostgreSQL/SQLite), o software não possui utilidade em ambiente real.
2. **Containerização via Dockerfile não-root (Containerização)**: Garantir a reprodutibilidade dos builds e isolamento da aplicação executando sob usuário não-privilegiado. É o pré-requisito técnico para liberar os deployments contínuos e garantir a paridade entre ambientes (Valente, Cap. 10).
3. **Substituição de `print()` por Módulo `logging` Estruturado (Observabilidade)**: O envio de mensagens via stdout sem formatação limita a rastreabilidade de falhas. A adoção do módulo nativo `logging` permite rotear logs para arquivos/agregadores com severidades claras (`INFO`, `ERROR`).

### Dependência Crítica
A **Containerização** destrava diretamente a **Automação de CD e Rollback**. Tentar configurar o deployment contínuo sem uma imagem containerizada reprodutível criaria acoplamento rígido com o servidor, gerando falhas do tipo "na minha máquina funciona" (Valente, Cap. 10).

### Item Adiado
A **Coleta de Métricas (Prometheus)** pode ser postergada. Em uma fase inicial com baixo volume de acessos, os logs estruturados e healthchecks básicos suprem as necessidades operacionais primárias de diagnóstico, tornando a complexidade de um servidor de métricas um custo desnecessário no momento.