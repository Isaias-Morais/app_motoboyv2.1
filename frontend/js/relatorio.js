const { requisicao: chamarApi, mensagemErro: formatarErro, moeda: formatarMoeda, numero: formatarNumero } = window.MotoboyApi;
const form = document.getElementById("form-relatorio");
const inicio = document.getElementById("data-inicio");
const fim = document.getElementById("data-fim");
const botao = document.getElementById("btn-relatorio");
const mensagem = document.getElementById("mensagem-relatorio");
const definirTexto = (id, valor) => { document.getElementById(id).textContent = valor; };
function mensagemStatus(texto, erro = false) { mensagem.textContent = texto; mensagem.classList.toggle("status--erro", erro); }
function exibirDados(dados) {
    definirTexto("total-ganhos", formatarMoeda(dados.ganhos)); definirTexto("total-gastos", formatarMoeda(dados.gastos)); definirTexto("lucro-liquido", formatarMoeda(dados.lucro_liquido)); definirTexto("km-rodados", `${formatarNumero(dados.km_rodados)} km`); definirTexto("dias-trabalhados", `${formatarNumero(dados.total_dias_trabalhados)} dias`); definirTexto("media-ganhos", formatarMoeda(dados.media_ganhos_por_dia)); definirTexto("media-gastos", formatarMoeda(dados.media_gastos_por_dia)); definirTexto("media-lucro", formatarMoeda(dados.lucro_medio_por_dia)); definirTexto("custo-km", formatarMoeda(dados.custo_por_km));
}
form.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    if (!inicio.value || !fim.value) return mensagemStatus("Informe a data inicial e a data final.", true);
    if (inicio.value > fim.value) return mensagemStatus("A data inicial não pode ser posterior à data final.", true);
    botao.disabled = true; botao.textContent = "CARREGANDO..."; mensagemStatus("Buscando os dados do período...");
    try {
        const parametros = new URLSearchParams({ data_inicio: inicio.value, data_fim: fim.value });
        const dados = await chamarApi(`/dashboard/relatorio?${parametros}`);
        exibirDados(dados); mensagemStatus("Relatório atualizado com sucesso.");
    } catch (erro) { mensagemStatus(formatarErro(erro), true); }
    finally { botao.disabled = false; botao.textContent = "GERAR RELATÓRIO"; }
});
const hoje = new Date();
const ano = hoje.getFullYear();
const mes = String(hoje.getMonth() + 1).padStart(2, "0");
inicio.value = `${ano}-${mes}-01`;
fim.value = `${ano}-${mes}-${String(new Date(ano, hoje.getMonth() + 1, 0).getDate()).padStart(2, "0")}`;
