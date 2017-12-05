queue()
    .defer(d3.json, '/donation-data/')
    .await(makeGraphs);


function makeGraphs(error, data) {


    var formatYear = d3.time.format("%Y");
    var formatDate = d3.time.format("%m/%d/%Y");

    data.forEach(function (d) {
        d.created_at = d['fields']['created_at'];
        d.amount = +d['fields']['amount'];
        d.user = +d['fields']['user'];
        d.pk = +d['pk'];
    });

    console.log(data);

    // Crossfilter Instance
    var ndx = crossfilter(data);

    // Crossfilter Dimensions
    var amountDim = ndx.dimension(function(d) {return d.amount;});

    var pkDim = ndx.dimension(function (d) {return d.pk});

    // Crossfilter Group
    var donationGroup = pkDim.group().reduceSum(function(d) {return d.amount});
    var pkGroup = pkDim.group();

    // Graph Scale

    maxPk = pkDim.top(1)[0].pk;

    var userScale = d3.scale.linear()
        .domain([1, (maxPk +1)])
        .range(2000);


      amount = function (p) { return d.amount };



    var chart = dc.barChart("#date-graph");

    var dataTable = dc.dataTable("#data-table");

    chart
        .width(768)
        .height(480)
        .x(userScale)
        .yAxisLabel('Donation (GBP)', 25)
        .xAxisLabel('Per Donation')
        .dimension(pkDim)
        .group(donationGroup);

    dataTable
        .height(1500)
        .dimension(amountDim)
        .group(function (d) {
            return d.pk
        })
        .columns([
            {
                label: "Donation Date",
                format: function (d) { return d.created_at;}
            },
            {
                label: "Amount",
                format: function (d) { return d.amount;}
            }
        ]);


    dc.renderAll();
}

makeGraphs();
