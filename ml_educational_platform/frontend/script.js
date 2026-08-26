document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault(); // Prevent page refresh

    // 1. Get values from the input fields
    const sqft = parseFloat(document.getElementById('sqft').value);
    const beds = parseInt(document.getElementById('beds').value);
    const resultContainer = document.getElementById('result-container');
    const priceDisplay = document.getElementById('price-value');
    const rawJsonDisplay = document.getElementById('raw-json');
    const button = e.target.querySelector('button');

    // UI updates while loading
    button.textContent = "Calculating...";
    button.disabled = true;

    try {
        // 2. Make the POST request to our FastAPI backend
        // Note: Make sure the FastAPI server is running on localhost:8000
        const response = await fetch('http://127.0.0.1:8000/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ sqft: sqft, beds: beds })
        });

        // 3. Parse the JSON response
        const data = await response.json();

        // 4. Update the UI with the result
        if (response.ok && !data.error) {
            // Format number as currency
            const formatter = new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: 'USD',
                maximumFractionDigits: 0
            });
            
            priceDisplay.textContent = formatter.format(data.estimated_price);
            rawJsonDisplay.textContent = JSON.stringify(data, null, 2);
            resultContainer.classList.remove('hidden');
        } else {
            priceDisplay.textContent = "Error!";
            rawJsonDisplay.textContent = data.error || "An unknown error occurred.";
            resultContainer.classList.remove('hidden');
        }

    } catch (error) {
        console.error("Fetch error:", error);
        priceDisplay.textContent = "Connection Error!";
        rawJsonDisplay.textContent = "Could not connect to API. Is the FastAPI server running on port 8000?";
        resultContainer.classList.remove('hidden');
    } finally {
        // Reset UI
        button.textContent = "Predict Price";
        button.disabled = false;
    }
});
