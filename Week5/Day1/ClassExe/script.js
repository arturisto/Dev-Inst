function insert_Row(){

  var tr=document.createElement('tr');
  var td=document.createElement('td');
  for(var i = 1; i<=2 ;i++){
    var td=document.createElement('td');
    td.innerHTML="row3 cell "+ i;
    tr.appendChild(td);
    console.log(tr);
  }

  var elem= document.getElementById('sampleTable');
  elem.appendChild(tr);
}

let btn = document.getElementById("jsstyle");
let div = document.getElementById("exe3");
btn.addEventListener("click", clickClack);
btn.addEventListener("mouseover", hoverIng);
btn.addEventListener("mouseleave", hoverLeave);
div.addEventListener("click", clickClack2);
function clickClack(e){
    button = document.getElementById("jsstyle");
    button.style.fontSize="3em";
     e.stopPropagation();
}
function clickClack2(){
    let div = document.getElementById("exe3")
     div.style.backgroundColor="blue";


}
function hoverIng(){
    button = document.getElementById("jsstyle");
    button.style.color="red";
}
function hoverLeave(){
  button = document.getElementById("jsstyle");
  button.removeAttribute("style");
}
