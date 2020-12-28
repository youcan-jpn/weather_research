//
// Calculator
//
function plotbar() {
    // Build query parameter
    var param = {};
    param["area_bar"] = document.getElementById("area_bar").value;
    param["start_bar"] = document.getElementById("start_bar").value;
    var query = jQuery.param(param);

    // Query with a new parameter 
    $.get("/plot/bar" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("bar_plot").addEventListener("click", function(){
    plotbar();
}, false);
