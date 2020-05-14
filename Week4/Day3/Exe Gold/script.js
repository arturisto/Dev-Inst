//exe1
let elem = document.getElementsByTagName('div')[0];
elem.setAttribute("style","background-color:lightblue;padding:5px;");

let l = document.getElementsByTagName('ul')[0].children;
l[0].setAttribute("style","display:none;");
l[1].setAttribute("style", "border:1px solid black")

document.body.setAttribute("style","font-size:3em;");

// if (document.getElementsByTagName('div')[0].style.backgroundColor == 'lightblue'){
//   alert("hello x and y");
// }

let table = document.body.firstElementChild;
l = table.children[0];
for (let i = 0; i<5;i++ ){
    l.children[i].children[i].setAttribute("style","background-color:blue;")
}
