let word = prompt("Player 1 please choose 1 word").split("");
let guess_word =("*".repeat(word.length)).split("");
let used_letters=[];

let lives = 10;
console.log("let the game begin");
console.log("lives left: "+lives);
console.log(guess_word.join(""));


while(lives>0){
  var letter = prompt("Choose a letter");

  if(used_letters.includes(letter)){
    console.log("this letter was used");
    console.log("your used letters are: "+ used_letters.join(","));
    console.log(guess_word.join(""));
  }
  else if( word.includes(letter)){
            for(var i=0; i<word.length;i++){
                if(word[i]==letter){
                  guess_word[i] = letter;
                }
            }

            console.log("that was a correct letter, good job");
            console.log("your number of lives is: "+lives);
            used_letters.push(letter);
            console.log("your used letters are: "+ used_letters.join(","));
            console.log(guess_word.join(""));
            if(guess_word.join("") === word.join("")){
              break;
            }

        }
      else{
            console.log("Wrong letter");
            lives -=1;
            console.log("you lost a life, now it is:" + lives);
            used_letters.push(letter);
            console.log("your used letters are: "+ used_letters.join(","));
            console.log(guess_word.join(""));

          }
}
if(lives>0){
    console.log("you have won!");
}
else{
  console.log("sorry, but you are out of lives");
  console.log("the word was: "+ word.join(""));
}
