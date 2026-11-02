const { baseUrl, mensagemErro: formatarErro } = window.MotoboyApi;
const form = document.getElementById("form-login");
const botao = document.getElementById("btn-login");
const mensagem = document.getElementById("mensagem-login");

form.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    botao.disabled = true;
    botao.textContent = "ENTRANDO...";
    mensagem.textContent = "";
    mensagem.classList.remove("status--erro");
    try {
        const dados = new URLSearchParams({ username: document.getElementById("email").value.trim(), password: document.getElementById("senha").value, grant_type: "password" });
        const resposta = await fetch(`${baseUrl}/Motoboy/auth`, { method: "POST", headers: { Accept: "application/json", "Content-Type": "application/x-www-form-urlencoded" }, body: dados });
        const resultado = await resposta.json().catch(() => ({}));
        if (!resposta.ok || !resultado.access_token) throw new Error(typeof resultado.detail === "string" ? resultado.detail : "Não foi possível entrar.");
        localStorage.setItem("access_token", resultado.access_token);
        window.location.assign("index.html");
    } catch (erro) {
        mensagem.textContent = formatarErro(erro);
        mensagem.classList.add("status--erro");
        botao.disabled = false;
        botao.textContent = "ENTRAR";
    }
});
