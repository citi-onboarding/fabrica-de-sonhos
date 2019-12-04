// CARROSSEL
$(document).ready(function(){
    $('#carrossel').slick({
        dots: false,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 3000,
    });
});

// CORAÇÃO
const galeria = document.querySelector('#galeria');
const box_coracao = galeria.querySelector('.coracao_box');
const coracao_sem_mensagem = galeria.querySelector('#coracao_branco');
const coracao_mensagem = galeria.querySelector('#coracao_mensagem');
const retangulo_mensagem = coracao_mensagem.querySelector('#Retângulo_201');
const mensagem = galeria.querySelector('.mensagem');

function removeCoracaoSemMensagem() {
    coracao_sem_mensagem.classList.add('remove_button');
}

function removeCoracaoComMensagem() {
    coracao_mensagem.classList.add('remove_button');
}

function addCoracaoSemMensagem() {
    coracao_sem_mensagem.classList.remove('remove_button');
}

function addCoracaoComMensagem() {
    coracao_mensagem.classList.remove('remove_button');
}

function addMensagem() {
    mensagem.classList.remove('remove_button');
}

function removeMensagem() {
    mensagem.classList.add('remove_button');
}

coracao_sem_mensagem.addEventListener('click', () => {
    removeCoracaoSemMensagem();
    addCoracaoComMensagem();
    addMensagem();
})

coracao_mensagem.addEventListener('click', () => {
    removeCoracaoComMensagem();
    addCoracaoSemMensagem();
    removeMensagem();
})

retangulo_mensagem.addEventListener('click', () => {
    removeCoracaoComMensagem();
    addCoracaoSemMensagem();
    removeMensagem();
})

mensagem.addEventListener('click', () => {
    removeCoracaoComMensagem();
    addCoracaoSemMensagem();
    removeMensagem();
})