const { requisicao, mensagemErro } = window.MotoboyApi;
const form = document.getElementById("form-registro");
const botao = document.getElementById("btn-registro");
const mensagem = document.getElementById("mensagem-registro");
const campoData = document.getElementById("data");
campoData.value = new Date().toISOString().slice(0, 10);
form.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    const inicial = Number(document.getElementById("km-inicial").value);
    const final = Number(document.getElementById("km-final").value);
    if (final <= inicial) { mensagem.textContent = "A quilometragem final deve ser maior que a inicial."; mensagem.classList.add("status--erro"); return; }
    botao.disabled = true; botao.textContent = "SALVANDO..."; mensagem.textContent = ""; mensagem.classList.remove("status--erro");
    try {
        await requisicao("/dia_de_trabalhada/create", { method: "POST", body: JSON.stringify({ data_trabalhada: campoData.value, ganho_bruto: Number(document.getElementById("ganhos").value), quilometragem_inicial: inicial, quilometragem_final: final }) });
        mensagem.textContent = "Dia de trabalho registrado com sucesso."; form.reset(); campoData.value = new Date().toISOString().slice(0, 10);
    } catch (erro) { mensagem.textContent = mensagemErro(erro); mensagem.classList.add("status--erro"); }
    finally { botao.disabled = false; botao.textContent = "SALVAR REGISTRO"; }
});
