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

Configure `SECRET_KEY` com um valor aleatório de pelo menos 32 bytes e `DATABASE_URL` com a conexão do banco. A API rejeita inicialização se a chave JWT estiver ausente ou curta. Em produção, configure também `CORS_ALLOWED_ORIGINS` como uma lista separada por vírgulas contendo apenas as origens do frontend, por exemplo `https://seu-frontend.example`.

Execute:

```bash
uvicorn main:app --reload
```

### Teste ponta a ponta

Instale as dependências JavaScript e o Chromium do Playwright uma vez:

```bash
npm install
npx playwright install chromium
```

Com a API local rodando em `http://127.0.0.1:8000`, execute:

```bash
npm run test:e2e
```

O teste inicia automaticamente o servidor estático do frontend em `http://127.0.0.1:4173`, cria uma conta com e-mail aleatório e percorre cadastro, login, moto, trabalho, abastecimento, manutenção, dashboard e relatório. Os registros de teste ficam no banco usado pela API.

Para usar outros endereços, configure `E2E_API_URL` e `E2E_BASE_URL` antes de executar o teste.

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
