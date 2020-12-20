//
// Calculator
//
function plotrain() {
    // Build query parameter
    var param = {};
    param["area1"] = document.getElementById("area1").value;
    param["area2"] = document.getElementById("area2").value;
    param["area3"] = document.getElementById("area3").value;
    param["rain_color1"] = document.getElementById("rain_color1").value;
    param["rain_color2"] = document.getElementById("rain_color2").value;
    param["rain_color3"] = document.getElementById("rain_color3").value;
    param["data_num"] = document.getElementById("data_num").value;
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    var query = jQuery.param(param);

    // Query with a new parameter 
    $.get("/plot/rain" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("rain_plot").addEventListener("click", function(){
    plotrain();
}, false);
