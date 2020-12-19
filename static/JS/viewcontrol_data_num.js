function changeViewByDataNum() {
    var data_num = document.getElementById('data_num').value;
    var matches1 = document.getElementsByClassName('data1');
    var matches2 = document.getElementsByClassName('data2');
    var matches3 = document.getElementsByClassName('data3');

    if (data_num ==3) {
        for (var j=0; j<matches2.length; j++) {
            matches2[j].classList.remove('hidden');
        }
        for (var k=0; k<matches3.length; k++) {
            matches3[k].classList.remove('hidden');
        }
    } else if(data_num == 2) {
        for (var i=0; i<matches2.length; i++) {
            matches2[i].classList.remove('hidden');
        }
        for (var j=0; j<matches3.length; j++) {
            matches3[j].classList.add('hidden');
        }
    } else if(data_num == 1) {
        for (var i=0; i<matches2.length; i++) {
            matches2[i].classList.add('hidden');
        }
        for (var j=0; j<matches3.length; j++) {
            matches3[j].classList.add('hidden');
        }
    }
};

document.getElementById("data_num").addEventListener("input", function(){
    changeViewByDataNum();
}, false);
changeViewByDataNum();
