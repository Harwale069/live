let health = 100;
let supplies = 100;
let distance = 2000;
let day = 1;
let currentUser = "";
let currentSlot = 0;
let savedGames = {};

// ASCII Art to enhance visual appeal
const asciiArt = `
    ______________________________________
   / \\                                     \\.
  |   | Oregon Trail Adventure             |
   \\_ |____________________________________|   
      |                                   |
      | Journey Across the Untamed West!   |
      |___________________________________|
`;

// Initialize art panel
document.getElementById("ascii-art").innerText = asciiArt;

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
    }
    // Additional events can be added here
];

function login() {
    const username = document.getElementById("username").value;
    if (username) {
        currentUser = username;
        document.getElementById("user-name").innerText = username;
        document.getElementById("login-container").style.display = "none";
        document.getElementById("save-container").style.display = "block";
    }
}

function loadGame(slot) {
    currentSlot = slot;
    const userSave = savedGames[currentUser]?.[slot];
    if (userSave) {
        ({ health, supplies, distance, day } = userSave);
    }
    document.getElementById("save-container").style.display = "none";
    document.getElementById("game-container").style.display = "block";
    updateStatus();
}

function saveGame() {
    if (!savedGames[currentUser]) savedGames[currentUser] = {};
    savedGames[currentUser][currentSlot] = { health, supplies, distance, day };
    alert("Game saved!");
}

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
        saveGame();
        startEvent();
    }
}

function endGame(message) {
    document.getElementById("event-description").innerText = message;
    document.getElementById("choice-container").innerHTML = "";
}

updateStatus();
