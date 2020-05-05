// exe conditions
let newDog = 'Chihuahua';
let len = newDog.length;
console.log('The length of the dog is: '+len);

console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog == 'Chihuahua'){
  console.log('I LOVE Chihuahua, it’s my favorite dog');
}
else {
  console.log('I dont care, I prefer CATS');
}


// exe Loops 1
let colors=['blue','purple', 'pink fuchsia']
let suffix ='';
let num=1
for (let i=1;i<=3;i++){
    if (i==1) {suffix='st'}
    else if(i==2){suffix='nd'}
    else {suffix='rd'}

    console.log("My "+i+suffix+" choice is "+colors[i-1]);
}

//exe loops 2
num = 0
num = parseInt(prompt("please enter a number between 1 and a gazillion"));
while(true){

  if(num <= 10){
    num = parseInt(prompt("please enter a new number between 1 and a gazillion"));
    }
  else {break;}
}
alert("Thank you for playing'gues what I wanted'");

//exe Loop3
let people = ["Greg", "Mary", "Devon", "James"];

for (i of people){
  console.log(i)
}
let index = people.indexOf("Greg");
people.splice(index,1);
index = people.indexOf("James");
people.splice(index,1,'Jason');
people.push('Arthur');

for(i of people){
  console.log(i);
  if (i=='Mary'){break;}
}
let people2=people.slice(1,3);
console.log(people2);

console.log(people.indexOf('Mary'));
console.log(people.indexOf('Foo'));

let item = people[people.length-1];
console.log(item);

//exe loop4
let age = [20,5,12,43,98,55];
let sum = 0;
for(i of age){
  sum +=i;
}
console.log(sum);
for( i of age){
  if (i%2 ==0){console.log(i)}
}

console.log(Math.max(...age));
