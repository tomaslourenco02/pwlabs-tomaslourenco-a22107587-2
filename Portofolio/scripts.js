let header = document.querySelector("header");
let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
  header.classList.toggle("shadow", window.scrollY > 0);
});

menu.onclick = () => {
  navbar.classList.toggle("active");
};
window.onscroll = () => {
  navbar.classList.remove("active");
};

// Dark Mode / light mode
let darkmode = document.querySelector("#darkmode");

darkmode.onclick = () => {
  if (darkmode.classList.contains("bx-moon")) {
    darkmode.classList.replace("bx-moon", "bx-sun");
    document.body.classList.add("active");
  } else {
    darkmode.classList.replace("bx-sun", "bx-moon");
    document.body.classList.remove("active");
  }
};
function calcular() {
  // Obter a expressão aritmética inserida pelo usuário
  var expressao = document.getElementById("expressao").value;
  
  // Calcular o valor da expressão aritmética usando a função eval()
  var resultado = eval(expressao);
  
  // Exibir o resultado no elemento <p> abaixo do input
  document.getElementById("resultado").innerHTML = "Resultado: " + resultado;
}

function limparResultado() {
  // Limpar o conteúdo do elemento <p> que exibe o resultado
  document.getElementById("resultado").innerHTML = "";
}
function atualizarFrase() {
  // Obter a frase inserida pelo usuário
  var novaFrase = document.getElementById("input-frase").value;

  // Atualizar o texto sobreposto na imagem com a nova frase
  document.getElementById("frase").innerHTML = novaFrase;
}

document.getElementById("btn-confirmar").addEventListener("click", function() {
  var nome = document.getElementById("input-nome").value;

  document.getElementById("nome-header").innerHTML = "Olá, " + nome + "!";
  document.getElementById("nome-paragrafo-1").innerHTML = "Seu nome é " + nome + ".";
  document.getElementById("nome-paragrafo-2").innerHTML = "Obrigado por visitar, " + nome + "!";
});

var dataAtual = new Date();
		var opcoesData = { day: 'numeric', month: 'long', year: 'numeric' };
		var dataFormatada = dataAtual.toLocaleDateString('pt-BR', opcoesData);
		document.getElementById("data").innerHTML = dataFormatada;
                                    