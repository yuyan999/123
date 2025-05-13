alert('外部js檔')
function myfunction(){
    var p=document.getElementById('text');
   p.innerHTML='<b>Java Hello SCU</b>';
}
function addbook(){
    console.log("list element running.")
    var list = document.getElementById('list');
    var book = document.getElementById('book');
    list.innerHTML+='<li>'+book.value+'</li>';

}
function randomtest(){
    var randata;
    randata = Math.random();
    document.getElementById("ex1").innerHTML = "Random number is ="+randata;
    if(randata>0.5){
        document.getElementById("ex2").innerHTML = 'Big Big';
    }
    else{
        document.getElementById("ex2").innerHTML = 'Small Small';
    }
}
function timefunction(){
    var timehour = new Date().getHours();
    var minutes = new Date().getMinutes();
    document.getElementById("hr").innerHTML = "Hours = "+timehour+" Minutes = "+minutes;
    if(timehour<=12){
        document.getElemetById('t').innerHTML = "上午";
    }
    if(timehour>12){
        document.getElementById('t').innerHTML = "下午";
    }
    if(timehour>=18){
        document.getElementById('t').innerHTML = "晚上";
    }
}
//-------------------------------------------------------
function weekfunction(){
    var dayweek = new Date().getDay();
    switch(dayweek){
        case 0:
            document.getElementById('w').innerHTML ="星期日";
            break;
        case 3:
            document.getElementById('w').innerHTML ="星期三";
            break;
        default:
            document.getElementById('w').innerHTML ="不明";
    }
}