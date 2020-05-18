//exe1

var cart =[]
let elem =document.createElement("input");
elem.setAttribute("type","text");
elem.setAttribute("name","cartInput");
elem.setAttribute("id", "input");

let root = document.getElementById("root");
root.appendChild(elem);
elem = document.createElement("br");
root.appendChild(elem);
elem = document.createElement("button");
elem.setAttribute("type","button");
elem.setAttribute("id", "add");
elem.innerHTML="add";
elem.setAttribute("onclick", "addItemToCart()");

root.appendChild(elem);
elem = document.createElement("br");
root.appendChild(elem);

elem = document.createElement("button");
elem.setAttribute("type","button");
elem.setAttribute("id", "clear");
elem.innerHTML="Clear Cart";
elem.setAttribute("onclick", "clearCart()");

root.appendChild(elem);
elem = document.createElement("br");
root.appendChild(elem);

elem = document.createElement("button");
elem.setAttribute("type","button");
elem.setAttribute("id", "items");
elem.innerHTML="Number of Items";
elem.setAttribute("onclick", "cartSize()");

root.appendChild(elem);
elem = document.createElement("br");
root.appendChild(elem);

function addItemToCart(){
    cart.push(document.getElementById("input").value);
    document.getElementById("input").value = "";
}

function clearCart(){
    cart=[];
}

function cartSize(){
  alert(cart.length);
}


//exe2
let select = document.getElementById('genres');

alert(select.value);
let option = document.createElement("option");
option.text = "Classic";
option.value="classic";

select.add(option);
select.options[2].selected=true;

//exe3


let input = document.getElementsByTagName("input")[1];

input.addEventListener("click",removeItem);

function removeItem(){

  let colors = document.getElementById("colorSelect");
  colors.remove(colors.selectedIndex);
}
