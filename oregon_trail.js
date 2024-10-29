let health = 100;
let supplies = 100;
let distance = 2000;
let day = 1;

const events = [
    {
        description: "You encounter a river crossing.",
        choices: [
            { text: "Attempt to ford the river", healthChange: -10, suppliesChange: 0, distanceChange: -10 },
            { text: "Look for another path", healthChange: 0, suppliesChange: -5, distanceChange: -5 }
        ]
    },
    {
        description: "A storm damages your supplies.",
        choices: [
            { text: "Take shelter", healthChange: -5, suppliesChange: -10, distanceChange: 0 },
            { text: "Move forward despite the storm", healthChange: -10, suppliesChange: -5, distanceChange: -10 }
        ]
    },
    {
        description: "A friendly traveler offers supplies for trade.",
        choices: [
            { text: "Trade health for supplies", healthChange: -10, suppliesChange: +15, distanceChange: 0 },
            { text: "Refuse trade", healthChange: 0, suppliesChange: 0, distanceChange: 0 }
        ]
    }
    // Add more events as desired
];

function updateStatus() {
    document.getElementById("health-status").innerText = `Health: ${health}`;
    document.getElementById("supplies-status").innerText = `Supplies: ${supplies}`;
    document.getElementById("distance-status").innerText = `Distance to Oregon: ${distance} miles`;
    document.getElementById("day-status").innerText = `Day: ${day}`;
}

function startEvent() {
    const randomEvent = events[Math.floor(Math.random() * events.length)];
    document.getElementById("event-description").innerText = randomEvent.description;
    const choiceContainer = document.getElementById("choice-container");
    choiceContainer.innerHTML = "";

    randomEvent.choices.forEach((choice) => {
        const choiceBtn = document.createElement("button");
        choiceBtn.innerText = choice.text;
        choiceBtn.addEventListener("click", () => makeChoice(choice));
        choiceContainer.appendChild(choiceBtn);
    });
}

function makeChoice(choice) {
    health += choice.healthChange;
    supplies += choice.suppliesChange;
    distance -= choice.distanceChange;
    day += 1;

    updateStatus();
    if (distance <= 0) {
        endGame("Congratulations! You've reached Oregon!");
    } else if (health <= 0 || supplies <= 0) {
        endGame("Game Over. You've succumbed to the journey.");
    } else {
        startEvent();
    }
}

function endGame(message) {
    document.getElementById("event-description").innerText = message;
    document.getElementById("choice-container").innerHTML = "";
}

// Initialize the game
document.getElementById("continue-btn").addEventListener("click", () => {
    startEvent();
    document.getElementById("continue-btn").style.display = "none";
});

updateStatus();
