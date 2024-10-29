let health, supplies, distance, day, currentUser, currentSlot;
const defaultGameState = { health: 100, supplies: 100, distance: 2000, day: 1 };
const asciiArt = `
    ______________________________________
   / \\                                     \\.
  |   | Oregon Trail Adventure             |
   \\_ |____________________________________|   
      | Journey Across the Untamed West!   |
      |___________________________________|
`;

document.getElementById("ascii-art").innerText = asciiArt;

function login() {
    const username = document.getElementById("username").value;
    if (username) {
        currentUser = username;
        document.getElementById("user-name").innerText = username;
        document.getElementById("login-container").style.display = "none";
        document.getElementById("save-container").style.display = "block";
    } else {
        alert("Please enter a valid username.");
    }
}
let creatingAccount = false;

function toggleCreateAccount() {
    creatingAccount = !creatingAccount;
    document.querySelector("button[onclick='login()']").style.display = creatingAccount ? "none" : "inline";
    document.querySelector("button[onclick='toggleCreateAccount()']").innerText = creatingAccount ? "Go to Login" : "Create Account";
}

function createAccount(username, password) {
    if (localStorage.getItem(username)) {
        alert("Username already exists. Choose another.");
        return;
    }
    localStorage.setItem(username, JSON.stringify({ password, slot1: null, slot2: null, slot3: null }));
    alert("Account created! You can now log in.");
}

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    const storedData = localStorage.getItem(username);
    if (storedData) {
        const { password: storedPassword } = JSON.parse(storedData);
        if (creatingAccount) createAccount(username, password);
        else if (storedPassword === password) {
            currentUser = username;
            document.getElementById("user-name").innerText = username;
            document.getElementById("login-container").style.display = "none";
            document.getElementById("save-container").style.display = "block";
        } else alert("Incorrect password.");
    } else alert("Account not found.");
}

function startNewGame(slot) {
    currentSlot = slot;
    loadGame();
    document.getElementById("save-container").style.display = "none";
    document.getElementById("game-container").style.display = "block";
    updateStatus();
}

function loadGame() {
    const savedData = localStorage.getItem(`${currentUser}_slot${currentSlot}`);
    if (savedData) {
        const gameState = JSON.parse(savedData);
        ({ health, supplies, distance, day } = gameState);
    } else {
        ({ health, supplies, distance, day } = defaultGameState);
    }
}

function saveGame() {
    const gameState = { health, supplies, distance, day };
    localStorage.setItem(`${currentUser}_slot${currentSlot}`, JSON.stringify(gameState));
    alert("Game saved!");
}

function logout() {
    currentUser = null;
    document.getElementById("game-container").style.display = "none";
    document.getElementById("save-container").style.display = "none";
    document.getElementById("login-container").style.display = "block";
}

function updateStatus() {
    document.getElementById("health-status").innerText = `Health: ${health}`;
    document.getElementById("supplies-status").innerText = `Supplies: ${supplies}`;
    document.getElementById("distance-status").innerText = `Distance to Oregon: ${distance} miles`;
    document.getElementById("day-status").innerText = `Day: ${day}`;
}

function startEvent() {
    const events = [
        { description: "You encounter a river crossing.", healthChange: -10, suppliesChange: -5, distanceChange: -15 },
        { description: "A storm damages your supplies.", healthChange: -5, suppliesChange: -10, distanceChange: -5 }
    ];
    
    const event = events[Math.floor(Math.random() * events.length)];
    document.getElementById("event-description").innerText = event.description;

    health += event.healthChange;
    supplies += event.suppliesChange;
    distance += event.distanceChange;
    day += 1;

    updateStatus();
    saveGame();

    if (distance <= 0) endGame("You made it to Oregon! Congratulations!");
    else if (health <= 0 || supplies <= 0) endGame("You didn't survive the journey.");
}

function endGame(message) {
    document.getElementById("event-description").innerText = message;
    document.getElementById("choice-container").innerHTML = "";
}

updateStatus();
