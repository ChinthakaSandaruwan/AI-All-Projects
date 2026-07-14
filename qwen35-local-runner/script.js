async function AI() {

    let prompt = document.getElementById("x").value;

    console.log(prompt);

    let url = "http://localhost:11434/api/generate";
    let data = {
        model: "qwen3.5:0.8b",
        prompt: prompt,
        stream: false
    };

    let request = await fetch(
        url,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data),

        }
    );

    let result = await request.json();
    
    document.getElementById("output").innerText = result.response;

}   