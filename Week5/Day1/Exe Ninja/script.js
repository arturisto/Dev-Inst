document.getElementById("calculate").addEventListener("click",calculateTip);

function calculateTip(){

  let billAmt =parseFloat(document.getElementById("billamt").value);
  let serviceQual =parseFloat(document.getElementById("serviceQual").value);
  let numOfPeople =parseInt(document.getElementById("peopleamt").value);
  if (isNaN(billAmt) || serviceQual==0){
    alert("Bill amount or the service quality is empty");
    return;
  }
  if(numOfPeople <=0 || isNaN(numOfPeople)){
    numOfPeople=1;
    document.getElementById("each").style.display="none";
  }
  let total = (billAmt*serviceQual)/numOfPeople;
total =  total.toFixed(2);

  document.getElementById("tip").innerHTML = total;
}


function validateEmail(e){
  let email = document.getElementById("email").value;
  email = email.toLowerCase();
  let letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  let numbers=[0,1,2,3,4,5,6,7,8,9];
  let arr =email.split("");

  let i = 0;
  if (arr.includes("@")==false){
    alert("Email must have @");
    return;
  }

  let before = email.split("@")[0];
  let after = email.split("@")[1];

  //check before
  arr = before.split("");
  //check dots of before
  if(arr.includes(".")){

      if(arr[0]=='.'){
        alert("can't have . at the beggining of the email");
        return;
      }
      for (x of arr){
        if (x=="."){i++;}
      }
      if(i>1){
        alert("can't have more than one . in the before @");
        return;
      }
  }
  //check letters and numbersx
console.log(arr[1]);
  for (x of arr){

      if(letters.includes(x)==false && numbers.includes(x)==false && x!=="."){
        alert("you can't have special characters in am email");

      }
    }

  arr=after.split("");

  i=0;
  for (x of arr){
    if (x=="."){i++;}
  }
  if(i!==1){
    alert("must have one . in the TLD");
    return;
  }

  for (x of arr){

    if(letters.includes(x)==false && numbers.includes(x)==false && x!=="."){
       //{
      alert("you can't have special characters in am email");
      return;
    }
  }

  if(i!=1){
    alert("you must have have only 1 dot in the TLD");
    return;
  }

  if(after.split(".")[1].length <2){
    alert("it is not valid TLD. Must have at least 2 chars");
    return
  }

  alert("it is a valid email");
  e.preventDefault();
}
