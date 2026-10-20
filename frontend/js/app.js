(() => {
    const API_BASE_URL = window.APP_API_BASE_URL || "https://app-motoboyv2-1.onrender.com";

    const tokenSalvo = () =>
        localStorage.getItem("access_token") ||
        localStorage.getItem("token") ||
        sessionStorage.getItem("access_token") ||
        sessionStorage.getItem("token");

    const mensagemErro = (erro) => {
        if (erro instanceof TypeError) {
            return "Não foi possível conectar à API. Confira sua conexão.";
        }
        return erro.message || "Não foi possível concluir a operação.";
    };

    async function requisicao(caminho, opcoes = {}) {
        const token = tokenSalvo();
        if (!token) {
            throw new Error("Você precisa entrar na sua conta primeiro.");
        }

        const resposta = await fetch(API_BASE_URL + caminho, {
            ...opcoes,
            headers: {
                Authorization: "Bearer " + token,
                Accept: "application/json",
                ...(opcoes.body ? { "Content-Type": "application/json" } : {}),
                ...opcoes.headers
            }
        });

        const dados = await resposta.json().catch(() => ({}));
        if (!resposta.ok) {
            throw new Error(
                resposta.status === 401
                    ? "Sua sessão expirou. Entre novamente."
                    : typeof dados.detail === "string"
                        ? dados.detail
                        : "Não foi possível concluir a operação."
            );
        }
        return dados;
    }

    window.MotoboyApi = {
        requisicao,
        mensagemErro,
        moeda: (valor) => new Intl.NumberFormat("pt-BR", {
            style: "currency",
            currency: "BRL"
        }).format(Number(valor) || 0),
        numero: (valor) => new Intl.NumberFormat("pt-BR", {
            maximumFractionDigits: 1
        }).format(Number(valor) || 0)
    };
})();
