//
// Calculator
//
function plotmaxmin() {
    // Build query parameter
    var param = {};
    param["area1_maxmin"] = document.getElementById("area1_maxmin").value;
    param["area2_maxmin"] = document.getElementById("area2_maxmin").value;
    param["area3_maxmin"] = document.getElementById("area3_maxmin").value;
    param["maxmin_color1"] = document.getElementById("maxmin_color1").value;
    param["maxmin_color2"] = document.getElementById("maxmin_color2").value;
    param["maxmin_color3"] = document.getElementById("maxmin_color3").value;
    param["maxmin_year1"] = document.getElementById("maxmin_year1").value;
    param["maxmin_year2"] = document.getElementById("maxmin_year2").value;
    param["maxmin_year3"] = document.getElementById("maxmin_year3").value;
    param["data_num_maxmin"] = document.getElementById("data_num_maxmin").value;
    var query = jQuery.param(param);

    // Query with a new parameter 
    $.get("/plot/maxmin" + "?" + query, function(data) {
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
