var fs = require('fs');
var array = fs.readFileSync('input.txt').toString().split("\n");

console.log("Part one:", partOne())
function partOne(){
  let total = 0
  for(let i = 0, j = 1; j < array.length; i++, j++){
    if(array[j] > array[i]){
      total++
    }
  }
  return total + 1 //plus one because array
}

console.log("Part two:", partTwo());
function partTwo(){
  let total = 0
  for(let a = 0, b = 2, i = 1, j = 3; j < array.length; a++, b++, i++, j++){
    if(tally(array.slice(i, j + 1)) > tally(array.slice(a, b + 1))){
      total ++
    }
  }

  return total

  function tally(arr){
    return arr.reduce((out, curr) => out + curr)
  }
}