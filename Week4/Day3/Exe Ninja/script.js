function createCalendar(elem, year, month){

  let th =null;
  let tr = document.createElement("tr");
  let l = ["MO","TU","WE","TH","FR","SA","SU"];

  for (let i =0; i<7; i++){
    th = document.createElement("th");
    th.innerHTML=l[i];
    tr.appendChild(th);
  }
  let thead = document.createElement("thead");
  thead.appendChild(tr);
  elem.appendChild(thead);
  let tbody = document.createElement("tbody");
  elem.appendChild(tbody);
  let firstDay = new Date(year,month-1);
  console.log(firstDay);
  var firstDayOfWeek = firstDay.getDay()
  var daysInMonth = new Date(year, month+1,0).getDate();
  console.log(daysInMonth+firstDayOfWeek);
  let flag = false;
  for (let i=0; i <daysInMonth+firstDayOfWeek;i++){
      if (i%7 == 0){
        th = document.createElement("tr");
        flag = true;
      }
      tr = document.createElement("td");
      if (i <=6 && i<firstDayOfWeek){
        tr.innerHTML='.';
      }
      else{
        tr.innerHTML=i-firstDayOfWeek+1;
      }
      th.appendChild(tr);
      if (i%6 == 0){
        elem.appendChild(th);
        flag = false;
      }
  }
  if (flag){
    elem.appendChild(th);
  }

  document.body.appendChild(elem);


}
let year = parseInt(prompt("please enter year, nyashush: "));
let month = parseInt(prompt("please enter a month, kotik: "));
let cal = document.createElement("table");
createCalendar(cal, year ,month)
