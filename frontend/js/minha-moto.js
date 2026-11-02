const { requisicao: chamarApi, mensagemErro: formatarErro, numero: formatarNumero } = window.MotoboyApi;

const mensagem = document.getElementById("mensagem-moto");
const titulo = document.getElementById("moto-titulo");
const modelo = document.getElementById("moto-modelo");
const ano = document.getElementById("moto-ano");
const quilometragem = document.getElementById("moto-km");
const consumo = document.getElementById("moto-consumo");
const telaMoto = document.querySelector(".tela-minha-moto");

function exibirMoto(moto) {
    titulo.textContent = `${moto.marca} ${moto.modelo}`;
    modelo.textContent = moto.modelo;
    ano.textContent = moto.ano;
    quilometragem.textContent = `${formatarNumero(moto.quilometragem)} km`;
    consumo.textContent = `${formatarNumero(moto.consumo)} km/L`;
}

function exibirErro(erro) {
    mensagem.textContent = `${formatarErro(erro)} `;
    const link = document.createElement("a");
    link.href = "criar-moto.html";
    link.textContent = "Cadastrar moto";
    mensagem.append(link);
    mensagem.classList.add("status--erro");
}

function criarSeletorMoto(motos, motoAtiva) {
    if (motos.length < 2) {
        return;
    }

    const secao = document.createElement("section");
    secao.className = "card";
    secao.innerHTML = `
        <h2>Trocar moto ativa</h2>
        <div class="campo">
            <label for="moto-ativa">Moto usada nos próximos registros</label>
            <select id="moto-ativa"></select>
        </div>
        <button class="button" id="btn-trocar-moto" type="button">ATIVAR MOTO</button>
        <button class="button" id="btn-excluir-moto" type="button">EXCLUIR MOTO SELECIONADA</button>
        <p class="status" id="mensagem-moto-ativa" role="status" aria-live="polite"></p>
    `;

    const seletor = secao.querySelector("#moto-ativa");
    const botao = secao.querySelector("#btn-trocar-moto");
    const botaoExcluir = secao.querySelector("#btn-excluir-moto");
    const status = secao.querySelector("#mensagem-moto-ativa");

    motos.forEach((moto) => {
        const opcao = document.createElement("option");
        opcao.value = moto.id;
        opcao.textContent = `${moto.marca} ${moto.modelo} — ${formatarNumero(moto.quilometragem)} km`;
        opcao.selected = moto.id === motoAtiva.id;
        seletor.append(opcao);
    });

    botao.addEventListener("click", async () => {
        const motoId = Number(seletor.value);
        botao.disabled = true;
        status.textContent = "";
        status.classList.remove("status--erro");

        try {
            await chamarApi(`/Motoboy/ativa/moto?moto_id=${motoId}`, {
                method: "PATCH"
            });

            const motoSelecionada = motos.find((moto) => moto.id === motoId);
            exibirMoto(motoSelecionada);
            status.textContent = "Moto ativa alterada com sucesso.";
        } catch (erro) {
            status.textContent = formatarErro(erro);
            status.classList.add("status--erro");
        } finally {
            botao.disabled = false;
        }
    });

    botaoExcluir.addEventListener("click", async () => {
        const motoId = Number(seletor.value);

        if (motoId === motoAtiva.id) {
            status.textContent = "Ative outra moto antes de excluir a moto ativa.";
            status.classList.add("status--erro");
            return;
        }

        const motoSelecionada = motos.find((moto) => moto.id === motoId);
        const confirmar = window.confirm(
            `Excluir ${motoSelecionada.marca} ${motoSelecionada.modelo}? Esta ação não pode ser desfeita.`
        );

        if (!confirmar) {
            return;
        }

        botaoExcluir.disabled = true;
        status.textContent = "";
        status.classList.remove("status--erro");

        try {
            await chamarApi(`/moto/delete?moto_id=${motoId}`, {
                method: "DELETE"
            });
            window.location.reload();
        } catch (erro) {
            status.textContent = formatarErro(erro);
            status.classList.add("status--erro");
            botaoExcluir.disabled = false;
        }
    });

    telaMoto.append(secao);
}

async function carregarPagina() {
    const [motoAtiva, motos] = await Promise.all([
        chamarApi("/Motoboy/busca/moto"),
        chamarApi("/moto/motos")
    ]);

    exibirMoto(motoAtiva);
    criarSeletorMoto(motos, motoAtiva);
}

carregarPagina().catch(exibirErro);
