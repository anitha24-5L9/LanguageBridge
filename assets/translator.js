const inputText =
document.getElementById("inputText");

inputText.addEventListener("input", () => {
    document.getElementById("charCount").textContent =
    inputText.value.length;
});

async function translateText(){

    const text =
    document.getElementById("inputText").value;

    const source =
    document.getElementById("sourceLang").value;

    const target =
    document.getElementById("targetLang").value;

    if(text.trim()===""){
        alert("Enter text first");
        return;
    }

    document.getElementById("loading").style.display="block";

    try{

        const response =
        await fetch("/translate",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                text:text,
                source:source,
                target:target
            })
        });

        const data = await response.json();

        document.getElementById("outputText").value =
        data.translated_text;

        saveHistory(
            text,
            data.translated_text
        );

    }catch(error){

        alert("Translation Failed");

    }finally{

        document.getElementById("loading").style.display="none";
    }
}

function copyText(){

    navigator.clipboard.writeText(
        document.getElementById("outputText").value
    );

    alert("Copied!");
}

function speakText(){

    const text =
    document.getElementById("outputText").value;

    const speech =
    new SpeechSynthesisUtterance(text);

    speechSynthesis.speak(speech);
}

function clearAll(){

    document.getElementById("inputText").value="";
    document.getElementById("outputText").value="";
    document.getElementById("charCount").textContent="0";
}

function swapLanguages(){

    let source =
    document.getElementById("sourceLang");

    let target =
    document.getElementById("targetLang");

    let temp = source.value;

    source.value = target.value;
    target.value = temp;
}

function toggleDarkMode(){

    document.body.classList.toggle("dark");
}

function saveHistory(original,translated){

    let history =
    JSON.parse(
        localStorage.getItem("history")
    ) || [];

    history.unshift(
        `${original} ➜ ${translated}`
    );

    history = history.slice(0,5);

    localStorage.setItem(
        "history",
        JSON.stringify(history)
    );

    loadHistory();
}

function loadHistory(){

    let history =
    JSON.parse(
        localStorage.getItem("history")
    ) || [];

    const list =
    document.getElementById("historyList");

    list.innerHTML="";

    history.forEach(item=>{

        const li =
        document.createElement("li");

        li.textContent=item;

        list.appendChild(li);
    });
}

loadHistory();