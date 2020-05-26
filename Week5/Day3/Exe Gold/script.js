// exe1

function over(e){

    e.preventDefault();
  let elem = document.getElementById(e.target.id);
  elem.style.backgroundColor="cyan";
}
function drop(e){

  e.preventDefault();
  let elem = document.getElementById(e.target.id);
  elem.style.backgroundColor="black";
}


//exe2
elem = document.createElement("div");
elem.classList.add("letter");
elem.innerHTML =" drop area";
elem.id="dropArea";
document.getElementById("alphabet").appendChild(elem)
const l =[...'abcdefghijklmnopqrstuvwxyz']
console.log(l);
let bucket=document.getElementById("dropArea");
let coordBucket = bucket.getBoundingClientRect();
for(x of l){

  elem = document.createElement("div");
  elem.classList.add("letter");
  elem.innerHTML = x;
  elem.id=x;
  elem.draggable="true";
  console.log("hit");
  elem.addEventListener("ondragstart",function(e){
      e.preventDefault();
      console.log("hi");
      bucket.style.backgroundColor="cyan";

  });
  elem.addEventListener("ondragend", function(e){

      e.preventDefault();
      console.log("hello");
      coordTarget = document.getElementById(e.target.id).getBoundingClientRect();
      if(coordBucket["top"] <= coordTarget["top"] && coordBucket["left"] <= coordTarget["left"] && coordBucket["bottom"] >= coordTarget["bottom"] && coordBucket["right"] >= coordTarget["right"]){
            bucket.style.background="green";
          }
      });

    document.getElementById("alphabet").appendChild(elem)
  }
