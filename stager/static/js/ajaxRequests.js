$(document).ready(function(){

    function drawPartitions(partData, canvasWidth, diskWidth) {

        var canvas = document.getElementById('partCanvas');

        if (canvas.getContext) {
            var ctx = canvas.getContext('2d');
        };

        var scaleFactor = (1000 * (canvasWidth / diskWidth));

        console.log("scaleFactor: " + scaleFactor);

        for (i = 0; i < partData.length; i++){

            console.log(partData[i]);

            var geom_start = partData[i].part_geom_start;
            var geom_end = partData[i].part_geom_end;
            var end = geom_end * scaleFactor;
            var start = geom_start * scaleFactor;
            var width = (end - start) * scaleFactor;

            console.log("partWidth: " + width);

            ctx.fillRect(start, 0, width, 80);

        }
    }

    function pullPartitions(diskIndex){

        $.ajax({
            url: "/ajax/pullpartitions",
            type: "POST",
            data: {"part": diskIndex},
            success: function(result){

                var data = JSON.parse(result);
                var canvasDataObject = [];
                var fullDiskLength = data[0].disk_geom_length;

                for (i = 0; i < data.length; i++) {

                    var partLength = data[i].part_geom_length;
                    var partStart = data[i].part_geom_start;
                    var partEnd = data[i].part_geom_end;
                    var partWidth = (100 * (partLength / fullDiskLength));
                    var sectorSize = data[i].sector_size
                    var readablePartLength = ((partLength * sectorSize) / 1000000000);
                    var readableDiskLength = ((fullDiskLength * sectorSize) / 1000000000);

                    canvasDataObject.push( {
                        type: "stackedBar",
                        dataPoints: [
                            {y: readablePartLength, label: "Partition " + data[i].number + " (GB)", indexLabelPlacement: "inside"},
                        ]}
                    );
                }


                var canvasWidth = $("#chartContainer").width();

                $("#chartContainer").html('<canvas id="partCanvas" width="'+ canvasWidth +'" height="80" style="border:1px solid #000000;"></canvas>');

                drawPartitions(data, canvasWidth, fullDiskLength);

                console.log("canvasWidth: " + canvasWidth + " fullDiskLength: " + fullDiskLength);

                $("#chartContainer").append(JSON.stringify(data));

                //console.log(data);

/*
                var chart = new CanvasJS.Chart("chartContainer",

                    {
                         data: canvasDataObject,
                         axisY:{
                           maximum: readableDiskLength,
                           minimum: 0
                         },
                         animationEnabled: true,
                         animationDuration: 1000,
                         dataPointWidth: 100,
                         height: 100,
                         backgroundColor: null
                    }
                );

                chart.render();
*/

            }
        })
    }



    pullPartitions($("#disk_select").val());


    // Drop-down change
    $("#disk_select").change(function(){
        pullPartitions($("#disk_select").val());
    })

})