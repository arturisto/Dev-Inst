 function myMove(){
   let x=0;
   let id = setInterval(function() {
     let anim = document.getElementById("animate");
      x=x+5;
      anim.style.left = x+"px";
        if(x>=350){
          clearInterval(id);
        }
   } , 20);
}

function start(event){

  let elem = document.getElementById(event.target.id);
  elem.style.backgroundColor="lightblue";
  // event.style.backgroundColor="blue";
}
function over(event){
  event.preventDefault();
  let elem = document.getElementById(event.target.id);
  elem.style.backgroundColor="green";
}

function drop(event){

  event.preventDefault();
  console.log("here");
  let elem = document.getElementById(event.target.id);
  elem.style.backgroundColor="grey";
}
