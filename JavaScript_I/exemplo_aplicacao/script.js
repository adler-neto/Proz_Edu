//cria um elemento li
let elementoJavaScript = document.createElement("li");
//adiciona um texto (JavaScript) para o novo elemento li
elementoJavaScript.innerText = "JavaScript"
//adiciona uma id para o novo elemento li
elementoJavaScript.id = "ling-js"
//seleciona onde será inserido o novo elemento li
let listaLinguagens = document.querySelector(".lista-linguagens");
//adiciona um o elemento JavaScript a lista
listaLinguagens.appendChild(elementoJavaScript);

//cria um novo elemento (div) na postagem 
const postagemJavaScript = document.createElement("div");
postagemJavaScript.innerHTML =`
<h2 class="post-titulo">JavaScript</h2>
<p class="post-texto">
  JavaScript é uma linguagem de programação
</p>`
//adiciona um script em html para a nov apostagem
const postagens = document.querySelector(".postagens");
postagens.appendChild(postagemJavaScript);