let img;

const grav = 0.15;
const bad_char_prob = 0.9;
const wep_size = 20;

var sword;
var chars = [];//on screen chars

var lives;
var score;


function preload(){
 img = loadImage('images/Background.jpg');
}

function setup(){
    createCanvas(800,600);

    sword = new weapon();
    frameRate(60);

    lives = 3;
    score = 0;
    output = "";
    lefoutput = "";
    rigoutput = "";
}

function draw(){
    background(151);
    image(img, 0, 0, 800, 600); 

    handleMouse();
    handleOBC();

    drawScore();
    drawLives();
    drawOutput();
}

function handleMouse(){
    if(mouseIsPressed){
        sword.swing(mouseX, mouseY);
    }

    if (frameCount % 2 == 0) { // update half the time
		sword.update();
	}

  sword.draw();
}

function handleOBC(){
    if(frameCount % 10 === 0){
        if(noise(frameCount) > 0.66){
            chars.push(randomOBC());   
        }
    }

    for (var i = chars.length - 1; i >= 0; i--) {

		chars[i].update();
		chars[i].draw();

		if (!chars[i].visible) { // if the character is no longer on-screen

			if (!chars[i].sliced && !chars[i].bad) { // if we haven't sliced & it's not a bad

				lives--;
			}

			if (lives < 1) { // if it's game over

				endGame();
			}

			chars.splice(i, 1); // delete from array
		} else {
			if(sword.checkForSlice(chars[i])){
                score += 1;
                output = chars[i].ranchar;
                lefoutput = chars[i].leftchar;
                rigoutput = chars[i].rightchar;
            }; // if we sliced add to the points
		}

	}
   
}

function drawLives() {

    stroke(0);
    strokeWeight(3);
    fill(255,0,0);
  
    for (var i = lives; i > 0; i--) {
  
          ellipse(width - (i * 30 + 150), 40, 20);
      }
  
  }

function drawScore() {

    textAlign(LEFT);
    noStroke();
    fill(0);
    textSize(50);
    text(score, 10, 50);
  }

function drawOutput() {
    fill(0);
    line(650, 600, 650, 0);
    textAlign(LEFT);
    noStroke();
    textSize(40);
    text('output', 665, 50);
    text(output, 665, 125); 
    text('Left', 665, 200);
    text(lefoutput, 665, 275);
    text('Right', 665, 400);
    text(rigoutput, 665, 475);
}

function endGame() {

    noLoop();
  
    textAlign(CENTER);
    noStroke();
    fill("#888888");
    textSize(100);
    text("Game over!", width / 2, height / 2);
    textSize(50);
    text("Press f5 to restart!", width / 2, height / 2 + 60);
}