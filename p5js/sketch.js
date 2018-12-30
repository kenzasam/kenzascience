var dna ;
var jdna ;
var clr ;
var f ;
var i=0;
var clrA='#91DFAA' ;
var clrC='#5FACA3';
var clrT='#1E796F';
var clrG='#E35B96';
var base;
var canvas

function preload(){
  dna = loadStrings('dna.txt', fileready);
}

function setup() {
  // put setup code here
 canvas = createCanvas(windowWidth, windowHeight);
 canvas.position(0,0);
 canvas.style('z-index', '-1')
 smooth();
 //ackground(255);
 f = textFont('Ariel',26,true); // courrier, 16 point, anti-aliasing on;

}

function keyPressed() {
  clear();
}

function fileready(dna){
  //"https://github.com/kenzasam/kenzascience/blob/gh-pages/dna.txt");
  jdna = join(dna,'');
  console.log(jdna);
  console.log(jdna.length);
}


function draw() {
  // put drawing code here
  base = jdna.charAt(i);
  noFill();
  if (base =='G'){
    clr = clrG;}
  else if (base=='C'){
   clr = clrC;}
  else if (base=='A'){
      clr = clrA ;}
  else {
      clr = clrT;}
  fill(clr);
  text(base,mouseX,mouseY);
}

function mouseMoved(){

 if (i == jdna.length){
    i=0;
  }
  i = i+1;
 }

function keyPressed(){
    if (keyCode==DELETE){
    background(255);
    i=0;}
    else if (keyCode==ENTER){
    exit()
    }
  }
