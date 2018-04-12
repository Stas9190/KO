var prevVal;
var index;

function currentVal(val){
    prevVal = val;
    var elements = document.getElementsByTagName('select');
    var i = elements.length;
    masLength = i;
    while(i--) {
        if(elements[i].value == val) {
            index = i;
            break;
        }
    }
}

function Order(curVal){
    var el = document.getElementsByTagName('select');
    for (var i = 1; i < el.length; i++){
        if (el[i].value == curVal){
            if (i != index){
                el[i].value = prevVal;
            }
        }
    }
}