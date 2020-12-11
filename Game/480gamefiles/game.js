let img;

const grav = 0.15;// gravity to be applied to the characters
const bad_char_prob = 0.9;// probibility that the character is bad, will be used in a comparison and if a random floating point between 0 and 1 is greater than 0.9, it will be a bad char.
const wep_size = 20;//size of weapon 

var sword;
var chars = [];//on screen chars

var lives;
var score;


function preload(){//allows for the background image to be properly displayed
 img = loadImage('images/Background.jpg');
}

function setup(){
    createCanvas(800,600);//size of the game window

    sword = new weapon();//creation of a weapon object to use
    frameRate(60);//framerate of the game

    //variables to be output to the screen
    lives = 3;
    score = 0;
    output = "";
    lefoutput = "";
    rigoutput = "";
}

/*
Function to continuously draw the game area and call other functions
that are used to run the game
*/
function draw(){
    background(151);
    image(img, 0, 0, 800, 600); 

    handleMouse();
    handleOBC();

    drawScore();
    drawLives();
    drawOutput();
}

//function to control the mouse
function handleMouse(){
    if(mouseIsPressed){
        sword.swing(mouseX, mouseY);//calls swing method when the mouse is pressed either left or right button
    }

    if (frameCount % 2 == 0) { // updates the weapon half the time
		sword.update();
	}

  sword.draw();//draws the dots to visualize the mouse button being pressed
}

//function to handle the chinese scripts, called obc since Oracle Bone characters might be used
function handleOBC(){
    //timing for  pushing new characters to the screen
    if(frameCount % 10 === 0){
        if(noise(frameCount) > 0.66){
            chars.push(randomOBC());   
        }
    }
    //loop that updates and draws the characters that are in the play area
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
// draws lives at top right of game area
function drawLives() {

    stroke(0);
    strokeWeight(3);
    fill(255,0,0);
  
    for (var i = lives; i > 0; i--) {
  
          ellipse(width - (i * 30 + 150), 40, 20);
      }
  
  }
// draws score at top left of the game area
function drawScore() {

    textAlign(LEFT);
    noStroke();
    fill(0);
    textSize(50);
    text(score, 10, 50);
  }

// draws the output of the charater and its parts to the right of the game area  
function drawOutput() {
    fill(0);
    line(650, 600, 650, 0);
    textAlign(LEFT);
    noStroke();
    textSize(40);
    text('output', 665, 50);
    text(output, 665, 125); //character that was most recently sliced
    text('Left', 665, 200);
    text(lefoutput, 665, 275);// left part of the character that was sliced
    text('Right', 665, 400);
    text(rigoutput, 665, 475);// right part of the character that was sliced
}
//function to end the game if all lives are lost
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