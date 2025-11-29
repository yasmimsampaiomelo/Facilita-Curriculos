function enviarCurriculo(url, dados) {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dados),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erro na resposta do servidor: " + response.statusText);
      }
      return response.text();
    })
    .then((htmlContent) => {
      const newWindow = window.open("", "_blank");
      newWindow.document.write(htmlContent);
      newWindow.document.close();
      newWindow.focus();
    })
    .catch((error) => {
      console.error("Erro ao gerar currículo:", error);
      alert("⚠️ Ocorreu um erro ao gerar o currículo. Verifique o console.");
    });
}

function formatarLink(url) {
  if (url && !url.startsWith("http://") && !url.startsWith("https://")) {
    return "https://" + url;
  }
  return url;
}

// Currículo simples
function salvarDados() {
  const nome = document.getElementById("nome").value.trim();
  const email = document.getElementById("email").value.trim();
  const telefone = document.getElementById("telefone").value.trim();
  const resumo = document.getElementById("resumo").value.trim();
  const formacao = document.getElementById("formacao").value.trim();
  const experiencia = document.getElementById("experiencia").value.trim();
  const habilidades = document.getElementById("habilidades").value.trim();

  const idiomas = document.getElementById("idiomas")?.value.trim() || "";
  const linkedin = formatarLink(
    document.getElementById("linkedin")?.value.trim() || ""
  );
  const portfolio = formatarLink(
    document.getElementById("portfolio")?.value.trim() || ""
  );

  if (!nome || !email || !telefone) {
    alert("⚠️ Preencha os campos obrigatórios: nome, email e telefone.");
    return;
  }

  const dados = {
    nome,
    email,
    telefone,
    resumo,
    formacao,
    experiencia,
    habilidades,
    idiomas,
    linkedin,
    portfolio,
  };

  enviarCurriculo("/gerar_curriculo", dados);
}

// Currículo completo
function salvarDadosCompleto() {
  const nome = document.getElementById("nome").value.trim();
  const email = document.getElementById("email").value.trim();
  const telefone = document.getElementById("telefone").value.trim();
  const resumo = document.getElementById("resumo").value.trim();
  const formacao = document.getElementById("formacao").value.trim();
  const experiencia = document.getElementById("experiencia").value.trim();
  const habilidades = document.getElementById("habilidades").value.trim();
  const nome_completo = document.getElementById("nome_completo").value.trim();
  const data_nasc = document.getElementById("data_nasc").value.trim();
  const naturalidade = document.getElementById("naturalidade").value.trim();
  const disp = document.getElementById("disp").value.trim();

  const idiomas = document.getElementById("idiomas")?.value.trim() || "";
  const linkedin = formatarLink(
    document.getElementById("linkedin")?.value.trim() || ""
  );
  const portfolio = formatarLink(
    document.getElementById("portfolio")?.value.trim() || ""
  );

  const dados = [
    "nome",
    "email",
    "telefone",
    "nome_completo",
    "data_nasc",
    "naturalidade",
    "disp",
    "resumo",
    "formacao",
    "experiencia",
    "habilidades",
    "linkedin", // PRECISA estar aqui!
  ];

  enviarCurriculo("/gerar_curriculo_completo", dados);
}

// Currículo criativo
function salvarDadosCriativo() {
  const nome = document.getElementById("nome").value.trim();
  const email = document.getElementById("email").value.trim();
  const telefone = document.getElementById("telefone").value.trim();
  const resumo = document.getElementById("resumo").value.trim();
  const formacao = document.getElementById("formacao").value.trim();
  const experiencia = document.getElementById("experiencia").value.trim();
  const habilidades = document.getElementById("habilidades").value.trim();
  const perfil = document.getElementById("perfil").value.trim();

  const idiomas = document.getElementById("idiomas")?.value.trim() || "";
  const linkedin = formatarLink(
    document.getElementById("linkedin")?.value.trim() || ""
  );
  const portfolio = formatarLink(
    document.getElementById("portfolio")?.value.trim() || ""
  );

  if (!nome || !email || !telefone) {
    alert("⚠️ Preencha os campos obrigatórios: nome, email e telefone.");
    return;
  }

  const dados = {
    nome,
    email,
    telefone,
    resumo,
    formacao,
    experiencia,
    habilidades,
    perfil,
    idiomas,
    linkedin,
    portfolio,
  };

  enviarCurriculo("/gerar_curriculo_criativo", dados);
}
