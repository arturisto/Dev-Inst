//exe1
let me = ["my","favorite","color","is","blue"];
array = me[0]+me[1]+me[2]+me[3]+me[4];
console.log(array);

//exe2
let string1 = "Green";
let string2 = "Cabbage";
let chars1 = string1.split('');
let chars2 = string2.split('');
let chars1_temp = [...chars1];
chars1.splice(0,2,chars2[0],chars2[1]);
chars2.splice(0,2,chars1_temp[0],chars1_temp[1]);
console.log(chars1.toString()+" "+chars2.toString());

//exe3

let num1 = prompt("Enter a number");
let num2 = prompt("Enter a second number");
let operand = prompt("enter math operand: + - * /");
let func = num1 +operand+ num2;
let num3 = eval(func);
alert("The answer to your query is: "+num3)
