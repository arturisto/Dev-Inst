//exe1

// 1. Give to all paragraphs inside the article tag the class para_article
// 2. Remove the last paragraph in the article.
// 3. Add an event listener so that when you click on the h2, it is removed from the DOM.
// 4. Set the font size of the h1 to be a random pixel size from 0 to 100.
// 5. Hide the 1st paragraph, when it’s clicked
// 6. Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked
// 7. Get the value in the inputs and append it to the end of the html, inside a table


// 1
let pS = document.getElementsByTagName("p");
for (x of pS){
  x.setAttribute("class","para_article");
}

// 2
let article = document.getElementsByTagName("article")[0];
article.removeChild(article.lastChild);

//3

let h2 = document.getElementsByTagName("h2")[0];

h2.addEventListener('click', removeH2);

function removeH2(){
  let h2 = document.getElementsByTagName("h2")[0];
  h2.parentNode.removeChild(h2);
}
//4
let h1 = document.getElementsByTagName("h1")[0];
h1.style.fontSize = Math.random()*100+"px";
h1.addEventListener("click", hideH1);
function hideH1(){
  let h1 = document.getElementsByTagName("h1")[0];
  h1.style.display="none";
}

pS[1].addEventListener("click",fadeOut);

function fadeOut(){

  let p = document.getElementsByTagName("p")[1];
  console.log(p);
  p.style.opacity="0";
  p.style.transition="opacity 2s ease-in-out ";
}
function storeData(){

  let input = document.getElementsByTagName("input");
  let bool = false;
  for( x of input){
    if (x.value){
      bool=true;
    }
    else{
      bool=false;
    }
  }

  if(bool){

    let table = document.createElement("table");
    let row = table.insertRow(0);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    cell1.innerHTML = input[0].value;
    cell2.innerHTML = input[1].value;

    document.body.appendChild(table);
  }
}


//exe2

// Create a function called : getBold_items() that takes no parameter. This function has to collect all the bold items inside the paragraph.
// Create a function called : highlight() that change the color of each bold item to blue. Create a function called : return_normal() that change the color of each bold item to black
// Call function highlight() onMouseOver and the function return_normal() onMouseOut
function getBold_items(){
  let strong = document.getElementById("exe2").getElementsByTagName("strong");
  return strong
}

function highlight(){
  let s=getBold_items();
  for (let x of s){
    x.style.color="blue";
  }
}

function return_normal(){
  let s=getBold_items();
  for (let x of s){
    x.removeAttribute("style");
  }
}
let exe2=document.getElementById("exe2");
exe2.addEventListener("mouseover",highlight);
exe2.addEventListener("mouseleave",return_normal);


//exe3
let radius = document.getElementById('MyForm');
radius.addEventListener("submit",caclRadius);

function caclRadius(e){
  let radius = parseFloat(document.getElementById('radius').value);
  let volume = document.getElementById('volume');
  volume.value = 4*Math.pow(radius,3)*Math.PI / 3;
  e.preventDefault();
}
