let health = 100;
let supplies = 100;

const events = [
    { description: "You encounter a river. Cross carefully to avoid injury.", healthChange: -10, suppliesChange: 0 },
    { description: "A trader offers supplies in exchange for some of your gold.", healthChange: 0, suppliesChange: 10 },
    { description: "You got caught in a storm and lost some supplies.", healthChange: 0, suppliesChange: -20 }
];

document.getElementById('continue-btn').addEventListener('click', () => {
    const randomEvent = events[Math.floor(Math.random() * events.length)];
    updateStatus(randomEvent);
});

function updateStatus(event) {
    health += event.healthChange;
    supplies += event.suppliesChange;
    document.getElementById('event-description').innerText = event.description;
    document.getElementById('health-status').innerText = `Health: ${health}`;
    document.getElementById('supplies-status').innerText = `Supplies: ${supplies}`;

    if (health <= 0 || supplies <= 0) {
        alert("Game Over! You've reached the end of your journey.");
        location.reload();
    }
}
