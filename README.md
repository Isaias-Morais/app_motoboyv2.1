# 🚀 App Motoboy V2

Aplicação desenvolvida em **Python + FastAPI** para ajudar motoboys a controlarem **ganhos reais**, **custos por km**, **manutenção da moto** e **lucro líquido diário/mensal**.

O projeto começou como uma aplicação local em Python e evoluiu para uma **API REST completa**, utilizando banco de dados relacional, autenticação e arquitetura em camadas.

Projeto desenvolvido com foco em **aprendizado prático**, organização de código e criação de uma solução próxima de um produto real.

---

## 🌐 API

A API não está publicada no momento. Para usá-la localmente, inicie o backend; a API ficará disponível em `http://127.0.0.1:8000` e a documentação Swagger em `http://127.0.0.1:8000/docs`.

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

Crie um arquivo `.env` na raiz do projeto e configure `DATABASE_URL` com a conexão PostgreSQL e `SECRET_KEY` com um valor aleatório de pelo menos 32 bytes. A API rejeita inicialização se a chave JWT estiver ausente ou curta. Opcionalmente, defina `CORS_ALLOWED_ORIGINS` como uma lista separada por vírgulas com as origens permitidas do frontend. Para validar mudanças, prefira um banco local separado do banco com seus dados reais. Exemplo de formato (substitua pelos dados do seu PostgreSQL):

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@127.0.0.1:5432/app_motoboy_teste
SECRET_KEY=coloque_aqui_uma_chave_aleatoria_com_pelo_menos_32_bytes
```

Execute:

```bash
uvicorn backend.app.main:app --reload
```

### Teste local ponta a ponta

Com o PostgreSQL local preparado e o `.env` apontando para o banco de teste, abra um terminal na raiz do projeto e inicie a API:

```bash
uvicorn backend.app.main:app --reload
```

Confirme que `http://127.0.0.1:8000/docs` abre. Em outro terminal, na raiz do projeto, instale as dependências JavaScript e o Chromium do Playwright uma vez:

```bash
npm install
npx playwright install chromium
```

Com a API ainda rodando, execute:

```bash
npm run test:e2e
```

O teste inicia automaticamente o servidor estático do frontend em `http://127.0.0.1:4173`, cria uma conta com e-mail aleatório e percorre cadastro, login, moto, trabalho, abastecimento, manutenção, dashboard e relatório. Os registros criados ficam no banco configurado em `DATABASE_URL`; por isso, aponte para um banco de teste separado quando quiser manter seus dados reais intactos. O teste não apaga esses registros.

Para usar outros endereços, configure `E2E_API_URL` e `E2E_BASE_URL` antes de executar o teste.

---

## 🛣️ Próximos Passos

* Criar frontend web/mobile
* Criar PWA para uso no celular
* Melhorar relatórios financeiros
* Adicionar gráficos
* Implementar notificações
* Ampliar os testes automatizados para cenários de erro e segurança

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
