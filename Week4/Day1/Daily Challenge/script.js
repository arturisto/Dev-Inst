let l  = prompt("please enter a short sentance").split(" ");
let max = 0;
let str = "";
//get max length
for(x of l){
  if (x.length > max){ max = x.length}
}
for(let i =0; i<max+2; i++){
    str=str.concat("*");
}
console.log(str);
for (x of l){
  print(x);
}
str=""
for(let i =0; i<max+2; i++)
{
    str=str.concat("*");
}
console.log(str);

function print(string){
  str = "*";
  str = str.concat(string)
  for (i=0; i<(max-string.length);i++){
  str=str.concat(" ");
  }
    str=str.concat("*");
  console.log(str);
}
