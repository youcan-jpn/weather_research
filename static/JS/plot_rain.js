//
// Calculator
//
function plotrain() {
    // Build query parameter
    var param = {};
    param["area1_rain"] = document.getElementById("area1_rain").value;
    param["area2_rain"] = document.getElementById("area2_rain").value;
    param["area3_rain"] = document.getElementById("area3_rain").value;
    param["rain_color1"] = document.getElementById("rain_color1").value;
    param["rain_color2"] = document.getElementById("rain_color2").value;
    param["rain_color3"] = document.getElementById("rain_color3").value;
    param["data_num_rain"] = document.getElementById("data_num_rain").value;
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
