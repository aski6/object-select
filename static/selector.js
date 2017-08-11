var canvas = document.getElementById("selector-area");
var context = canvas.getContext("2d");

//create image variable, load and log the source.
selectorImage = new Image();
selectorImage.onload = function () {
  canvas.width = selectorImage.width;
  canvas.height = selectorImage.height;
  canvas.style.width = selectorImage.width;
  canvas.style.height = selectorImage.height;
}
selectorImage.src=document.getElementById("img_src").innerHTML;

console.log("Source of image to select from:");
console.log(document.getElementById("img_src").innerHTML);

//set the canvas size to match that of the image we are selecting objects in
/*
canvas.width = selectorImage.width;
canvas.height = selectorImage.height;
canvas.style.width = selectorImage.width;
canvas.style.height = selectorImage.height;
*/
var width = selectorImage.width;
var height = selectorImage.height;
var mouseX;
var mouseY;
var currentlySelecting = false;
var currentSelectionName = "default";
var objX1;
var objY1;
var objX2;
var objy2;

function Selection(name, x1, y1, x2, y2) {
  this.name = name
  this.x1 = x1;
  this.y1 = y1;
  this.x2 = x2;
  this.y2 = y2;
  this.toString = function(){
    return (name + "," + x1 + "," + y1 + "," + x2 + "," + y2);
  };
}

var selections = [];

//setup event listeners
function mouseMoved(e) {
  mouseX = e.pageX;
  mouseY = e.pageY;
}
document.onmousemove = mouseMoved;

canvas.onclick = canvasClicked;
function canvasClicked(e) {
  if(currentlySelecting) {
    objX2 = e.pageX;
    objY2 = e.pageY;
    addCurrentObject();
    currentlySelecting = false;
  } else {
    currentlySelecting = true;
    objX1 = e.pageX;
    objY1 = e.pageY;
  }
}

//data and setting handling functions.
//function to add a new object based on the current selection co-ordenates.
function addCurrentObject() {
  selections.push(new Selection(currentSelectionName, objX1, objY1, objX2, objY2));
  populateObjectSubmit();
}

function setSelectionName() {
  name = document.getElementById("selectionName").value;
  console.log("Name for new selections set to : " + name);
  currentSelectionName = name;
}

function populateObjectSubmit() {
  dataContainer = document.getElementById("selectionData");
  dataString = "";
  for (var i in selections) {
    dataString = dataString.concat(selections[i].toString() + "|");
  }
  dataContainer.value = dataString;
  console.log(dataString);
}

//main loop functions
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
  render();
}

setInterval(run, 60);
