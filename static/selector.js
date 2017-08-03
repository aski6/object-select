var canvas = document.getElementById("selector-area");
var context = canvas.getContext("2d");

selectorImage = new Image();
selectorImage.src=document.getElementById("img_src").innerHTML;

console.log("Source of image to select from:");
console.log(document.getElementById("img_src").innerHTML);

canvas.width = selectorImage.width;
canvas.height = selectorImage.height;
canvas.style.width = selectorImage.width;
canvas.style.height = selectorImage.height;

function update() {
}

function render() {
  //clear screen to draw new stuff on it.
  context.clearRect(0, 0, canvas.width, canvas.height);

  context.drawImage(selectorImage, 0, 0);
}

function run() {
  update();
  render();
}

setInterval(run, 60);
