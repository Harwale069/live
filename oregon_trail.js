let health = 100;
let supplies = 100;
let distance = 2000;
const events = [
    {
        description: "You encounter a raging river. You can try to cross it or find another way.",
        choices: [
            { text: "Cross the river", healthChange: -15, suppliesChange: 0, distanceChange: -10 },
            { text: "Find another way", healthChange: 0, suppliesChange: -10, distanceChange: -5 }
        ]
    },
    {
        description: "You meet a trader who offers you supplies in exchange for gold.",
        choices: [
            { text: "Trade supplies for gold", healthChange: 0, suppliesChange: 20, distanceChange: 0 },
            { text: "Refuse to trade", healthChange: 0, suppliesChange: 0, distanceChange: 0 }
        ]
    },
    {
        description: "A storm hits, and some supplies are damaged.",
        choices: [
            { text: "Protect supplies", healthChange: -10, suppliesChange: -10, distanceChange: -5 },
            { text: "Wait out the storm", healthChange: 0, suppliesChange: -15, distanceChange: 0 }
        ]
    },
    // Add more complex events and choices here
];

document.getElementById('continue-btn').addEventListener('click', () => {
    startEvent();
});

function startEvent() {
    const randomEvent = events[Math.floor(Math.random() * events.length)];
    document.getElementById('event-description').innerText = randomEvent.description;
    const choiceContainer = document.getElementById('choice-container');
    choiceContainer.innerHTML = "";

    randomEvent.choices.forEach((choice, index) => {
        const choiceBtn = document.createElement('button');
        choiceBtn.innerText = choice.text;
        choiceBtn.addEventListener('click', () => makeChoice(choice, randomEvent));
        choiceContainer.appendChild(choiceBtn);
    });
}

function makeChoice(choice, event) {
    health += choice.healthChange;
    supplies += choice.suppliesChange;
    distance -= choice.distanceChange;

    document.getElementById('health-status').innerText = `Health: ${health}`;
    document.getElementById('supplies-status').innerText = `Supplies: ${supplies}`;
    document.getElementById('distance-status').innerText = `Distance to Oregon: ${distance} miles`;

    checkGameOver();
    if (distance > 0) {
        startEvent();
    } else {
        endGame("Congratulations! You've reached Oregon!");
    }
}

function checkGameOver() {
    if (health <= 0) {
        endGame("You've succumbed to the harsh conditions. Game Over.");
    } else if (supplies <= 0) {
        endGame("You ran out of supplies and couldn't continue. Game Over.");
    }
}

function endGame(message) {
    alert(message);
    location.reload();
}
