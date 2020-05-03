let array = ["Banana", "Apples", "Oranges", "Blueberries"];

let index =array.indexOf('Banana');
array.splice(index,1);
array.sort();
console.log(array.toString());
array.push('kiwi');
lindex =array.indexOf('Apples');
array.splice(index,1);
array.reverse();
console.log(array.toString());

let array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let fruit = array2[1][1][0];
console.log(fruit);
