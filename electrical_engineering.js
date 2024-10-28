const questions = [
    {
        question: "What is the total resistance (R_total) for R1 = 5 Ω and R2 = 3 Ω in series?",
        answer: 8,
        hint: "In series circuits, resistances add up."
    },
    {
        question: "What is the secondary voltage (V_s) for a primary voltage of 131 V and turns ratio of 1.57?",
        answer: 206.04,
        hint: "Use V_secondary = V_primary * turns ratio."
    }
];

let currentQuestionIndex = 0;
let score = 0;

document.getElementById('submit').addEventListener('click', checkAnswer);
document.getElementById('hint').addEventListener('click', showHint);
document.getElementById('calculator').addEventListener('click', openCalculator);

function displayQuestion() {
    document.getElementById('question').innerText = questions[currentQuestionIndex].question;
}

function checkAnswer() {
    const userAnswer = parseFloat(document.getElementById('answer').value);
    if (userAnswer === questions[currentQuestionIndex].answer) {
        score++;
        alert("Correct! Well done.");
    } else {
        alert(`Incorrect! The correct answer was ${questions[currentQuestionIndex].answer}.`);
    }
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        displayQuestion();
    } else {
        alert(`Game Over! Your final score is: ${score}`);
        location.reload(); // Reload the page to start over
    }
    document.getElementById('score').innerText = `Score: ${score}`;
    document.getElementById('answer').value = ''; // Clear input
}

function showHint() {
    alert(questions[currentQuestionIndex].hint);
}

function openCalculator() {
    const calc = prompt("Enter your calculation:");
    try {
        alert(`Result: ${eval(calc)}`);
    } catch {
        alert("Invalid calculation.");
    }
}

// Initialize the first question
displayQuestion();
