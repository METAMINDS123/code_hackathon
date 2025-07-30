from transformers import pipeline

# Load HuggingFace summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_meal_description(desc: str):
    summary = summarizer(desc, max_length=50, min_length=15, do_sample=False)
    return summary[0]['summary_text']
