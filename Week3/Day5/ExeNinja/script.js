var average = {
    student_name : null,
    score: 0,
}
var course = {
}
average.student_name = prompt("What is your name?");
while(true){
  let name = prompt("What is the name of the course?");
  let grade = parseInt(prompt("what is your exepcted grade of this course?"));
    let coefficient=0;
  while(true){
    coefficient = parseFloat(prompt("what is the coefficiant of this course(0-1)?"));
    if (coefficient >0 && coefficient <=1 ){break;}
  }
  course[name]= [grade,coefficient]
  if (confirm("Do you want to add another course")==false){break};
}
average.courses=course;
let list = Object.getOwnPropertyNames(average.courses)
for(i of list){
    average.score += average.courses[i][0]*average.courses[i][1]
}
average.score =(average.score/list.length).toFixed(2);
alert("The average score for "+average.student_name+" is: "+average.score)
