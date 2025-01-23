
let fontSize = 10;
const pic = document.getElementById('photo');

document.addEventListener('keydown', (event) => {
    if (event.code === 'Space') {
        event.preventDefault();
        
        fontSize += 1;

        if (fontSize > 48) {
            fontSize = 10;
        }
        pic.style.fontSize = fontSize + 'pt';
    }
});
                      