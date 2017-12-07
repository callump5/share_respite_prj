queue()
    .defer(d3.json, '/donation-data/')
    .await(makeGraphs);


function makeGraphs(error, data) {

    data.forEach(function (d) {
        d.created_at = d['fields']['created_at'];
        d.amount = +d['fields']['amount'];
        d.user = +d['fields']['user'];
        d.pk = +d['pk'];
    });

    // Crossfilter Instance
    var ndx = crossfilter(data);

    // Crossfilter Dimensions
    var all = ndx.groupAll();

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



    var amount = ndx.dimension(function(d) { return d.amount })
    var sumAllAmount = amount.groupAll().reduceSum(function(d) {return d.amount;})



    var chart = dc.barChart("#date-graph");
    var dataTable = dc.dataTable("#data-table");
    var dataCount = dc.dataCount("#data-count");
    var numberDisplay = dc.numberDisplay("#total");


    dataCount
        .dimension(donationGroup)
        .group(all);

    numberDisplay
        .valueAccessor(function(d) { return d; } )
        .group(sumAllAmount);

    chart
        .width(768)
        .height(400)
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
