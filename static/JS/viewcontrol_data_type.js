function changeViewByDataType() {
    var target_value = document.getElementById('data_type').value;
    let graphs = ['maxmin', 'rain'];
    for(let item of graphs) {
        if(item == target_value) {
            var display_item = document.getElementById(item);
            display_item.classList.remove('hidden');
        } else {
            var hidden_item = document.getElementById(item);
            hidden_item.classList.add('hidden');
        };
    };
};

document.getElementById("data_type").addEventListener("input", function(){
    changeViewByDataType();
}, false);
changeViewByDataType();