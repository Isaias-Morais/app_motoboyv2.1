# 🚀 App Motoboy V2

Aplicação desenvolvida em **Python + FastAPI** para ajudar motoboys a controlarem **ganhos reais**, **custos por km**, **manutenção da moto** e **lucro líquido diário/mensal**.

O projeto começou como uma aplicação local em Python e evoluiu para uma **API REST completa**, utilizando banco de dados relacional, autenticação e arquitetura em camadas.

Projeto desenvolvido com foco em **aprendizado prático**, organização de código e criação de uma solução próxima de um produto real.

---

## 🌐 API Online

A API está disponível em:

```
https://app-motoboyv2-1.onrender.com
```

Documentação Swagger:

```
https://app-motoboyv2-1.onrender.com/docs
```

---

## 🎯 Objetivo do Projeto

Criar uma solução para que motoboys possam:

* Registrar ganhos diários
* Controlar quilometragem rodada
* Registrar abastecimentos
* Registrar manutenções da moto
* Calcular custos operacionais
* Analisar lucro líquido
* Acompanhar indicadores financeiros

---

## 🧱 Tecnologias Utilizadas

### Backend

* Python 3
* FastAPI
* SQLAlchemy ORM
* Pydantic
* Uvicorn
* JWT Authentication

### Banco de Dados

* PostgreSQL
* SQL

### Arquitetura

* Programação Orientada a Objetos (POO)
* Arquitetura em camadas

Estrutura:

```
models/
schemas/
repositories/
services/
routers/
validators/
database/
security/
```

---

## ⚙️ Funcionalidades Atuais

### Cadastro e gerenciamento

✅ Cadastro de motoboy  
✅ Cadastro de moto vinculada ao motoboy  
✅ Autenticação com JWT  

### Controle financeiro

✅ Registro de abastecimentos  
✅ Registro de manutenções  
✅ Registro de dias trabalhados  

### Dashboard

✅ Quilometragem diária  
✅ Ganho bruto  
✅ Custos com combustível  
✅ Custos com manutenção  
✅ Custo médio por km  
✅ Lucro líquido  

---

## 🧮 Lógica de Cálculo

### Quilometragem rodada

```
KM rodado = KM final - KM inicial
```

### Custo combustível por KM

```
Combustível por KM = valor gasto / KM percorrido
```

### Lucro líquido

```
Lucro líquido =
ganho bruto - (combustível + manutenção)
```

---

## ▶️ Como Executar Localmente

Clone o projeto:

```bash
git clone https://github.com/Isaias-Morais/app_motoboyv2.1.git
```

Entre na pasta:

```bash
cd app_motoboyv2.1
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente:

Crie um arquivo `.env` baseado no:

```
.env.example
```

Execute:

```bash
uvicorn main:app --reload
```

---

## 🛣️ Próximos Passos

* Criar frontend web/mobile
* Criar PWA para uso no celular
* Melhorar relatórios financeiros
* Adicionar gráficos
* Implementar notificações
* Criar testes automatizados

---

## 🧠 Aprendizados

Este projeto ajudou a consolidar conhecimentos em:

* Desenvolvimento de APIs REST
* FastAPI na prática
* Banco de dados relacional
* SQLAlchemy ORM
* Autenticação JWT
* Organização de código
* Separação de responsabilidades
* Desenvolvimento orientado a problemas reais

---

## 👊 Autor

Projeto desenvolvido por **Isaias Morais**, estudante de programação com foco em **Backend Python**.

A ideia do projeto nasceu de uma necessidade real do dia a dia de motoboys, buscando transformar um problema financeiro comum em uma solução utilizando tecnologia.