
const container_valor = document.querySelector('.container_image_gif');

const image_valor = container_valor.querySelector('.image_valor');
const gif_valor = container_valor.querySelector('.gif_valor');

[...document.querySelectorAll('.image_valor')].forEach((image) => {
    image.addEventListener('mouseover', () => {
        const siblingGif = image.parentElement.querySelector('.gif_valor');
        image.style.display = 'none';
        siblingGif.style.display = 'block';
        siblingGif.style.position = 'relative';
    });
});

[...document.querySelectorAll('.gif_valor')].forEach((gif) => {
    gif.addEventListener('mouseout', () => {
        const siblingImage = gif.parentElement.querySelector('.image_valor');
        siblingImage.style.display = 'block';
        gif.style.display = 'none';
    });
});
