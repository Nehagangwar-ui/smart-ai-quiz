async function generateQuiz(){

let ques = document.getElementById("ques").value
let topic = document.getElementById("topic").value
let resultBox = document.getElementById("result")

// check empty input
if(ques === "" || topic === ""){
    alert("Please enter topic and number of questions")
    return
}

// loading message
resultBox.innerText = "Generating quiz... please wait ⏳"

try{

let response = await fetch("http://127.0.0.1:5000/quiz",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
questions:ques,
topic:topic
})

})

let data = await response.json()

resultBox.innerText = data.quiz

}

catch(error){

resultBox.innerText = "❌ Error generating quiz. Please check backend server."

console.log(error)

}

}