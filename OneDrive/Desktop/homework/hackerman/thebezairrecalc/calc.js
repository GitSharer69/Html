function display(txt) {
    var op = document.getElementById(opscreen);
    opscreen.value = opscreen.value + txt;
}
    //var op = document.getElementById(opscreen)
    //opscreen.value = txt
    function calculate (){
        var op = document.getElementById(opscreen);
        opscreen.value = eval(opscreen.value);
        console.log(opscreen.value)
    }
    function ce (){
        var op = document.getElementById(opscreen);
        opscreen.value = 0;
    }
    //function del (){
        //var op = document.getElementById(opscreen);
        //str=opscreen.value;f
        //op.value = str.substring(0, str.length - 1);
    //}


    