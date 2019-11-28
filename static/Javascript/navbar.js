const header_navBar = document.querySelector('#header_navbar');
const button_menu_hamburguer = header_navBar.querySelector('.box_menu_hamburguer');
const button_icon_exit = header_navBar.querySelector('.box_botao_sair');
const action_div = header_navBar.querySelector('.action_menu_hamburguer');

function menuHamburguerRemove() {
    button_menu_hamburguer.classList.add('remove_button');
}

function menuHamburguerAdd() {
    button_menu_hamburguer.classList.remove('remove_button');
}

function iconExitRemove() {
    button_icon_exit.classList.add('remove_button');
}

function iconExitAdd() {
    button_icon_exit.classList.remove('remove_button');
}

function changeMenuScreenRemove() {
    action_div.classList.add('remove_button');
}

function changeMenuScreenAdd() {
    action_div.classList.remove('remove_button');
}

button_menu_hamburguer.addEventListener('click', () => {
    menuHamburguerRemove();
    iconExitAdd();
    changeMenuScreenAdd();
})

button_icon_exit.addEventListener('click', () => {
    iconExitRemove();
    menuHamburguerAdd();
    changeMenuScreenRemove();
})