function styleCalculator(){

  let elem =  document.querySelectorAll(".input")[0];
  elem.setAttribute("style","width:520px; height:70px; font-size:60px; border-width:2px; border-radius:3px;")

  elem = document.querySelectorAll(".number");
  for (let i =0; i<elem.length;i++ ){
    elem[i].setAttribute("style","width:128px;font-size:3em;background-color:green;color:white;")
  }

  elem = document.querySelectorAll(".sign");
  for (let i =0; i<elem.length;i++ ){

    elem[i].setAttribute("style","width:128px; font-size:3em;background-color:orange;color:white;")
  }
  elem = document.querySelectorAll(".reset")[0];
  elem.setAttribute("style","width:260px; font-size:3em;background-color:blue;color:white;")
  elem = document.querySelectorAll(".clear")[0];
  elem.setAttribute("style","width:260px; font-size:3em;background-color:red;color:white;")
}


function my_f(input){
  switch(input){
    default:
         elem = document.querySelectorAll(".input")[0];
         var text = elem.value;
         elem.value=text.concat(input);
         break;
    case '.':
         elem = document.querySelectorAll(".input")[0];
         var text = elem.value;
         elem.value=text.concat(input);
         break;
    case 'reset':
         memory=[ ];
         document.querySelectorAll(".input")[0].value="";
         break;
    case 'clear':
         document.querySelectorAll(".input")[0].value="";
         break;
    case '+':
         memory.push(parseFloat(document.querySelectorAll(".input")[0].value));
         memory.push('+');
         document.querySelectorAll(".input")[0].value="";
         break;
    case "-":
          memory.push(parseFloat(document.querySelectorAll(".input")[0].value));
          memory.push('-');
          document.querySelectorAll(".input")[0].value="";
          break;
    case "*":
          memory.push(parseFloat(document.querySelectorAll(".input")[0].value));
          memory.push('*');
          document.querySelectorAll(".input")[0].value="";
          break;
    case "/":
          memory.push(parseFloat(document.querySelectorAll(".input")[0].value));
          memory.push('/');
          document.querySelectorAll(".input")[0].value="";
          break;
    case "=":
          memory.push(parseFloat(document.querySelectorAll(".input")[0].value));
          var result = eval(memory.join(""));
          document.querySelectorAll(".input")[0].value= result;
          memory=[];
          break;
  }


}

styleCalculator();
var memory=[];
