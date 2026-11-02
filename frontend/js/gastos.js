const { requisicao, mensagemErro, moeda } = window.MotoboyApi;
const form = document.getElementById("form-gasto");
const tipo = document.getElementById("tipo");
const mensagem = document.getElementById("mensagem-gasto");
const botao = document.getElementById("btn-gasto");
const lista = document.getElementById("lista-gastos");
const campos = { posto: document.getElementById("campo-posto"), litros: document.getElementById("campo-litros"), tanque: document.getElementById("campo-tanque"), descricao: document.getElementById("campo-descricao") };
const campoData = document.getElementById("data");

function atualizarTipo() {
    const abastecimento = tipo.value === "abastecimento";
    campos.posto.classList.toggle("campo--oculto", !abastecimento);
    campos.litros.classList.toggle("campo--oculto", !abastecimento);
    campos.tanque.classList.toggle("campo--oculto", !abastecimento);
    campos.descricao.classList.toggle("campo--oculto", abastecimento);
    document.getElementById("posto").required = abastecimento;
    document.getElementById("litros").required = abastecimento;
    document.getElementById("descricao").required = !abastecimento;
}

function formatarData(valor) { return valor ? new Intl.DateTimeFormat("pt-BR").format(new Date(`${valor}T00:00:00`)) : ""; }
function renderizarGastos(abastecimentos, manutencoes) {
    const gastos = [...abastecimentos.map((item) => ({ titulo: "Abastecimento", data: item.data_abastecimento, valor: item.valor })), ...manutencoes.map((item) => ({ titulo: item.tipo || "Manutenção", data: item.data_manutencao, valor: item.valor }))].sort((a, b) => String(b.data).localeCompare(String(a.data))).slice(0, 6);
    lista.innerHTML = gastos.length ? gastos.map((item) => `<article class="lista-item"><div><strong>${item.titulo}</strong><small>${formatarData(item.data)}</small></div><strong class="valor">${moeda(item.valor)}</strong></article>`).join("") : '<p class="status">Nenhum gasto registrado.</p>';
}
async function carregarGastos() {
    const resultados = await Promise.allSettled([requisicao("/abastecimento/list"), requisicao("/manutencao/list")]);
    renderizarGastos(resultados[0].status === "fulfilled" ? resultados[0].value : [], resultados[1].status === "fulfilled" ? resultados[1].value : []);
}
tipo.addEventListener("change", atualizarTipo);
atualizarTipo();
campoData.value = new Date().toISOString().slice(0, 10);
form.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    const abastecimento = tipo.value === "abastecimento";
    const valor = Number(document.getElementById("valor").value);
    const quilometragem = Number(document.getElementById("quilometragem").value);
    botao.disabled = true; botao.textContent = "SALVANDO..."; mensagem.textContent = ""; mensagem.classList.remove("status--erro");
    try {
        const corpo = abastecimento ? { data: campoData.value, posto: document.getElementById("posto").value, litros: Number(document.getElementById("litros").value), valor, tanque_completo: document.getElementById("tanque-completo").checked, quilometragem_abastecimento: quilometragem } : { data_manutencao: campoData.value, tipo: "Manutenção", descricao: document.getElementById("descricao").value, valor, quilometragem_manutencao: quilometragem };
        await requisicao(abastecimento ? "/abastecimento/create" : "/manutencao/create", { method: "POST", body: JSON.stringify(corpo) });
        mensagem.textContent = "Gasto registrado com sucesso."; form.reset(); tipo.value = abastecimento ? "abastecimento" : "manutencao"; campoData.value = new Date().toISOString().slice(0, 10); atualizarTipo(); await carregarGastos();
    } catch (erro) { mensagem.textContent = mensagemErro(erro); mensagem.classList.add("status--erro"); }
    finally { botao.disabled = false; botao.textContent = "REGISTRAR GASTO"; }
});
carregarGastos().catch((erro) => { lista.innerHTML = `<p class="status status--erro">${mensagemErro(erro)}</p>`; });
