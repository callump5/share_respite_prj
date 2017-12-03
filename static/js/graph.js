queue()
    .defer(d3.json, '/donation-data/')
    .await(makeGraphs);

function makeGraphs(error, donationsData) {

    ndx = crossfilter(donationsData);

    amountDim = ndx.dimension(function (d) {
        return d;
    });

    amountGroup = amountDim.group();

    print(amountGroup)
}

makeGraphs()