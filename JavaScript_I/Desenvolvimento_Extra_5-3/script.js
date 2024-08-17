// Criação do elemento h1
let elementoJavaScriptH1 = document.createElement("h1");
elementoJavaScriptH1.innerText = "Vendas de Produtos";
elementoJavaScriptH1.id = "titulo-site";

// Adiciona o h1 ao body
let elementoBody = document.querySelector("body");
elementoBody.appendChild(elementoJavaScriptH1);

// Criação da section
const elementoJavaScriptSection = document.createElement("section");
elementoJavaScriptSection.className = "postagens";

// Criação da div dentro da section
const elementoJavaScriptDiv1 = document.createElement("div");
elementoJavaScriptDiv1.id = "produtos"; 

// Criação dos elementos de texto
const nomeProduto = 'VIOLÃO 517E WHB BE TAYLOR ELETROACÚSTICO AÇO';
const descricaoProduto = `Apresentando o formato de corpo Grand Pacific Dreadnought, com uma
      experiência de conforto exclusiva de madeiras de primeira linha, o
      Builder's Edition 517e Western Honey Burst apresenta aos músicos Taylor um
      novo tipo de som além dos padrões Taylor. O fundo e os lados de mogno
      sólido geram uma resposta de médios quentes e fortes com projeção e calor
      envelhecido do tampo de Sitka Spruce torrado, resultando em um som
      complexo e temperado com clara potência nos graves. Nosso reforço Classe V
      melhora a experiência com mais volume e sustain mais longo, além de
      proporcionar maior harmonia entre as notas. Este modelo Builder's Edition
      também possui bordas chanfradas e um pescoço esculpido composto para uma
      sensação mais fluída, e o acabamento Silent Satin reduz o ruído de
      reprodução incidental para aplicações de gravação. Vem com um captador ES2
      e um belíssimo Hard Case Deluxe Hardshell-Western Floral Taylor.`;
const precoProduto = `R$16.000,00`;

const nomeElemento = document.createElement('p');
nomeElemento.textContent = `Nome: ${nomeProduto}`;

const descricaoElemento = document.createElement('p');
descricaoElemento.textContent = `Descrição: ${descricaoProduto}`;

const precoElemento = document.createElement('p');
precoElemento.textContent = `Preço: ${precoProduto}`;

// Adiciona os elementos de texto à div do produto
elementoJavaScriptDiv1.appendChild(nomeElemento); //Insere o nome do produto
elementoJavaScriptDiv1.appendChild(descricaoElemento); //Insere o descrição do produto
elementoJavaScriptDiv1.appendChild(precoElemento); //Insere o preço do produto

// Adiciona uma imagem do produto
const imagemProduto = document.createElement('img');
imagemProduto.src = "./img/violao.jpg"; // Substitua pelo URL da imagem real
imagemProduto.alt = 'Imagem do Produto';
imagemProduto.style.display = 'block'; // Centraliza a imagem
imagemProduto.style.margin = '0 auto'; // Centraliza a imagem
elementoJavaScriptDiv1.insertBefore(imagemProduto, nomeElemento); // Insere a imagem antes do nome do produto

// Adiciona a div à section
elementoJavaScriptSection.appendChild(elementoJavaScriptDiv1);

// Adiciona a section ao body
elementoBody.appendChild(elementoJavaScriptSection);