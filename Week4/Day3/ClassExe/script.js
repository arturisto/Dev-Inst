// //exe1
//
// let div = document.body.firstElementChild;
//
// console.log(div);
// div = document.body.children[0];
//
// console.log(div);
//
// let ul = document.body.children[1];
// console.log(ul);
//
// ul = document.body.firstElementChild.nextElementSibling;
// console.log(ul);
//
// let li = document.body.children[1].children[1];
// console.log(li);

//exe2
// div = document.getElementById('container');
//
// div = document.getElementsByTagName("div")[0];
//
// console.log("part 2");
//  ul = document.getElementsByTagName("ul");
//
// //ul = document.querySelectorAll(".list");
// for (x of ul){
//   for (y of x.children){
//      console.log(y);
//   }
// }
// console.log("part 3");
//
// for (x of ul){
//   console.log(x.children[0]);
// }


//exe3

let href = document.getElementById("dI");
console.log(href.getAttribute("href"));
console.log(href.getAttribute("hreflang"));
console.log(href.getAttribute("rel"));
console.log(href.getAttribute("target"));
console.log(href.getAttribute("type"));

let p = document.getElementById("text");
p.setAttribute("style", "font-size: 3em;")
