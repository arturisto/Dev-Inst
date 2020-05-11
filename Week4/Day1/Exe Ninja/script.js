let list = [1,2,3,3,3,3,4,5];

function toSet(l){

  return new Set(l);
}

let mySet = toSet(list);

console.log(mySet);


//exe2

list = [1,0,3,100, 99, 2, 99,'a', 3, 4, 2];

function findBiggest(l){
  let max = 0
  if (l.length==0){
    return 0;
  }
  for (x of l){
      if(isNaN(x)){
        continue;
      }
      else{
        if (max<x) {
          max=x;
        }
      }
  }
  return max;
}
let x_max = findBiggest(list);
console.log(x_max)
