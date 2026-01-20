# 🚀 App Motoboy V2

Aplicação em **Python + PostgreSQL** para ajudar motoboys a controlarem **ganhos reais**, **custos por km**, **manutenção da moto** e **lucro líquido diário/mensal**.

Projeto desenvolvido com foco em **aprendizado prático**, **evolução de arquitetura** e uso real no dia a dia.

---

## 🔄 Atualização Importante

> Esta versão do projeto marca a **migração do SQLite para PostgreSQL**, trazendo mais robustez, escalabilidade e proximidade com ambientes profissionais de produção.

---

## 🎯 Objetivo do Projeto

Criar um app simples e funcional que permita ao motoboy:

* Registrar ganhos diários
* Registrar quilometragem rodada
* Controlar abastecimentos
* Controlar manutenções da moto
* Calcular custo por km
* Calcular lucro líquido do dia
* Visualizar histórico de trabalho

---

## 🧱 Tecnologias Utilizadas

* Python 3
* **PostgreSQL**
* SQL
* Programação Orientada a Objetos (POO)
* Arquitetura em camadas:

  * `modelos`
  * `repositorios`
  * `servicos`
  * `utilidades`

---

## ⚙️ Funcionalidades Atuais

* Cadastro de motoboy
* Cadastro de moto vinculada ao motoboy
* Registro de abastecimento
* Registro de manutenção
* Registro de dia de trabalho
* Cálculo de:

  * Quilometragem diária
  * Ganho bruto
  * Custos do dia
  * Lucro líquido

---

## 🧮 Lógica de Cálculo (Resumo)

* **KM do dia** = quilometragem final − quilometragem inicial
* **Custo de manutenção** = custo médio por km × km rodado
* **Lucro líquido** = ganho bruto − (combustível + manutenção)

---

## 🛣️ Próximos Passos

* Melhorar interface no terminal
* Relatórios mensais e comparativos
* Exportação de dados (CSV / PDF)
* API REST com FastAPI
* Interface web ou mobile
* Autenticação de usuários

---

## 🧠 Aprendizados

Este projeto foi criado para consolidar conhecimentos em:

* SQL aplicado a cenários reais
* PostgreSQL na prática
* Organização e escalabilidade de projeto
* Separação de responsabilidades
* Pensamento de produto real
* Backend Python aplicado ao dia a dia

---

## 👊 Autor

Projeto desenvolvido por **Isaias Morais**, estudante de programação e motoboy, com foco em **backend Python**, **bancos de dados relacionais** e aplicações reais.
