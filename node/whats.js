var testArr = ["One", "Two", 1,"three",5];
let newarray= [];
for(let i=0;i<testArr.length;i++)
    {
      console.log(typeof testArr[i])
      if(typeof testArr[i]== "number")
      {
          testArr.splice(i,i)
      }
      
    }
    console.log(testArr);