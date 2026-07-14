import ollama from 'ollama';
import express from 'express';

const app = express();

app.use(express.static('public'));

app.get("/chinthaka", async (req, res) => {

    const response = await ollama.chat({
        model: 'qwen3.5:0.8b',
        messages: [{ role: 'user', 
        content: 'What is the capital of France?'
     }
     
    ],
    });

    res.send(response.message.content);

});

app.listen(3000);
