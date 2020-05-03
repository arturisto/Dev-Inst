//Exe 1

let addressNumber=16;
let addressStreet = "Shmuel Ha-Nagid";
let country= "Israel";
let global_address ="I live in "+addressStreet+" "+addressNumber+" ,"+country;

console.log(global_address);


//exe 2

let b_year = 1989;
let f_year = 2036;
let age = f_year-b_year;
console.log("I will be "+age+ " in "+f_year);

//exe 3
let pets = ['cat','dog','fish','rabbit','cow'];
console.log(pets[1]);
let index = pets.indexOf('rabbit');
pets.splice(index,1);
pets.push('horse');
console.log(pets.length);
console.log(pets.toString());
