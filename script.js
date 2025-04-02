// Game data
const locations = {
    home: {
        description: "Your apartment in Hong Kong",
        actions: ["Save Energy", "Reduce Waste", "Rest"]
    },
    work: {
        description: "Your office in Central",
        actions: ["Use Public Transport", "Reduce Paper", "Advocate Sustainability"]
    },
    market: {
        description: "Local wet market in Mong Kok",
        actions: ["Buy Local Produce", "Reduce Plastic", "Educate Vendors"]
    }
};

let player = {
    name: "",
    ecoPoints: 0,
    energy: 100,
    day: 1
};

// DOM elements
const welcomeScreen = document.getElementById("welcome-screen");
const gameScreen = document.getElementById("game-screen");
const playerNameInput = document.getElementById("player-name");
const startGameButton = document.getElementById("start-game");
const playerInfo = document.getElementById("player-info");
const gameStats = document.getElementById("game-stats");
const gameMessage = document.getElementById("game-message");
const actionsContainer = document.getElementById("actions");
const endDayButton = document.getElementById("end-day");

// Start game
startGameButton.addEventListener("click", () => {
    const playerName = playerNameInput.value.trim();
    if (playerName) {
        player.name = playerName;
        welcomeScreen.classList.add("hidden");
        gameScreen.classList.remove("hidden");
        updateGameHeader();
        showLocation("home");
    } else {
        alert("Please enter your name to start the game.");
    }
});

// Update game header
function updateGameHeader() {
    playerInfo.textContent = `Player: ${player.name}`;
    gameStats.textContent = `Day: ${player.day} | Eco Points: ${player.ecoPoints} | Energy: ${player.energy}`;
}

// Show location and actions
function showLocation(location) {
    const loc = locations[location];
    gameMessage.textContent = loc.description;
    actionsContainer.innerHTML = "";
    loc.actions.forEach(action => {
        const button = document.createElement("button");
        button.textContent = action;
        button.addEventListener("click", () => performAction(action));
        actionsContainer.appendChild(button);
    });
}

// Perform action
function performAction(action) {
    let ecoPoints = Math.floor(Math.random() * 10) + 1;
    let energyCost = Math.floor(Math.random() * 10) + 1;
    player.ecoPoints += ecoPoints;
    player.energy -= energyCost;
    gameMessage.textContent = `You performed: ${action}. Gained ${ecoPoints} Eco Points, lost ${energyCost} Energy.`;
    updateGameHeader();
    if (player.energy <= 0) {
        gameMessage.textContent += " You're out of energy! End the day to recover.";
        endDayButton.classList.remove("hidden");
    }
}

// End day
endDayButton.addEventListener("click", () => {
    player.day += 1;
    player.energy = 100;
    endDayButton.classList.add("hidden");
    updateGameHeader();
    gameMessage.textContent = "A new day begins! Choose your actions wisely.";
});