let container = document.querySelector('.container');
let btn = document.getElementById('spin');
let number = Math.ceil(Math.random() * 1000);

btn.onclick = function () {
    container.style.transform = "rotate(" + number + "deg)";
    number += Math.ceil(Math.random() * 1000);
    const button = document.getElementById('spin');
    function disableButton() {
        button.disabled = true;
        setTimeout(() => {
            button.disabled = false;
        }, 3000);
    }
    button.addEventListener('click', disableButton);
}


const divs = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight'];
let containe2 = document.querySelector('.container');
const wheel = document.getElementById('spin');
let rotateCount = 0;

wheel.addEventListener('click', () => {
    wheel.style.transition = 'transform 3s ease';
    rotateCount += 360 * 5;
    wheel.style.transform = `rotate(${rotateCount}deg)`;

    const index = Math.floor(rotateCount / 45) % 8;
    setTimeout(function () {
        alert(`You landed on: ${divs[index]}`);
    }, 3000);
});
