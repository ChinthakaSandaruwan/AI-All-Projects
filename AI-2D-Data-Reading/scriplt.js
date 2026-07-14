function test() {

    let data = [

        [1, 1, 1],
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 0]

    ];

    let weaight1 = 0.6;
    let weaight2 = 0.2;
    let bias = -2;
    let learningRate = 0.5;

    for (let i = 0; i < 10000; i++) {

        for (let j = 0; j < data.length; j++) {

            let input1 = data[j][0];
            let input2 = data[j][1];
            let expectedoutput = data[j][2];

            let weightedSum = (input1 * weaight1) + (input2 * weaight2) + bias;
            let activation = 1 / (1 + Math.exp(-weightedSum));

            let error = expectedoutput - activation;

            weaight1 = weaight1 + (learningRate * error * input1);
            weaight2 = weaight2 + (learningRate * error * input2);
            bias = bias + (learningRate * error);

            console.log(weaight1 + ", " + weaight2 + ", " + bias);

        }
    }
}


// after training the model, 

// function test() {



//     let weaight1 = 16.668593997275153;
//     let weaight2 = -0.40507301109831095;
//     let bias = -7.929103692496993;

//     let input1 = 1; //can change
//     let input2 = 1; // can change

//     let weightedSum = (weaight1 * input1) + (weaight2 * input2) + bias;
//     let activation = 1 / (1 + Math.exp(-weightedSum));
//     console.log(activation);

//     //    removed for loop

// }
