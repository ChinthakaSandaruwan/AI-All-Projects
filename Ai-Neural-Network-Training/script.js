
let input1 = 1;
let input2 = 1;
let expectedOutput = 1;

let weight1 = 0.6;
let weight2 = 0.2;
let bias = -2;

let learningRate = 0.5;


function calculate() {

    for (let i = 0; i < 1000; i++) {

        let weightSum = (input1 * weight1) + (input2 * weight2) + bias;
        let activationOutput = 1 / (1 + Math.exp(-weightSum));
        console.log("Activation Output: " + activationOutput);

        let error = expectedOutput - activationOutput;


        weight1 = weight1 + (learningRate * error * input1);
        weight2 = weight2 + (learningRate * error * input2);
        bias = bias + (learningRate * error);

        console.log("Updated weight and bias values");
        console.log("weight1: " + weight1);
        console.log("weight2: " + weight2);
        console.log("bias: " + bias);

    }


}