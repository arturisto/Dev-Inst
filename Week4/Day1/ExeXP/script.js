//exe1

function checkDriverAge(age){

  if (Number(age) < 18) {
  return ("Sorry, you are too yound to drive this car. Powering off");
  } else if (Number(age) > 18) {
  return ("Powering On. Enjoy the ride!");
  } else if (Number(age) === 18) {
  return ("Congratulations on your first year of driving. Enjoy the ride!");
  }
}

console.log(checkDriverAge(Number(prompt("enter an age"))));


//exe2
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
function checkBasket(item){
  for (x in amazonBasket){
    if (x==item){
      alert("there such an item in my basket");
      return;
    }
  }
    alert("there is no such item in my basket");
}
checkBasket( prompt(" Guess what is in my basket!"));


// exe3
var stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
};

var shoppingList=['banana','orange','apple'];

function myBill(){
  let total_price = 0;
  for (x of shoppingList){
      if (stock[x] >0){
        stock[x]= stock[x]-1;
        total_price+=prices[x];
      }
  }
  console.log(total_price);
}
myBill();

//exe4

let days = parseInt(prompt("how many days will you be staying?"));
let dest = prompt("London, Paris or other?");
function hotel_cost (days){
  return days*140;
}

function flight_cost(d){
  if (d=="London"){return 183}
  else if(d=="Paris") {return 220}
  else return 300;
}
function car_cost (days){
  return days*40;
}
alert(hotel_cost(days) + flight_cost(dest)+car_cost(days));
