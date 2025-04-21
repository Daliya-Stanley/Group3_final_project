const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const spinButton = document.getElementById("spinButton");
const resultText = document.getElementById("result");

const prizes = promotional_products.map(p => ({
    id:    p.productid,
    // remove the trailing " - Free" just for the label
    label: p.productname.replace(/\s*-\s*Free$/, "")
  }));

console.log("prizes now: ", prizes )

const noPrizeLabels = [
    "No Prize - Try Again",
    "Not This Time",
    "Extra Spin"
  ];

console.log("prizes now: ", prizes )

noPrizeLabels.forEach(lbl => prizes.push({ id: null, label: lbl }));

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
        ctx.font = "13px Arial";
        ctx.fillText(prizes[i].label, 180, 10);
        ctx.restore();
    }
}

function getPrizeIndex(finalAngle) {
    const degrees = finalAngle % 360;
    const sliceDegrees = 360 / prizes.length;
    return Math.floor((360 - degrees + sliceDegrees / 2) % 360 / sliceDegrees);
}


// This function will be called when the wheel stops spinning
function showPrize(prize) {
    const noPrizeOptions = ["No Prize", "No Prize - Try Again", "Not This Time", "Extra Spin"];

    // Check if the prize is one of the "no prize" types
    if (noPrizeOptions.includes(prize.label)) {
        resultText.innerHTML = `<p>Sorry: ${prize.label}</p>`;
    } else {

        // Get productid of the prize won
        productid = prize.id

        // Replace with your actual product page or link structure
        const link = `/add_product_to_cart/${productid}`;  // e.g., /product/a-magic-wand

        resultText.innerHTML = `<p>You won: <a href="${link}"class="gold-link">${prize.label}</a></p>
        <p><em>Click the prize to add it to your cart!</em></p>`;
    }
}


function spinWheel() {
    if (spinning) return;
    spinning = true;
    let spinAngle = Math.floor(3600 + Math.random() * 1000);
    //The number of seconds the wheel spins for 500 = 0.5 seconds
    let spinTime = 2500;
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
