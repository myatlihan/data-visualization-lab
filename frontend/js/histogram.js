const binsInput = document.getElementById("bins-input");
const binsValue = document.getElementById("bins-value");

const dataInput = document.getElementById("data-input");
const updateButton = document.getElementById("update-button");
const histogramContainer = document.getElementById("histogram-container");


const meanValue = document.getElementById("mean-value");
const medianValue = document.getElementById("median-value");
const modeValue = document.getElementById("mode-value");

const minimumValue = document.getElementById("minimum-value");
const maximumValue = document.getElementById("maximum-value");
const rangeValue = document.getElementById("range-value");

const q1Value = document.getElementById("q1-value");
const q3Value = document.getElementById("q3-value");
const iqrValue = document.getElementById("iqr-value");

const varianceValue = document.getElementById("variance-value");
const stdValue = document.getElementById("std-value");
const outliersValue = document.getElementById("outliers-value");

const sortedDataValue = document.getElementById("sorted-data-value");


binsInput.addEventListener("input", function () {
    binsValue.textContent = binsInput.value;
});


updateButton.addEventListener("click", async function () {

    const data = dataInput.value
        .split(",")
        .map(function (value) {
            return Number(value.trim());
        });


    const hasInvalidValue = data.some(function (value) {
        return Number.isNaN(value);
    });


    if (hasInvalidValue) {
        alert("Please enter only numbers.");
        return;
    }


    const bins = Number(binsInput.value);


    const chartData = [
        {
            x: data,
            type: "histogram",
            nbinsx: bins
        }
    ];


    Plotly.newPlot(
        histogramContainer,
        chartData
    );


    const response = await fetch("http://127.0.0.1:8000/statistics", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            data: data
        })
    });


    const statistics = await response.json();


    meanValue.textContent = statistics.mean;
    medianValue.textContent = statistics.median;
    modeValue.textContent = statistics.mode;

    minimumValue.textContent = statistics.minimum;
    maximumValue.textContent = statistics.maximum;
    rangeValue.textContent = statistics.range;

    q1Value.textContent = statistics.q1;
    q3Value.textContent = statistics.q3;
    iqrValue.textContent = statistics.iqr;

    varianceValue.textContent = statistics.variance;
    stdValue.textContent = statistics.standard_deviation;

    outliersValue.textContent = statistics.outliers.join(", ");

    sortedDataValue.textContent = statistics.sorted_data.join(", ");
});