/**
 * Created by hduser on 26/04/17.
 */


var colors = d3.scale.category10();
var bg_col = "#ABDDA4";
var highlight_col = "#17becf";

function changecolor(data, map) {
    refresh(map, bg_col);
    var index = 0;
    for (var i in data) {
        if(data[i].value > data[index].value) {
            index = i;
        }
    }
    region = data[index].region;
    var col = 12345 * 50;

    //gulf
    if(region == 0) {
        map.updateChoropleth({
            BHR: highlight_col,
            IRQ: highlight_col,
            QAT: highlight_col,
            KWT: highlight_col,
            SAU: highlight_col,
            ARE: highlight_col,
            YEM: highlight_col,
            OMN: highlight_col
        });
    } else if(region == 1) {//egy
        map.updateChoropleth({
            EGY: highlight_col
        });
    } else if(region == 2) {//Lav
        map.updateChoropleth({
            SYR: highlight_col,
            LBN: highlight_col,
            ISR: highlight_col,
            JOR: highlight_col,
            PSE: highlight_col
        });

    } else if(region == 3) {//Nor
        map.updateChoropleth({
            DZA: highlight_col,
            LBY: highlight_col,
            MAR: highlight_col,
            TUN: highlight_col,
            ESH: highlight_col
        });
    } else {
        refresh(map, highlight_col);
    };

}
function refresh(map, color) {

    map.updateChoropleth({
        //gulf
        BHR: color,
        IRQ: color,
        QAT: color,
        KWT: color,
        SAU: color,
        ARE: color,
        YEM: color,
        OMN: color,

        //egy
        EGY: color,

        //lav
        SYR: color,
        LBN: color,
        ISR: color,
        JOR: color,
        PSE: color,

        //nor
        DZA: color,
        LBY: color,
        MAR: color,
        TUN: color,
        ESH: color

    });
}
