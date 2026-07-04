function checkWorkingHour()
{
    const now = new Date();
    day = now.getDay()
    time = now.getHours()
    
    if(day>=1 && day<=5 && time>=8 && time<=17)
    {
        return true;
    }
    else return false;
    
}
console.log(checkWorkingHour())