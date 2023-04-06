import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

class SentimentAnalysisTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis de sentimiento")

        # Crear widgets
        self.input_label = ttk.Label(self.root, text="Texto de entrada:")
        self.input_label.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 10))

        self.input_text = tk.Text(self.root, width=60, height=10)
        self.input_text.grid(row=1, column=0, padx=20)

        self.analyze_button = ttk.Button(self.root, text="Analizar", command=self.analyze_sentiment)
        self.analyze_button.grid(row=2, column=0, pady=(10, 20))

        self.result_label = ttk.Label(self.root, text="Resultado:")
        self.result_label.grid(row=3, column=0, sticky="w", padx=20)

        self.sentiment_label = ttk.Label(self.root, text="")
        self.sentiment_label.grid(row=4, column=0, padx=20)

    def analyze_sentiment(self):
        input_text = self.input_text.get("1.0", tk.END).strip()

        if not input_text:
            self.sentiment_label["text"] = "Por favor, ingrese texto para analizar."
            return

        analysis = TextBlob(input_text)
        sentiment_polarity = analysis.sentiment.polarity

        if sentiment_polarity > 0:
            sentiment = "Positivo"
        elif sentiment_polarity < 0:
            sentiment = "Negativo"
        else:
            sentiment = "Neutral"

        self.sentiment_label["text"] = f"Sentimiento: {sentiment} ({sentiment_polarity:.2f})"

if __name__ == "__main__":
    root = tk.Tk()
    SentimentAnalysisTool(root)
    root.mainloop()
