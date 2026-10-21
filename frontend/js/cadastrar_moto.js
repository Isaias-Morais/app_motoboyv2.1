const { requisicao, mensagemErro } = window.MotoboyApi;

const form = document.getElementById("form-moto");
const botao = document.getElementById("btn-moto");
const mensagem = document.getElementById("mensagem-moto");

const campoMarca = document.getElementById("marca");
const campoModelo = document.getElementById("modelo");
const campoAno = document.getElementById("ano");
const campoQuilometragem = document.getElementById("quilometragem");
const campoConsumo = document.getElementById("consumo");

campoAno.value = new Date().getFullYear();

function limparMensagem() {
mensagem.textContent = "";
mensagem.classList.remove("status--erro");
}

function definirEstadoBotao(carregando) {
botao.disabled = carregando;
botao.textContent = carregando
    ? "CADASTRANDO..."
    : "CADASTRAR MOTO";
}

form.addEventListener("submit", async (evento) => {
evento.preventDefault();

limparMensagem();
definirEstadoBotao(true);

const dadosMoto = {
    marca: campoMarca.value.trim(),
    modelo: campoModelo.value.trim(),
    ano: Number(campoAno.value),
    quilometragem: Number(campoQuilometragem.value),
    consumo: Number(campoConsumo.value)
};

try {
    await requisicao("/moto/create", {
        method: "POST",
        body: JSON.stringify(dadosMoto)
    });

    mensagem.textContent =
        "Moto cadastrada com sucesso. Redirecionando...";

    setTimeout(() => {
        window.location.assign("minha-moto.html");
    }, 900);

} catch (erro) {
    mensagem.textContent = mensagemErro(erro);
    mensagem.classList.add("status--erro");

    definirEstadoBotao(false);
}
});