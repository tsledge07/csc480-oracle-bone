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

OBC.prototype.update = function() {

  this.position.add(this.velocity);

  this.velocity.x *= 0.99; // air resistance
  this.velocity.y += grav; // gravity

	this.visible = (this.position.y < height); // update visibility

	if (this.sliced) {

		this.slicedTime++; // update sliced time
	}
};


OBC.prototype.draw = function() {

    /* if a bad char is chosen change color to red */
    if(this.bad){
        fill(255,0,0);
    }
    else{
        fill(0);
    }
    if(this.sliced){
      if(this.bad){
        endGame();
      }
      this.visible = false
    }

  noStroke();
  textAlign(LEFT);
  textSize(45);
  text(this.ranchar, this.position.x, this.position.y);

};


function randomOBC() {
 var tempranchar = ["邬","郗","郇","魏","魄","骸","髁","骰","髂","髌"];
 var templefchar = ["乌","希","旬","委","白","骨","骨","骨","骨","骨"];
 var temprigchar = ["阝"," 阝"," 阝","鬼","鬼","亥","果","殳","客","宾"];
 var badchar = "乙";
	/* randomize position */
  var x = random(600);
  var y = height;

  if(random() > bad_char_prob){
    var bad = true;
    var ranchar = badchar;
    var leftchar = "N/A";
    var rightchar = "N/A";
  }else{
    var bad = false;
    var ranval = floor(random(0,10)); 
    var ranchar = tempranchar[ranval];
    var leftchar = templefchar[ranval];
    var rightchar = temprigchar[ranval];
  }

  return new OBC(x, y, bad , ranchar, leftchar, rightchar); 
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