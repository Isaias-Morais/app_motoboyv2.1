const {
    requisicao,
    mensagemErro,
    moeda,
    numero
} = window.MotoboyApi;

const mensagem = document.getElementById("mensagem-dashboard");

requisicao("/dashboard/resumo")
    .then((dados) => {
        document.getElementById("lucro-liquido").textContent =
            moeda(dados.lucro_liquido);

        document.getElementById("ganhos").textContent =
            moeda(dados.lucro_bruto);

        const gastos =
            (Number(dados.gasto_media_abastecimento) || 0) +
            (Number(dados.gasto_medio_manutencao) || 0);

        document.getElementById("gastos").textContent =
            moeda(gastos);

        document.getElementById("km-rodados").textContent =
            `${numero(dados.km_rodados)} km`;
    })
    .catch((erro) => {
        mensagem.textContent = mensagemErro(erro);
        mensagem.classList.add("status--erro");
    });
