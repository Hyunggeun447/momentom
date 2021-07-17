//Array

/*
const mon = "mon";
const tue = "tue";
const wed = "wed";
const thu = "thu";
const fri = "fri";
const sat = "sat";
const sun = "sun";
*/



const dayOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

const nonsense = [1,2,3,4,5,6,7,8];


console.log(dayOfWeek);
console.log(nonsense);
console.log(dayOfWeek,nonsense);

console.log(dayOfWeek[2]);
console.log(dayOfWeek[5]);

dayOfWeek.push("hollyday");  // 마지막 elemunt 추가
console.log(dayOfWeek);

dayOfWeek.splice(2,2);    // splice(a,b) a부터 b개 제거
console.log(dayOfWeek);