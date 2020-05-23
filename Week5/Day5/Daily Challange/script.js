let str =''
for(let i=1; i<=5;i++){
  for (let j = 1;j<=i;j++){
      str+="x";
  }
  console.log(str);
  str="";
}
str = "";
for(let i=0; i<5;i++){
  for (let j =0; j<=9;j++ ){
      if(j>=(5-i) && j<=(5+i)){
        str+="x";
      }
      else{
        str+=" ";
      }

  }
  console.log(str);
  str="";
}
