// Game constants
const START_MONEY = 100;
const DISTANCE_GOAL = 1000;
const START_HEALTH = 100;
const START_FOOD = 50;
const START_WATER = 40;
const START_STAMINA = 100;
const START_MORALE = 75;
const FOOD_PER_TRAVEL = 10;
const WATER_PER_TRAVEL = 5;
const STAMINA_PER_TRAVEL = 10;
const MORALE_LOSS_TRAVEL = 5;

let health = START_HEALTH;
let food = START_FOOD;
let water = START_WATER;
let stamina = START_STAMINA;
let morale = START_MORALE;
let money = START_MONEY;
let milesTraveled = 0;
let daysPassed = 0;

// DOM Elements
const gameDisplay = document.getElementById('game');
const travelBtn = document.getElementById('travelBtn');
const statsBtn = document.getElementById('statsBtn');
const startGameBtn = document.getElementById('startGame');

// Start the game and show the intro
startGameBtn.addEventListener('click', startGame);
travelBtn.addEventListener('click', travel);
statsBtn.addEventListener('click', displayStats);

function startGame() {
    gameDisplay.innerHTML = "<p>Welcome to the Oregon Trail Deluxe Edition! Survive your journey to Oregon by managing your resources.</p>";
    startGameBtn.style.display = 'none';
    travelBtn.style.display = 'inline-block';
    statsBtn.style.display = 'inline-block';
    displayStats();
}

function travel() {
    if (food <= 0 || water <= 0 || stamina <= 0) {
        gameDisplay.innerHTML += "<p>You can't travel. You need food, water, or rest!</p>";
        return;
    }

    const distance = Math.floor(Math.random() * 51) + 50;
    milesTraveled += distance;
    food -= FOOD_PER_TRAVEL;
    water -= WATER_PER_TRAVEL;
    stamina -= STAMINA_PER_TRAVEL;
    morale -= MORALE_LOSS_TRAVEL;

    daysPassed++;
    gameDisplay.innerHTML += `<p>Traveled ${distance} miles. Days passed: ${daysPassed}</p>`;
    
    if (milesTraveled >= DISTANCE_GOAL) {
        gameDisplay.innerHTML += "<p>Congratulations! You've reached Oregon!</p>";
        travelBtn.style.display = 'none';
        statsBtn.style.display = 'none';
    } else {
        displayStats();
    }
}

function displayStats() {
    gameDisplay.innerHTML += `<p>Health: ${health}, Food: ${food}, Water: ${water}, Stamina: ${stamina}, Morale: ${morale}, Money: $${money}, Miles Traveled: ${milesTraveled}, Days Passed: ${daysPassed}</p>`;
}
