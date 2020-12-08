function weapon() {

    this.swipes = []; // fading blade movement
  
    this.color = color(0);
  }
  
  /**
   * fades blade movement
   */
  weapon.prototype.update = function() {
  
    /* fade swipe */
    if (this.swipes.length > wep_size) { // delete two every other frame
  
      this.swipes.splice(0, 1);
      this.swipes.splice(0, 1);
    } else if (this.swipes.length > 0) {
  
      this.swipes.splice(0, 1); // delete last value
    }
  };
  
  /**
   * tests whether the passed fruit is sliced by the sword's swipe
   */
  weapon.prototype.checkForSlice = function(chars) {
  
    if (chars.sliced || this.swipes.length < 2)
      return false;
  
    var length = this.swipes.length; // length of sword
  
      var stroke1 = this.swipes[length - 1]; 
      var stroke2 = this.swipes[length - 2]; 
  
      /* calculate distance from strokes 1 & 2 from char */
    var d1 = dist(stroke1.x, stroke1.y, chars.position.x, chars.position.y);
    var d2 = dist(stroke2.x, stroke2.y, chars.position.x, chars.position.y);
  
    var sliced = d1 < 30 && d2 < 30;//size of char is 45 so this makes it so you are close enought to have sliced			
  
    chars.sliced = sliced; 
  
    return sliced;
  };
  
  /**
   * draws the blade
   */
  weapon.prototype.draw = function() {
  
    var length = this.swipes.length;
  
    for (var i = 0; i < length; i++) {
  
      var s = map(i, 0, length, 2, 20); // shrink dots
  
      noStroke();
      fill(this.color);
      ellipse(this.swipes[i].x, this.swipes[i].y, s);
    }
  
  };
  
  /**
   * swings the sword
   */
  weapon.prototype.swing = function(x, y) {
  
    this.swipes.push(createVector(x, y));
  };