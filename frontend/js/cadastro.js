const { baseUrl, mensagemErro } = window.MotoboyApi;

const form = document.getElementById("form-cadastro");
const botao = document.getElementById("btn-cadastro");
const mensagem = document.getElementById("mensagem-cadastro");

const campoNome = document.getElementById("nome");
const campoEmail = document.getElementById("email");
const campoIdade = document.getElementById("idade");
const campoSenha = document.getElementById("senha");
const campoConfirmacao = document.getElementById("confirmacao-senha");

function exibirErro(texto) {
    mensagem.textContent = texto;
    mensagem.classList.add("status--erro");
}

function limparMensagem() {
    mensagem.textContent = "";
    mensagem.classList.remove("status--erro");
}

function definirEstadoBotao(carregando) {
    botao.disabled = carregando;
    botao.textContent = carregando
        ? "CRIANDO..."
        : "CRIAR CONTA";
}

form.addEventListener("submit", async (evento) => {
    evento.preventDefault();

    const senha = campoSenha.value;
    const confirmacao = campoConfirmacao.value;

    if (senha !== confirmacao) {
        exibirErro("As senhas não coincidem.");
        return;
    }

    limparMensagem();
    definirEstadoBotao(true);

    const dadosCadastro = {
        nome: campoNome.value.trim(),
        email: campoEmail.value.trim(),
        idade: Number(campoIdade.value),
        senha
    };

    try {
        const resposta = await fetch(
            `${baseUrl}/Motoboy/create`,
            {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(dadosCadastro)
            }
        );

        const resultado = await resposta
            .json()
            .catch(() => ({}));

        if (!resposta.ok) {
            throw new Error(
                typeof resultado.detail === "string"
                    ? resultado.detail
                    : "Não foi possível concluir o cadastro."
            );
        }

        mensagem.textContent =
            "Conta criada com sucesso. Redirecionando para o login...";

        setTimeout(() => {
            window.location.assign("login.html");
        }, 1200);
    } catch (erro) {
        exibirErro(mensagemErro(erro));
        definirEstadoBotao(false);
    }
});