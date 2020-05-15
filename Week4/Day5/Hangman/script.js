let word = [];
let guessed_letters=0;
let lives = 10;
word = prompt(" please choose sentance(up to 20 charecters)").split("");
while(word.length>20 ){
  word = prompt(" please choose sentance(up to 20 charecters)").split("");
}
guessed_letters = (word.join("")).split(" ").join("").length;
console.log(guessed_letters);

createWord(word);

function my_f(letter){
    if(word.includes(letter)==false){
      document.querySelectorAll("."+letter)[0].disabled=true;
      loselife(document.querySelectorAll("#l-"+lives)[0]);
      // document.querySelectorAll("#l-"+lives)[0].style.color="black";
        lives-=1;
      if(lives ==0 ){
        setTimeout(alertFunc("you lost :( \r\n the word was: "+word.join("") +"\r\n refresh window to start new game" ),3);
      }
        }
      else{
        for (var elem of document.querySelectorAll(".h-"+letter)){
                  elem.innerHTML=letter;
                  guessed_letters-=1;
        }
        document.querySelectorAll("."+letter)[0].disabled=true;

        if(guessed_letters==0){
          setTimeout(alertFunc("you have won!!! \r\n refresh window for new game"), 1)
        }
      }
}
function alertFunc(msg){
  alert(msg);
}

function loselife(elem){

  for (let i = 4;i>=0;i--)
  {
    elem.setAttribute("style","transform:translateY(100px);transition: all 1s ease-in-out;");
    elem.style.opacity=i/4

  }
}

function createWord(arr){

  for (x of arr){

      var elem=document.createElement('span');
      if (x ==" "){
          elem.innerHTML=" ";
      }
      else{
        elem.innerHTML="_";
      }
        elem.setAttribute("style","margin:auto;");
        elem.setAttribute("class","h-"+x);
        if(arr.length <10){ elem.style.fontSize="3em";}
        else if(arr.length <20){ elem.style.fontSize="2em";}
        document.querySelectorAll(".guess")[0].appendChild(elem);
  }
}
