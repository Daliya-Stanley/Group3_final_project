function playGame(playerChoice) {
    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `choice=${playerChoice}`,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `You chose: ${playerChoice}, Computer chose: ${data.computer_choice}. ${data.result}`;
        updateHistory(data.history);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred.';
    });
}

function updateHistory(history) {
    const historyList = document.getElementById('history');
    historyList.innerHTML = ''; // Clear previous history
    history.forEach(game => {
        const listItem = document.createElement('li');
        listItem.textContent = `You chose: ${game.player}, Computer chose: ${game.computer}, Result: ${game.outcome} (${game.time})`;
        historyList.appendChild(listItem);
    });
}