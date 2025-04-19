const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const spinButton = document.getElementById("spinButton");
const resultText = document.getElementById("result");

const prizes = [
    "A Magic Wand",
    "No Prize - Try Again",
    "A Flying Carpet",
    "Not This Time",
    "One dress - No mess",
    "No Prize",
    "A Magic Potion",
    "A Suitcase",
    "Extra Spin",
];

const colors = ["#fe2712", "#fc600a", "#fb9902"];

let angle = 0;
let spinning = false;

function drawOuterCircle() {
    ctx.beginPath();
    ctx.arc(220, 220, 210, 0, 2 * Math.PI);
    ctx.fillStyle = "white";
    ctx.fill();
    ctx.lineWidth = 4;
    ctx.strokeStyle = "gold";
    ctx.stroke();
    ctx.closePath();
}

function drawWheel() {
    drawOuterCircle();
    const sliceAngle = (2 * Math.PI) / prizes.length;
    for (let i = 0; i < prizes.length; i++) {
        ctx.beginPath();
        ctx.fillStyle = colors[i % colors.length];
        ctx.moveTo(220, 220);
        ctx.arc(220, 220, 200, i * sliceAngle, (i + 1) * sliceAngle);
        ctx.lineTo(220, 220);
        ctx.closePath();
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = "gold";
        ctx.stroke();

        ctx.save();
        ctx.translate(220, 220);
        ctx.rotate((i + 0.5) * sliceAngle);
        ctx.textAlign = "right";
        ctx.fillStyle = "#fff";
        ctx.font = "14px Arial";
        ctx.fillText(prizes[i], 180, 10);
        ctx.restore();
    }
}

function getPrizeIndex(finalAngle) {
    const degrees = finalAngle % 360;
    const sliceDegrees = 360 / prizes.length;
    return Math.floor((360 - degrees + sliceDegrees / 2) % 360 / sliceDegrees);
}

//const resultText = document.getElementById("result");

// This function will be called when the wheel stops spinning
function showPrize(prize) {
    const noPrizeOptions = ["No Prize", "No Prize - Try Again", "Not This Time", "Extra Spin"];

    // Check if the prize is one of the "no prize" types
    if (noPrizeOptions.includes(prize)) {
        resultText.innerHTML = `<p>You won: ${prize}</p>`;
    } else {

        // Replace with your actual product page or link structure
        const link = `/add_to_cart/${urlPrize}`;  // e.g., /product/a-magic-wand

        resultText.innerHTML = `<p>You won: <a href="${link}">${prize}</a></p>`;
    }
}


function spinWheel() {
    if (spinning) return;
    spinning = true;
    let spinAngle = Math.floor(3600 + Math.random() * 1000);
    //The number of seconds the wheel spins for 500 = 0.5 seconds
    let spinTime = 3000;
    let start = null;

    function animateWheel(timestamp) {
        if (!start) start = timestamp;
        let progress = timestamp - start;
        angle = (progress / spinTime) * spinAngle;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.translate(220, 220);
        ctx.rotate(angle * (Math.PI / 180));
        ctx.translate(-220, -220);
        drawWheel();
        ctx.restore();

        if (progress < spinTime) {
            requestAnimationFrame(animateWheel);
        } else {
            spinning = false;
            let winningIndex = getPrizeIndex(angle);
            prize = prizes[winningIndex];
            showPrize(prize)
        }
    }

    requestAnimationFrame(animateWheel);
}

drawWheel();
spinButton.addEventListener("click", spinWheel);
