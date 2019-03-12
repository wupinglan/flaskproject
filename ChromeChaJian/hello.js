
document.addEventListener("click",getall,false)

function getall(e){
    console.log(e.target);
    console.log(e.target.id)
    // var style = window.getComputedStyle(e.target);//获取元素的css属性
    console.log(e.target.value);
}
