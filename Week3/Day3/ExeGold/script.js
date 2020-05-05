//Conditionals
//Exe1
let z = parseInt(prompt("Enter a number"));
if (z%2 ==0){console.log('your number is even')}
else{console.log('your number is odd')}

//exe2
let x = parseInt(prompt("Enter a number"));
let y = parseInt(prompt("Enter a second number"));

if (x >y){alert('first number is bigger')}
else if(x<y){alert('second number is bigger')}
else{alert('are you kidding me?')}

//exe3
let language = prompt("What language do you speak?");
switch(language){
  case "French":
    alert("parle fu france?");
    break;
  case "Deutch":
    alert("Shprechen ze deutch?");
    break;
  case "English":
    alert("Do you speak english?");
    break;
  case "Hebrew":
    alert("ata medaber ivrit?");
    break;
  default:
    alert("I don't speal Elvish");
}

//Exe4
let grade = parseInt(prompt("what is your grade?"))

if (grade >=90){alert("A")}
else if(grade >=80){alert("B")}
else if(grade >=70){alert("C")}
else {alert("D")}


//Loops
//exe1
var family ={
  father:"Dad",
  mother : "Mom",
  child:"son"
}
var list = Object.getOwnPropertyNames(family);
for (l of list){
  console.log(l);
  console.log(family[l]);
}

//exe2
var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

console.log(building.number_levels);
 list = Object.getOwnPropertyNames(building.number_of_apt_by_level);
var num = 0;
for (i of list){
  if (i == 1 || i==3){
      console.log('Appartments on floor '+i+" is "+building.number_of_apt_by_level[i])
      num+=building.number_of_apt_by_level[i];
  }
}
console.log(num);

console.log("The second tennant is: "+building.name_of_tenants[1]+", he or she has "+
              building.number_of_rooms_and_rent[building.name_of_tenants[1]][0]+" rooms");
if (building.number_of_rooms_and_rent["Sarah"][1] + building.number_of_rooms_and_rent["David"][1] > building.number_of_rooms_and_rent["Dan"][1]){
  console.log("Dan's rent is too low, he should pay more");
  building.number_of_rooms_and_rent["Dan"][1] = 3000;
}

//exe3


person1={
  fullName:"Tiki Massla",
  mass: 95,
  height: 1.87,
  bmi:function() {
    return this.mass / (Math.pow(this.height, 2));
  }
}

person2={
  fullName:"Tiki tika Massla",
  mass:85,
  height: 1.87,
  bmi:function() {
    return this.mass / (Math.pow(this.height, 2));
  }
}

calc_bmi_diff(person1,person2);

function calc_bmi_diff(p1,p2){
  if (p1.bmi() > p2.bmi()){
    console.log(p1.fullName+" have a higher BMI");
  }
  else if (p1.bmi() < p2.bmi()){
    console.log(p2.fullName+" have a higher BMI");
  }
  else console.log("Oddly both of them have the same BMI")
}
