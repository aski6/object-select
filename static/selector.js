var canvas = document.getElementById("selector-area");
var context = canvas.getContext("2d");

//create image variable, load and log the source.
selectorImage = new Image();
selectorImage.src=document.getElementById("img_src").innerHTML;
console.log("Source of image to select from:");
console.log(document.getElementById("img_src").innerHTML);

//set the canvas size to match that of the image we are selecting objects in
canvas.width = selectorImage.width;
canvas.height = selectorImage.height;
canvas.style.width = selectorImage.width;
canvas.style.height = selectorImage.height;

var width = selectorImage.width;
var height = selectorImage.height;
var mouseX;
var mouseY;
var newObject = true;
var objC1X;
var objC1Y;
var objC2X;
var objC2Y;

function Object() {

}

var objects = [];

//setup event listeners
document.onmousemove = mouseMoved;
function mouseMoved(e) {
  mouseX = e.pageX;
  mouseY = e.pageY;
}

canvas.onclick = canvasClicked;
function canvasClicked(e) {
  if(newObject) {

  }
}

//main loop functions
function update() {

}

function render() {
  //clear screen to draw new stuff on it.
  context.clearRect(0, 0, canvas.width, canvas.height);
  context.drawImage(selectorImage, 0, 0);
  //draw a vertical and horizontal ruler crossing at the mouse
  context.fillStyle="#ffff00";
  //fill a rect 3px by the height of the image for the vertical ruler
  context.fillRect(mouseX-1, 0, 2, height);
  context.fillRect(0, mouseY-1, width, 2);
}

function run() {
  update();
  render();
}

setInterval(run, 60);
