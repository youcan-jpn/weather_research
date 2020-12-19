//
// Calculator
//
function plotmaxmin() {
    // Build query parameter
    var param = {};
    param["area1"] = document.getElementById("area1").value;
    param["area2"] = document.getElementById("area2").value;
    param["area3"] = document.getElementById("area3").value;
    param["maxmin_color1"] = document.getElementById("maxmin_color1").value;
    param["maxmin_color2"] = document.getElementById("maxmin_color2").value;
    param["maxmin_color3"] = document.getElementById("maxmin_color3").value;
    param["maxmin_year1"] = document.getElementById("maxmin_year1").value;
    param["maxmin_year2"] = document.getElementById("maxmin_year2").value;
    param["maxmin_year3"] = document.getElementById("maxmin_year3").value;
    param["data_num"] = document.getElementById("data_num").value;
    var query = jQuery.param(param);

    // Query with a new parameter 
    $.get("/plot" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("maxmin_plot").addEventListener("click", function(){
    plotmaxmin();
}, false);
plotmaxmin();
