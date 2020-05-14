// exe1

let elem = document.getElementById('navBar');
elem.setAttribute("id", "socialNetworkNavigation");

let li = document.createElement('li');
let a = document.createElement('a');
a.href="#";
let textNode = document.createTextNode("logout");
a.appendChild(textNode);
li.appendChild(a);
elem.firstElementChild.appendChild(li);

let text1 = elem.firstElementChild.firstElementChild.firstElementChild.childNodes[0].nodeValue;
let text2 = elem.firstElementChild.lastElementChild.firstElementChild.childNodes[0].nodeValue;

console.log(text1);
console.log(text2);


//exe2
console.log("exe2")
elem = document.getElementsByClassName("list")[1];

elem.firstElementChild.innerHTML="Richard";
for (let x of document.getElementsByClassName("list")){
    x.firstElementChild.innerHTML="arthur";
    elem = document.createElement("p");
    elem.innerHTML = "Hey Students";
    x.after(elem);

}
elem = document.getElementsByClassName('list')[1].childNodes[3];

let l = document.getElementsByClassName("list");
while(l.length>0){
  l[0].className="student";
}
