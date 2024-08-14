let tituloH1 = document.getElementById('titulo');
let linkA = document.querySelector('a');
let listaNaoOrdenada = document.querySelector('ul');
let listaOrdenada = document.getElementById('lista-ordenada');

console.log(tituloH1);
console.log(linkA);
console.log(listaNaoOrdenada);
console.log(listaOrdenada);


tituloH1.innerText = `
CAPTURANDO ELEMENTOS E MANIPULANDO VIA JAVASCRIPT
`

linkA.innerText = `
Site Pro Educação
`

listaNaoOrdenada.innerHTML = `
<li>Itém 1 - Lista não Ordenada</li>
<li>Itém 2 - Lista não Ordenada</li>
<li>Itém 3 - Lista não Ordenada</li>
`
listaOrdenada.innerHTML = `
<li><a href ="https://google.com.br" target="blank">Google</a></li>
<li><a href="https://prozeducacao.com.br" target="blank">ProzEducação </a></li>
<li><a href ="https://github.com/adler-neto" target="blank">Github Adler-Neto</a></li>
`
