To run this application, you need to provide your Google Gemini API key.

1.  **Create a `.env` file:** In the `streamlit_chatbot` directory, create a file named `.env`.

2.  **Add your API key to the `.env` file:**
    ```
    GEMINI_API_KEY=YOUR_API_KEY
    ```
    Replace `YOUR_API_KEY` with your actual Gemini API key. You can get a key from [Google AI Studio](https://aistudio.google.com/app/apikey).

3.  **Run the app:** Navigate to the `streamlit_chatbot` directory in your terminal and run the app using:
    ```bash
    streamlit run app.py
    ```