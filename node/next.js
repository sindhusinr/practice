var testArr = ["One", "Two", "Three", "Four"],opt="";
var Alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
function option(testArr)
{
   for(let i=0; i<testArr.length;i++)
   {
        opt += Alp[i]+")"+testArr[i]+" ";

   }
   return opt;
}
console.log(option(testArr))
