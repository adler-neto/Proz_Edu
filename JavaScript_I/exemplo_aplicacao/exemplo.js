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
elementoJavaScriptDiv1.innerHTML = `
    <h2 class="post-titulo">Vendas à Produtos</h2>
    <p class="post-texto">
        Estes são os produtos que temos à venda no momento!
    </p>
    <h3>Violão Taylor</h2>
    <p><strong>517E WHB BE VIOLÃO TAYLOR ELETROACÚSTICO AÇO
    </strong></p>
    <p><strong>R$16.000,00
    </strong></p>
    <p><strong>DESCRIÇÃO</strong></p>
        <p>
      Apresentando o formato de corpo Grand Pacific Dreadnought, com uma
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
      e um belíssimo Hard Case Deluxe Hardshell-Western Floral Taylor.
    </p>
    <p><strong>ITENS INCLUSOS</strong></p>
    <p>
      1 Violão Taylor 517e WHB BUILDER´S EDITION 1 Hard Case Deluxe
      Hardshell-Western Floral Taylor
    </p>
    <p><strong>FICHA TÉCNICA GERAL</strong></p>
    <p>
      Modelo – 517e WHB BUILDER´S EDITION Shape – Grand Pacific Dreadnought
      Comprimento da escala – 25-1/2"" (64,77 cm) Largura da escala – 1-3/4""
      (4,44 cm) Número de trastes - 20 Cordas - Phosphor Bronze (.012"-.053")
      (Aço) Bag – 1 Hard Case Deluxe Hardshell-Western Floral Taylor Captação –
      Eletroacústica Madeira Tampo – Sitka Spruce Madeira Corpo – Mógno Tropical
      Madeira Braço – Mógno Tropical
    </p>
    <p><strong>CORPO</strong></p>
    <p>
      Binding – Sapele Configuração Traseira – 2 peças sem cunha Tipo de Roseta
      – Anel único Acabamento traseiro/lateral - Silent Satin Junção Madeira
      Fundo - Nenhum Stain/Sunburst – Tampo: Wild Honey Burst, Fundo, Lados e
      Braço: Blackwood Stain Descanso de Braço - Não Acabamento Tampo – Silent
      Satin Incrustação de Ponte - Nenhum Binding no Descanço de Braço – Não
      Fechamento em cunha – Nenhum
    </p>
    <p><strong>BRAÇO</strong></p>
    <p>
      Largura do braço – 1-3/4” Existência de Borda do braço do violão - Ébano
      Tipo de junção do braço – Scarf Madeira do braço do violão – Ébano
      Comprimento do tróculo – 3-1/2” Incrustação do braço do violão – Marfim
      Tampa do Tróculo - Ébano Madeira Braço/Tróculo – Mógno Tropical Acabamento
      do braço – Satin
    </p>
    <p><strong>HEADSTOCK</strong></p>
    <p>
      Tipo de Headstock – Padrão Acabamento do Headstock – Satin Overlay do
      Headstock - Ébano Logotipo Headstock – Marfim Binding Headstock - Nenhum
      Incrustação Headstock – Marfim
    </p>


`;

// Adiciona a div à section
elementoJavaScriptSection.appendChild(elementoJavaScriptDiv1);

// Adiciona a section ao body
elementoBody.appendChild(elementoJavaScriptSection);