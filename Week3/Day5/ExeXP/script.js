//exe1

let x = 45;
let y = 190;
if (x+y <=100){
  console.log(true);
}
else{
  console.log(false);
}

//exe2
console.log( y - x*(Math.floor(y/x)));

//exe3
if (y%x ===0){console.log(true)}
else{console.log(false)}

//exe4
let arr=[1,44,223,42,122,22,5,12];

x = parseInt(prompt("Please enter a number between 1 and a 300"));

let bool = arr.includes(x);
if( bool==true){alert("true")}
else{alert("false")}
