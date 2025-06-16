from datasets import load_dataset
import pandas as pd

dataset = load_dataset("Pradeep016/career-guidance-qa-dataset")
print(dataset)               # Shows info about splits
print(dataset['train'][0])   # Shows the first example


# Convert to DataFrame
df = pd.DataFrame(dataset['train'])

# Save to CSV
df.to_csv("career_guidance_qna.csv", index=False)

print("Saved to career_guidance_qna.csv")
