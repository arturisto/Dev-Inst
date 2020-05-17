let div = document.getElementById("daily1");

div.addEventListener("mousedown", clickClack);
div.addEventListener("mouseover", hoverIng);
div.addEventListener("mouseleave", hoverLeave);
div.addEventListener("mousemove",mouseMove);

function clickClack(){
  let div = document.getElementById("daily1");
  div.style.borderColor="green";
}
function hoverIng(){
  let div = document.getElementById("daily1");
  div.innerHTML="hi there";
}

function hoverLeave(){
  let div = document.getElementById("daily1");
  div.innerHTML="";
}
function mouseMove(){
  let div = document.getElementById("daily1");
  div.innerHTML=Math.random()*100;
}
