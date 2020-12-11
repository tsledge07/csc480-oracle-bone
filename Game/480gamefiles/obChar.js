function OBC(x, y, bad, ranchar, leftchar, rightchar){

  this.position = createVector(x, y);

  this.bad = bad; 
  this.ranchar = ranchar;
  this.leftchar = leftchar;
  this.rightchar = rightchar;

	this.velocity = createVector(randomXVelocity(x), random(-7, -11));

  this.sliced = false;
	  this.slicedTime = 0; 

  this.visible = true;
}
//function to update characters on screen
OBC.prototype.update = function() {

  this.position.add(this.velocity);

  this.velocity.x *= 0.99; // air resistance
  this.velocity.y += grav; // gravity

	this.visible = (this.position.y < height); // update visibility

	if (this.sliced) {

		this.slicedTime++; // update sliced time
	}
};

//function to draw the characters
OBC.prototype.draw = function() {

    /* if a bad char is chosen change color to red */
    if(this.bad){
        fill(255,0,0);
    }
    else{// if a good character is randomly selected change color to black
        fill(0);
    }
    if(this.sliced){// if the character has been sliced
      if(this.bad){//if the character is bad and sliced end game
        endGame();
      }
      //if sliced and not bad set the visibility of the character to false
      this.visible = false
    }

  noStroke();
  textAlign(LEFT);
  textSize(45);
  text(this.ranchar, this.position.x, this.position.y);

};

//randomazation of character
function randomOBC() {
 var tempranchar = ["邬","郗","郇","魏","魄","骸","髁","骰","髂","髌"];//temp selection of characters to be replaced with database access
 var templefchar = ["乌","希","旬","委","白","骨","骨","骨","骨","骨"];//temp selection of left parts of characters
 var temprigchar = ["阝"," 阝"," 阝","鬼","鬼","亥","果","殳","客","宾"];//temp selection of right parts of characters
 var badchar = "乙";// a bad non sliceable character.
	/* randomize position */
  var x = random(600);
  var y = height;

  if(random() > bad_char_prob){
    //setting variable parts if character is bad
    var bad = true;
    var ranchar = badchar;
    var leftchar = "N/A";
    var rightchar = "N/A";
  }else{
    //setting variable parts if character is not bad
    var bad = false;
    var ranval = floor(random(0,9));//gives a random integer value from 0-9 to access 1 of the slots in the temp array  
    var ranchar = tempranchar[ranval];
    var leftchar = templefchar[ranval];
    var rightchar = temprigchar[ranval];
  }

  return new OBC(x, y, bad , ranchar, leftchar, rightchar);// returns the character with its parts 
}

/**
 * returns velocity to always point toward center
 */
function randomXVelocity(x) {

  if (x > width / 2) {

    return random(-1.5, -0.5);
  } else {

    return random(0.5, 1.5);
  }
}