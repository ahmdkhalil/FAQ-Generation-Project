from flask import Flask, request, render_template, flash, redirect
import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load the pre-trained clustering model and vectorizer
with open("../models/faq_cluster_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
with open("../models/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part", "error")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected", "error")
            return redirect(request.url)

        try:
            data = pd.read_csv(file)
            if "Description" not in data.columns:
                flash("File must contain a 'Description' column", "error")
                return redirect(request.url)
            faqs = generate_faqs(data)
            return render_template("results.html", faqs=faqs)
        except Exception as e:
            flash(f"Error processing file: {str(e)}", "error")
            return redirect(request.url)

    return render_template("index.html")

def generate_faqs(data):
    data['cleaned_text'] = data['Description'].apply(lambda x: x.lower())
    vectors = vectorizer.transform(data['cleaned_text'])

    # Predict clusters using the loaded model
    data['cluster'] = model.predict(vectors)

    faqs = {}
    for cluster in data['cluster'].unique():
        cluster_data = data[data['cluster'] == cluster]
        representative_question = cluster_data['Description'].iloc[0]
        related_questions = "\n".join(cluster_data['Description'].tolist())
        faqs[representative_question] = related_questions

    return faqs

if __name__ == "__main__":
    app.run(debug=True)
