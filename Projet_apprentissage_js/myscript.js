function toggleText(state) {
    const textElement = document.getElementById('text');
    textElement.innerText = `Qui est ${state}`;
}

function changeColor() {
    const textElement = document.getElementById('text');
    textElement.style.color = 'red';
}

function changeSize() {
    const textElement = document.getElementById('text');
    textElement.style.fontSize = '30px';
}
function randomColor() {
    const textElement = document.getElementById('text');
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    textElement.style.color = randomColor;
}


function turnOn() {
    const imageElement = document.getElementById('image');
    imageElement.src = 'allume.png'; // Chemin vers l'image "allumée"
}

function turnOff() {
    const imageElement = document.getElementById('image');
    imageElement.src = 'eteint.png'; // Chemin vers l'image "éteinte"
}








function operation1() {
    const result = 7 * 8; // Calcule 7 x 8
    displayResult(result);
}

function operation2() {
    const a = 12;
    const b = 14;
    const c = a + b; // Additionne a et b
    displayResult(c);
}

function operation3() {
     // Initialise d à 0 et incrémente de 1 à chaque clic
    if (typeof operation3.counter === 'undefined') {
        operation3.counter = 0; // Définit une variable persistante
    }
    operation3.counter += 1;
    displayResult(operation3.counter);
}

function operation4() {
    const d = operation3.counter || 0; // Utilise le compteur d'opération 3 ou 0 si non défini
    const cosValue = Math.cos(d); // Calcule le cosinus
    displayResult(cosValue);
}

// Fonction utilitaire pour afficher les résultats
function displayResult(value) {
    const resultElement = document.getElementById('result');
    resultElement.innerText = `Résultat : ${value}`;
}





function showDate() {
    const currentDate = new Date();
    const formattedDate = `Le ${currentDate.getDate()}/${currentDate.getMonth() + 1}/${currentDate.getFullYear()}`;
    document.getElementById('date-display').innerText = formattedDate;
}

// Affiche un message selon l'heure actuelle
function greetBasedOnTime() {
    const currentHour = new Date().getHours();
    let message = '';

    if (currentHour >= 6 && currentHour < 12) {
        message = 'Bonjour';
    } else if (currentHour >= 12 && currentHour < 18) {
        message = 'Bon après-midi';
    } else if (currentHour >= 18 && currentHour < 21) {
        message = 'Bonne soirée';
    } else {
        message = 'Bonne nuit';
    }

    document.getElementById('greeting').innerText = message;
}

// Affiche le jour de la semaine
function showDay() {
    const currentDate = new Date();
    const daysOfWeek = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'];
    const dayName = daysOfWeek[currentDate.getDay()];

    document.getElementById('day-display').innerText = `Aujourd'hui, c'est ${dayName}`;
}