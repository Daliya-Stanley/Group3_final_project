const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const spinButton = document.getElementById("spinButton");
const resultText = document.getElementById("result");

const prizes = ["Magic Wand", "No Prize", "Flying Carpet", "Pack the World -Suitcase", "Try Again", "Magic Potion"];
const colors = ["#FF5733", "#33FF57", "#3357FF", "#FFFF33", "#FF33A8", "#33FFF5"];

let angle = 0;
let spinning = false;

// Draw Wheel
function drawWheel() {
    const sliceAngle = (2 * Math.PI) / prizes.length;
    for (let i = 0; i < prizes.length; i++) {
        ctx.beginPath();
        ctx.fillStyle = colors[i];
        ctx.moveTo(250, 250);
        ctx.arc(250, 250, 250, i * sliceAngle, (i + 1) * sliceAngle);
        ctx.fill();
        ctx.closePath();

        // Add Text
        ctx.fillStyle = "#fff";
        ctx.font = "20px Arial";
        ctx.fillText(prizes[i], 250 + Math.cos(sliceAngle * i) * 100, 250 + Math.sin(sliceAngle * i) * 100);
    }
}
drawWheel();

// Spin Function
spinButton.addEventListener("click", function () {
    if (spinning) return;

    spinning = true;
    let spinAngle = Math.floor(3600 + Math.random() * 1000);
    let spinTime = 3000;

    let start = null;
    function animateWheel(timestamp) {
        if (!start) start = timestamp;
        let progress = timestamp - start;

        angle = (progress / spinTime) * spinAngle;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.translate(250, 250);
        ctx.rotate(angle * (Math.PI / 180));
        ctx.translate(-250, -250);
        drawWheel();
        ctx.restore();

        if (progress < spinTime) {
            requestAnimationFrame(animateWheel);
        } else {
            spinning = false;
            let winningIndex = Math.floor((angle % 360) / (360 / prizes.length));
            resultText.textContent = "You won: " + prizes[winningIndex];

            // Send result to server
            fetch("/save_result", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ prize: prizes[winningIndex] }),
            });
        }
    }
    requestAnimationFrame(animateWheel);
});