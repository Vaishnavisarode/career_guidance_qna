#  Career Guidance Q&A System

A lightweight, CPU-friendly question-answering system that helps users get guidance on various tech careers. It uses a Hugging Face dataset with `role`, `question`, and `answer` columns, and retrieves the most relevant answer based on the user's query using semantic similarity.

---

##  Features

-  Ask career-related questions like skills, salary, or learning paths.
-  Uses pre-trained Sentence-BERT (`all-MiniLM-L6-v2`) for semantic search.
-  No fine-tuning or training required — retrieval-based.
-  Fully runs on CPU (no GPU needed).
-  Built on a Hugging Face dataset: [`Pradeep016/career-guidance-qa-dataset`](https://huggingface.co/datasets/Pradeep016/career-guidance-qa-dataset)
-  CLI-based interactive question-answering
-  Graceful exit on typing `exit`, `quit`, or `end`

---

##  Dataset Format

The dataset must contain the following columns:

| role            | question                                      | answer                                       |
|------------------|-----------------------------------------------|-----------------------------------------------|
| Data Scientist   | What skills are needed for this role?         | Python, statistics, ML, and data wrangling.  |
| Web Developer    | What tools should I learn to get started?     | HTML, CSS, JavaScript, and version control.  |

---

##  Installation

### 1. Clone this Repository

```bash
git clone https://github.com/your-username/career-guidance-qa.git
cd career-guidance-qa
```

### 2. Install Dependencies

```bash
pip install pandas sentence-transformers
```

>  Make sure your Python version is 3.7 or above.

---

##  How It Works

```python
from datasets import load_dataset
dataset = load_dataset("Pradeep016/career-guidance-qa-dataset")
```

- We load the dataset and combine `role` and `question` for context retrieval.
- User input is embedded using `SentenceTransformer`.
- Closest match is found using cosine similarity.
- The corresponding answer is shown.

---

##  Running the App

```bash
python main.py
```

Sample Interaction:

```
 Ask your career-related question: What skills do I need to become a Data Analyst?

 Suggested Career Role: Data Analyst
 Matched Question: What skills are required to become a Data Analyst?
 Answer: SQL, Python, data visualization, and statistical analysis.
```

To exit:
```bash
Type: exit | quit | end
```

---

##  Example Questions

- What is the salary for a Cloud Engineer?
- How do I transition into a career in UX design?
- What certifications should a DevOps Engineer have?
- What are the roles of a Business Analyst?

---

##  Technologies Used

-  [Sentence Transformers](https://www.sbert.net/)
-  [Hugging Face Datasets](https://huggingface.co/datasets)
-  Python 3.x
-  pandas

---

##  Future Improvements

- Add a Streamlit UI
- Top-3 answer suggestions
- Multi-turn Q&A or chat mode
- Add support for new roles and richer context

---
