
let cpuData = []
let labels = []


const ctx = document.getElementById('cpuChart').getContext('2d')


const chart = new Chart(ctx, {

type: 'line',

data: {

labels: labels,

datasets: [{
label: "CPU Usage %",
data: cpuData,
borderColor: "cyan",
fill: false
}]

},

options:{
responsive:true
}

})


function simulate(){

fetch("/simulate")

.then(res => res.json())

.then(data => {

document.getElementById("cpu").innerText = data.cpu + "%"

document.getElementById("time").innerText = data.processing_time + " sec"

document.getElementById("servers").innerText = data.servers

document.getElementById("suggestion").innerText = data.suggestion


cpuData.push(data.cpu)
labels.push("Req " + labels.length)


chart.update()

})

}