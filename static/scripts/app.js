var teleNex = angular.module('teleNex', []);
teleNex.controller("MainController", function($scope){
    // $scope.randomEntry = function(){
    //     console.log("test");
    //     happiness.y.push(Math.random()*10);
    //     sadness.y.push(Math.random()*10);
    //     fear.y.push(Math.random()*10);
    //     anger.y.push(Math.random()*10);
    //     neutral.y.push(Math.random()*10);
    //     var data = [happiness, sadness, fear, anger, neutral];
    //     Plotly.newPlot('myDiv', data, layout);
    // };

    $scope.plot_points = function(jd) {
        happiness.y.push(parseFloat(jd["happiness"]));
        sadness.y.push(parseFloat(jd["sadness"]));
        fear.y.push(parseFloat(jd["fear"]));
        anger.y.push(parseFloat(jd["anger"]));
        neutral.y.push(parseFloat(jd["neutral"]));
        contempt.y.push(parseFloat(jd["contempt"]));
        // surprise.y.push(parseFloat(jd["surprise"]));
        // disgust.y.push(parseFloat(jd["disgust"]));
        data = [happiness, sadness, fear, anger, neutral, contempt];
        Plotly.newPlot('myDiv', data, layout, {scrollZoom: true});
    }

    var happiness = {
        y: [0, 0],
        name: 'Happiness',
        type: 'scatter'
    };

    var sadness = {
        y: [0, 0],
        name: 'Sadness',
        type: 'scatter'
    };

    var fear = {
        y: [0, 0],
        name: 'Fear',
        type: 'scatter'
    };

    var anger = {
        y: [0, 0],
        name: 'Anger',
        type: 'scatter'
    };

    var neutral = {
        y: [0, 0],
        name: 'Neutral',
        type: 'scatter'
    };

    var contempt = {
        y: [0, 0],
        name: 'Contempt',
        type: 'scatter'
    }

    // var surprise = {
    //     y: [0, 0],
    //     name: 'Surprise',
    //     type: 'scatter'
    // }

    // var disgust = {
    //     y: [0, 0],
    //     name: 'Disgust',
    //     type: 'scatter'
    // }

    var layout = {
        title: 'Emotion Graph',
        xaxis: {
            title: 'Time'
        },
        yaxis: {
            title: 'Emotions'
        },
        displaylogo: false,
        showLink: false
    };
    
    data = [happiness, sadness, fear, anger, neutral, contempt];
    Plotly.newPlot('myDiv', data, layout, {scrollZoom: true});
});
