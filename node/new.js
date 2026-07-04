var testTxt = "Coding Test";
function revString(testTxt)
{
    let newString="";
    for(let i=testTxt.length-1;i>=0;i--)
    {
        newString += testTxt[i];
    }
    return newString;
}
console.log(revString(testTxt))