let strings=[];

for(let i = 0; i<=4;i++){

    strings.push(prompt("please enter a word"));
}
console.log(strings[);

let word = null;
let max = 0
let counter = 0;
for (let i = 0; i<strings.length;i++){

    let s = strings[i];
    let arr = s.split("");
    var unique = Array.from(new Set(arr))
    for (let j of unique){
        for (let k=0; k<arr.length;k++ ){
          if(j===arr[k]){counter++;}
        }
        if (max<counter) {
          max=counter;
          word = strings[i];
        }
      }
}
console.log(word);
