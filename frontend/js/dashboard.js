const {
    requisicao: chamarApi,
    mensagemErro: formatarErro,
    moeda: formatarMoeda,
    numero: formatarNumero
} = window.MotoboyApi;

const mensagem = document.getElementById("mensagem-dashboard");
const listaGastos = document.getElementById("lista-gastos-recentes");

function formatarData(data) {
    return new Intl.DateTimeFormat("pt-BR").format(
        new Date(`${data}T00:00:00`)
    );
}

function renderizarGastosRecentes(abastecimentos, manutencoes) {
    const gastos = [
        ...abastecimentos.map((item) => ({
            titulo: "Abastecimento",
            data: item.data_abastecimento,
            valor: item.valor
        })),
        ...manutencoes.map((item) => ({
            titulo: item.tipo || "Manutenção",
            data: item.data_manutencao,
            valor: item.valor
        }))
    ]
        .sort((a, b) => String(b.data).localeCompare(String(a.data)))
        .slice(0, 3);

    listaGastos.replaceChildren();
    if (!gastos.length) {
        const vazio = document.createElement("p");
        vazio.className = "status";
        vazio.textContent = "Nenhum gasto registrado.";
        listaGastos.append(vazio);
        return;
    }

    gastos.forEach((item) => {
        const linha = document.createElement("article");
        linha.className = "lista-item";
        const detalhes = document.createElement("div");
        const titulo = document.createElement("strong");
        titulo.textContent = item.titulo;
        const data = document.createElement("small");
        data.textContent = formatarData(item.data);
        const valor = document.createElement("strong");
        valor.className = "valor";
        valor.textContent = formatarMoeda(item.valor);
        detalhes.append(titulo, data);
        linha.append(detalhes, valor);
        listaGastos.append(linha);
    });
}

chamarApi("/dashboard/resumo")
    .then((dados) => {
        document.getElementById("lucro-liquido").textContent =
            formatarMoeda(dados.lucro_liquido);

        document.getElementById("ganhos").textContent =
            formatarMoeda(dados.lucro_bruto);

        const gastoPorKm =
            (Number(dados.gasto_combustivel_km) || 0) +
            (Number(dados.gasto_manutencao_km) || 0);

        document.getElementById("gastos").textContent =
            `${formatarMoeda(gastoPorKm)}/km`;

        document.getElementById("km-rodados").textContent =
            `${formatarNumero(dados.km_rodados)} km`;
    })
    .catch((erro) => {
        mensagem.textContent = formatarErro(erro);
        mensagem.classList.add("status--erro");
    });

Promise.allSettled([
    chamarApi("/abastecimento/list"),
    chamarApi("/manutencao/list")
]).then((resultados) => {
    renderizarGastosRecentes(
        resultados[0].status === "fulfilled" ? resultados[0].value : [],
        resultados[1].status === "fulfilled" ? resultados[1].value : []
    );
}).catch(() => {
    const falha = document.createElement("p");
    falha.className = "status status--erro";
    falha.textContent = "Não foi possível carregar os gastos.";
    listaGastos.replaceChildren(falha);
});
