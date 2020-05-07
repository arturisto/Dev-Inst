//exe1

let arr=[5,-3,2];
let temp = 0
if (arr[1] < arr[0] && arr[1] < arr[2]){
    temp = arr[1];
    arr[1]=arr[0];
    arr[0]=temp;

    if (arr[1] > arr[2]){
      temp = arr[2];
      arr[2]=arr[1];
      arr[1]=temp;
    }
}
else if (arr[2] < arr[0] && arr[2] < arr[1]){
    temp = arr[2];
    arr[2]=arr[0];
    arr[0]=temp;

    if (arr[1] > arr[2]){
      temp = arr[2];
      arr[2]=arr[1];
      arr[1]=temp;
    }
}
else   if (arr[1] > arr[2]){
    temp = arr[2];
    arr[2]=arr[1];
    arr[1]=temp;

}
console.log(arr);


//exe2
arr = [-3, -3, -2];

if (arr[0] ==0 || arr[1]==0 || arr[2]==0){
  console.log("+");
}
else if (arr[0] <0 && arr[1] >0 && arr[2]>0){
  console.log("-");
}
else if (arr[0] >0 && arr[1] <0 && arr[2]>0){
  console.log("-");
}
else if (arr[0] >0 && arr[1] >0 && arr[2]<0){
  console.log("-");
}
else if (arr[0] <0 && arr[1] <0 && arr[2]<0){
  console.log("-");
}
else {console.log("+")};


//exe3
let grades = {
    david:  80,
    vinoth: 77,
    divya: 88,
    ishitha: 95,
    thomas: 68,
    lea: 77
}
let best = 0;
let name_best = null
let name_worst = null
let worst = 100;
arr=[];
for (let grade in grades){
    if (best <grades[grade]){
      best = grades[grade];
      name_best=grade;
    }
    if (worst >grades[grade]){
      worst=grades[grade];
      name_worst=grade;
    }
    for (let grade2 in grades){
      if (grade2 != grade && grades[grade] == grades[grade2] && arr.includes(grade)==false){
        arr.push(grade);
      }
    }
}
console.log('The best student is ' +name_best+' with a score of '+ best);
console.log('The worst student is ' +name_worst+' with a score of '+ worst);
console.log(arr);
