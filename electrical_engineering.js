let score = 0;
let questionIdx = 0;

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

function displayQuestion() {
    if (questionIdx < questions.length) {
        document.getElementById("question").innerText = questions[questionIdx].question;
        document.getElementById("answer").value = "";
        document.getElementById("result").innerText = "";
    } else {
        document.getElementById("question-container").innerHTML = `<p>Game Over! Final Score: ${score}/${questions.length}</p>`;
    }
}

function checkAnswer() {
    const userAnswer = parseFloat(document.getElementById("answer").value);
    const correctAnswer = questions[questionIdx].answer;

    if (!isNaN(userAnswer) && Math.abs(userAnswer - correctAnswer) < 0.01) {
        score++;
        document.getElementById("result").innerText = "Correct! Well done!";
    } else {
        document.getElementById("result").innerText = `Incorrect. The correct answer was ${correctAnswer}.`;
    }
    questionIdx++;
    displayQuestion();
}

function showHint() {
    alert(questions[questionIdx].hint);
}

function openCalculator() {
    document.getElementById("calculator").style.display = "block";
}

function calculate() {
    const expression = document.getElementById("calc-input").value;
    try {
        const result = eval(expression);
        document.getElementById("calc-result").innerText = "Result: " + result;
    } catch (e) {
        document.getElementById("calc-result").innerText = "Invalid expression!";
    }
}

displayQuestion();
