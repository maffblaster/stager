$(document).ready(function(){

    function pullPartitions(diskIndex){

        $.ajax({
            url: "/ajax/pullpartitions",
            type: "POST",
            data: {"part": diskIndex},
            success: function(result){

                var data = JSON.parse(result);
                var partCount = data.length;
                var canvasDataObject = [];

                for (i = 0; i < partCount; i++) {

                    var fullDiskLength = data[i].disk_geom_length;
                    var partLength = data[i].part_geom_length;
                    var partStart = data[i].part_geom_start;
                    var partEnd = data[i].part_geom_end;
                    var partWidth = (100 * (partLength / fullDiskLength));
                    var sectorSize = data[i].sector_size
                    var readablePartLength = ((partLength * sectorSize) / 1000000000);
                    var readableDiskLength = ((fullDiskLength * sectorSize) / 1000000000);

                    console.log(readableDiskLength);

                    canvasDataObject.push( {
                        type: "stackedBar",
                        dataPoints: [
                            {y: readablePartLength, label: "Partition " + data[i].number + " (GB)", indexLabelPlacement: "inside"},
                        ]}
                    );
                }

                console.log(canvasDataObject);

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
            }
        })
    }

    pullPartitions($('#disk_select').val());

    $("#disk_select").change(function(){

        pullPartitions($('#disk_select').val());

    })
})