const wordContainer = document.getElementById('wordContainer');
const startButton = document.getElementById('startButton');
const userLetters = document.getElementById('userLetters');
const canvas = document.getElementById('canvas');
const h1 = document.querySelector('h1');

let ctx = canvas.getContext('2d');

const streakDisplay = document.createElement('div');
streakDisplay.id = "streak_counter";
if (h1) document.body.insertBefore(streakDisplay, h1.nextSibling);

const CANVAS_SIZE = {width: 120, height: 160, scale: 20};
// Hangman drawing
const bodyParts = [
    [4, 2, 1, 1],
    [4, 3, 1, 2],
    [3, 5, 1, 1],
    [5, 5, 1 ,1],
    [3, 3, 1, 1],
    [5, 3, 1, 1]
];

let chosenWord;
let userWords;
let mistakes;
let hits;
let streak = parseInt(localStorage.getItem('hangmanStreak') || 0);

const updateStreakDisplay = () =>{
    streakDisplay.textContent = `Streak: ${streak}`;
}

const selectWordDifficulty = () =>{
    let filteredWords;
    if (streak < 3){
        filteredWords = wordBank.filter(w => w.length <= 5);
    } else if(streak < 6){
        filteredWords = wordBank.filter(w => w.length > 5 && w.length < 8);
    }else{
        filteredWords = wordBank.filter(w => w.length > 8);
    }

    const finalBank = filteredWords.length > 0 ? filteredWords: wordBank;
    return finalBank[Math.floor(Math.random() * finalBank.length)].toUpperCase();
}


const drawHangman = () => {
    canvas.width = CANVAS_SIZE.width;
    canvas.height = CANVAS_SIZE.height;
    ctx.scale(CANVAS_SIZE.scale, CANVAS_SIZE.scale)
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = '#d95d39'
    ctx.fillRect(0, 7, 4, 1) // Base
    ctx.fillRect(1, 0, 1, 8) // Post
    ctx.fillRect(2, 0, 3, 1) // Roof
    ctx.fillRect(4, 1, 1, 1) // Rope
};

const startGame = () => {
    userWords = [];
    mistakes = 0;
    hits = 0;
    wordContainer.innerHTML = '';
    userLetters.innerHTML = '';
    startButton.style.display = "none";

    updateStreakDisplay()
    chosenWord = selectWordDifficulty()

    drawHangman();
    drawWordStatus();

    document.addEventListener('keydown', wordEvent);
};

const drawWordStatus = () =>{
    const fragment = document.createDocumentFragment();
    chosenWord.split('').forEach(char => {
        const span = document.createElement('span');
        span.textContent = char;
        span.classList.add('letter', 'hidden')
        fragment.appendChild(span);
    });
    wordContainer.appendChild(fragment)
};


const wordEvent = event =>{
    const letter = event.key.toUpperCase();
    if(letter.match(/^[A-ZÑ]$/i)&& !userWords.includes(letter)){
        userWords.push(letter);

        if (chosenWord.includes(letter)){
            const children = wordContainer.children;
            for(let child of children){
                if(child.textContent === letter){
                    child.classList.remove('hidden')
                    hits++
                }
            }
        } else{
            ctx.fillStyle = '#FFF';
            ctx.fillRect(...bodyParts[mistakes]);
            mistakes++;
        }
        const usedLetterElement = document.createElement('span');
        usedLetterElement.textContent = letter + " ";
        userLetters.appendChild(usedLetterElement);

        checkGameStatus()
    }
};

const checkGameStatus = () =>{
    if (hits === chosenWord.length){
        streak++;
        localStorage.setItem('hangmanStreak', streak);

        Array.from(wordContainer.children).forEach((el, i) =>{
            setTimeout(() => el.classList.add('win_animation'), i * 50);
        });

        endGame("Level Up!");
    }else if(mistakes === bodyParts.length){
        streak = 0;
        localStorage.setItem('hangmanStreak', streak);
        // Revelas word at lose
        Array.from(wordContainer.children).forEach(el => el.classList.remove('hidden'))
        endGame(`Game Over! Word was: ${chosenWord}`);
    }
    updateStreakDisplay()
};

const endGame = (message) =>{
    document.removeEventListener('keydown', wordEvent);
    setTimeout(() =>{
        alert(message);
        startButton.style.display = 'block';
        startButton.textContent = streak > 0 ? "Continue Streak": "Try Again";
    }, 500);
};

updateStreakDisplay()
startButton.addEventListener('click', startGame);



