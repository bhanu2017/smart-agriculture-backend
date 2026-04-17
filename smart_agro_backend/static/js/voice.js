// =====================================
// GET SELECTED LANGUAGE
// =====================================

function getLang(){
  return localStorage.getItem("lang") || "en";
}



// =====================================
// VOICE MESSAGE DICTIONARY
// =====================================

const voiceMessages = {

listening:{
en:"Listening",
te:"వింటున్నాను",
hi:"सुन रहा हूँ"
},

crop:{
en:"Opening crop guide",
te:"పంట సూచన తెరవబడుతోంది",
hi:"फसल सलाह खुल रही है"
},

pesticide:{
en:"Opening pesticide scanner",
te:"కీటకనాశిని స్కానర్ తెరవబడుతోంది",
hi:"कीटनाशक स्कैनर खुल रहा है"
},

leaf:{
en:"Opening leaf disease detection",
te:"ఆకు వ్యాధి గుర్తింపు తెరవబడుతోంది",
hi:"पत्ते की बीमारी पहचान खुल रही है"
},

market:{
en:"Opening crop price information",
te:"పంట ధరల సమాచారం తెరవబడుతోంది",
hi:"फसल कीमत की जानकारी खुल रही है"
},

home:{
en:"Going to home page",
te:"ముఖ్య పేజీకి వెళ్తున్నాను",
hi:"मुख्य पेज पर जा रहा हूँ"
},

unknown:{
en:"Command not recognized",
te:"ఆదేశం గుర్తించబడలేదు",
hi:"कमांड पहचानी नहीं गई"
}

};



// =====================================
// GET MESSAGE BASED ON LANGUAGE
// =====================================

function getVoiceText(key){

const lang = getLang();

if(voiceMessages[key] && voiceMessages[key][lang]){
return voiceMessages[key][lang];
}

return voiceMessages[key]["en"];

}



// =====================================
// SPEAK FUNCTION
// =====================================

function speak(text){

if(!("speechSynthesis" in window)) return;

const lang = getLang();

const speech = new SpeechSynthesisUtterance(text);

if(lang === "te") speech.lang = "te-IN";
else if(lang === "hi") speech.lang = "hi-IN";
else speech.lang = "en-US";

speech.rate = 0.95;
speech.pitch = 1;

window.speechSynthesis.cancel();
window.speechSynthesis.speak(speech);

}



// =====================================
// AUTO PAGE VOICE MESSAGE
// =====================================

document.addEventListener("DOMContentLoaded", function () {

const message = document.body.getAttribute("data-voice");

if(message){

setTimeout(()=>{

speak(message);

},700);

}

});



// =====================================
// NAVIGATION WITH VOICE
// =====================================

function voiceNavigate(text,url){

speak(text);

setTimeout(()=>{
window.location.href = url;
},800);

}



// =====================================
// SPEECH RECOGNITION LANGUAGE
// =====================================

function getRecognitionLang(){

const lang = getLang();

if(lang === "te") return "te-IN";
if(lang === "hi") return "hi-IN";

return "en-US";

}



// =====================================
// START VOICE COMMAND
// =====================================

function startVoiceCommand(){

const SpeechRecognition =
window.SpeechRecognition || window.webkitSpeechRecognition;

if(!SpeechRecognition){
alert("Voice recognition not supported in this browser");
return;
}

const recognition = new SpeechRecognition();

recognition.lang = getRecognitionLang();

const btn = document.getElementById("voiceBtn");
const btnText = document.getElementById("voiceBtnText");

// Change button text
btnText.innerText = "🎤 Listening...";
btn.classList.remove("bg-green-600");
btn.classList.add("bg-red-500");

recognition.start();

recognition.onstart = () => {

speak(getVoiceText("listening"));

};

recognition.onresult = function(event){

const command =
event.results[0][0].transcript.toLowerCase();

console.log("Voice command:",command);

handleVoiceCommand(command);

};

recognition.onerror = () => {

speak(getVoiceText("unknown"));

};

recognition.onend = () => {

btnText.innerText = "🎤 Speak Command";
btn.classList.remove("bg-red-500");
btn.classList.add("bg-green-600");

};

}


// =====================================
// VOICE COMMAND ROUTER
// =====================================

function handleVoiceCommand(command){

// Crop Guide
if(
command.includes("crop") ||
command.includes("పంట") ||
command.includes("పంట సూచన") ||
command.includes("फसल")
){

voiceNavigate(getVoiceText("crop"),"/crop-guide/");

}


// Pesticide Scanner
else if(
command.includes("pesticide") ||
command.includes("కీటకనాశిని") ||
command.includes("कीटनाशक")
){

voiceNavigate(getVoiceText("pesticide"),"/pesticide-scanner/");

}


// Leaf Detection
else if(
command.includes("leaf") ||
command.includes("ఆకు") ||
command.includes("ఆకు వ్యాధి") ||
command.includes("पत्ता")
){

voiceNavigate(getVoiceText("leaf"),"/leaf-detection/");

}


// Market Price
else if(
command.includes("price") ||
command.includes("ధర") ||
command.includes("పంట ధర") ||
command.includes("मंडी") ||
command.includes("कीमत")
){

voiceNavigate(getVoiceText("market"),"/market-price/");

}


// Home
else if(
command.includes("home") ||
command.includes("ముఖ్య") ||
command.includes("मुख्य")
){

voiceNavigate(getVoiceText("home"),"/");

}


// Unknown command
else{

speak(getVoiceText("unknown"));

}

}