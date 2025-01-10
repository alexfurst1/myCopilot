const express = require("express");
const axios = require("axios");
const cors = require("cors");
const path = require("path");

const app = express();
const PORT = 3000;

// Enable CORS for all origins
app.use(cors());
app.use(express.json());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, "public")));

// Hugging Face API configuration
const HF_API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B";
const HF_API_KEY = "YOUR_HUGGING_FACE_API_KEY"; // Replace with your Hugging Face API key

// Endpoint to generate an academic outline
app.post("/generate-outline", async (req, res) => {
    const { topic } = req.body;

    const prompt = `
    Write a detailed academic paper outline on the topic: "${topic}".
    The outline should include:
    - Introduction (background, problem statement, objectives)
    - Literature Review (summary of key studies)
    - Methodology (approach, tools, and methods)
    - Results (expected findings or actual results)
    - Discussion (interpretation and significance of results)
    - Conclusion (summary, implications, and future directions)
    `;

    try {
        const response = await axios.post(
            HF_API_URL,
            { inputs: prompt },
            {
                headers: {
                    Authorization: `Bearer ${HF_API_KEY}`,
                },
            }
        );
        const generatedText = response.data.generated_text || "No text generated.";
        res.json({ outline: generatedText });
    } catch (error) {
        console.error("Error generating outline:", error.response?.data || error.message);
        res.status(500).json({ error: "Error generating outline. Please try again later." });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
