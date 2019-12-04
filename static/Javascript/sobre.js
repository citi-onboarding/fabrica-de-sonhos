
const container_valor = document.querySelector('.container_image_gif');

const image_valor = container_valor.querySelector('.image_valor');
const gif_valor = container_valor.querySelector('.gif_valor');


document.querySelector('.container_image_gif').addEventListener('mouseover', (e) => {
    console.log(e.target.children)
    
    image_valor.style.display = 'none';
    gif_valor.style.display = 'block';
    gif_valor.style.position = 'relative'
    
});

document.querySelector('.gif_valor').addEventListener('mouseout', () => {
    image_valor.style.display = 'block';
    gif_valor.style.display = 'none';
});

