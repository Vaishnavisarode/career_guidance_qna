
from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Load dataset
df = pd.read_csv("career_guidance_qna.csv")  # CSV must have 'role', 'question', 'answer'
df['combined'] = df['role'] + ": " + df['question']

# Load CPU-compatible model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode the entire corpus
corpus_embeddings = model.encode(df['combined'], convert_to_tensor=True)

print("\n Welcome to the Career Guidance Q&A System")
print("Ask anything about tech careers.")
print("Type 'exit', 'quit', or 'end' to leave.\n")

while True:
    user_query = input("Ask your career-related question: ")

    if user_query.lower() in ['exit', 'quit', 'end']:
        print("Exiting Career Guidance Q&A. Best of luck with your future!")
        break

    query_embedding = model.encode(user_query, convert_to_tensor=True)

    # Compute similarity scores
    cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    top_match = cos_scores.argmax().item()

    print("\n Suggested Career Role:", df.loc[top_match]['role'])
    print("Matched Question:", df.loc[top_match]['question'])
    print("Answer:", df.loc[top_match]['answer'])
    print("--------------------------------------------------")

