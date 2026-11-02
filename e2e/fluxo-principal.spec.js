const { test, expect } = require("@playwright/test");

test("percorre cadastro, moto, trabalho, gastos, dashboard e relatório", async ({ page }) => {
  const errosConsole = [];
  const falhasApi = [];
  page.on("pageerror", (erro) => errosConsole.push(erro.message));
  page.on("response", async (resposta) => {
    if (!resposta.ok() && resposta.url().includes("/Motoboy/create")) {
      falhasApi.push(`${resposta.status()} ${await resposta.text()}`);
    }
  });

  const identificador = `${Date.now()}-${Math.random().toString(16).slice(2, 8)}`;
  const email = `e2e-${identificador}@gmail.com`;
  const senha = "TesteE2E!2026";
  const hoje = new Date();
  const data = [hoje.getFullYear(), String(hoje.getMonth() + 1).padStart(2, "0"), String(hoje.getDate()).padStart(2, "0")].join("-");
  const dataInicio = new Date(hoje.getFullYear(), hoje.getMonth(), 1);
  const inicio = [dataInicio.getFullYear(), String(dataInicio.getMonth() + 1).padStart(2, "0"), "01"].join("-");

  await page.goto("/cadastro.html");
  await page.locator("#nome").fill("Usuário E2E");
  await page.locator("#email").fill(email);
  await page.locator("#idade").fill("30");
  await page.locator("#senha").fill(senha);
  await page.locator("#confirmacao-senha").fill(senha);
  await page.locator("#form-cadastro button[type=submit]").click();
  await expect(page.locator("#mensagem-cadastro")).toContainText("sucesso", {
    timeout: 15_000,
  }).catch(async () => {
    throw new Error(`Cadastro falhou. Resposta da API: ${falhasApi.join(" | ") || "sem resposta HTTP; verifique se a API local está acessível ao navegador"}`);
  });
  await expect(page).toHaveURL(/login\.html/, { timeout: 15_000 });

  await page.locator("#email").fill(email);
  await page.locator("#senha").fill(senha);
  await page.locator("#form-login button[type=submit]").click();
  await expect(page).toHaveURL(/index\.html/, { timeout: 15_000 });

  await page.goto("/criar-moto.html");
  await page.locator("#marca").fill("Honda");
  await page.locator("#modelo").fill(`CG E2E ${identificador}`);
  await page.locator("#ano").fill(String(hoje.getFullYear()));
  await page.locator("#quilometragem").fill("10000");
  await page.locator("#consumo").fill("35");
  await page.locator("#form-moto button[type=submit]").click();
  await expect(page).toHaveURL(/minha-moto\.html/, { timeout: 15_000 });
  await expect(page.locator("#moto-titulo")).toContainText(`CG E2E ${identificador}`);

  await page.goto("/registrar.html");
  await page.locator("#data").fill(data);
  await page.locator("#ganhos").fill("300");
  await page.locator("#km-inicial").fill("10000");
  await page.locator("#km-final").fill("10100");
  await page.locator("#form-registro button[type=submit]").click();
  await expect(page.locator("#mensagem-registro")).toContainText("registrado com sucesso");

  await page.goto("/gastos.html");
  await page.locator("#tipo").selectOption("abastecimento");
  await page.locator("#valor").fill("50");
  await page.locator("#data").fill(data);
  await page.locator("#quilometragem").fill("10050");
  await page.locator("#posto").fill("Posto teste E2E");
  await page.locator("#litros").fill("5");
  await page.locator("#form-gasto button[type=submit]").click();
  await expect(page.locator("#mensagem-gasto")).toContainText("registrado com sucesso");

  await page.locator("#tipo").selectOption("manutencao");
  await page.locator("#valor").fill("20");
  await page.locator("#data").fill(data);
  await page.locator("#quilometragem").fill("10060");
  await page.locator("#descricao").fill("Revisão E2E");
  await page.locator("#form-gasto button[type=submit]").click();
  await expect(page.locator("#mensagem-gasto")).toContainText("registrado com sucesso");

  await page.goto("/index.html");
  await expect(page.locator("#ganhos")).toHaveText("R$ 300,00");
  await expect(page.locator("#km-rodados")).toContainText("100");
  await expect(page.locator("#gastos")).toContainText("/km");
  await expect(page.locator("#lista-gastos-recentes")).toContainText("Abastecimento");
  await expect(page.locator("#lista-gastos-recentes")).toContainText("Manutenção");

  await page.goto("/relatorio.html");
  await page.locator("#data-inicio").fill(inicio);
  await page.locator("#data-fim").fill(data);
  await page.locator("#form-relatorio button[type=submit]").click();
  await expect(page.locator("#mensagem-relatorio")).toContainText("atualizado com sucesso");
  await expect(page.locator("#total-ganhos")).toHaveText("R$ 300,00");
  await expect(page.locator("#total-gastos")).toHaveText("R$ 70,00");
  await expect(page.locator("#km-rodados")).toContainText("100");

  expect(errosConsole, `Erros JS no navegador: ${errosConsole.join(" | ")}`).toEqual([]);
});
