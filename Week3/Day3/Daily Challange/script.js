//Conditionals

let bad ="bad";
let not = "not";

let string1 = "The good, the bad and the ugly";
let string2 = "The dev institute  course is not bad";

if (string1.indexOf(not) < string1.indexOf(bad) && string1.indexOf(not)>-1 && string1.indexOf(bad)>-1 ){

  var string3 = string1.slice(0,string1.indexOf(not))+ "good" + string1.slice(string1.indexOf(bad)+bad.length);
  console.log(string3);
}
else {
  console.log(string1);
}

if (string2.indexOf(not) < string2.indexOf(bad) && string2.indexOf(not)>-1 && string2.indexOf(bad)>-1 ){
   string3 = string2.slice(0,string2.indexOf(not))+ "good" + string2.slice(string2.indexOf(bad)+bad.length);
  console.log(string3);
}
else {
  console.log(string2);
}
console.log("loops");
//loops
arr = [5,0,9,1,7,4,2,6,3,8];
let swap = 0;
for (let i =0; i<=arr.length; i++){
  for (let j =1; j<=arr.length-1; j++){
    if ( arr[j-1] < arr[j]){
        swap = arr[j-1];
        arr[j-1]=arr[j];
        arr[j]=swap;
      }
    }
}
let string = arr.toString();
console.log(string);

string = arr.join("/");
console.log(string);
string = arr.join("");
console.log(string);
string = arr.join("-");
console.log(string);
