#python script to evaluaute test cases

#importing necessary libraries and variables
from evals.test_cases import test_cases 
from groq import Groq
from dotenv import load_dotenv
from prompt.sage import SAGE_SYSTEM_PROMPT

load_dotenv()
client = Groq()

EVAL_PROMPT = """
You are an expert AI evaluation system designed to assess the reasoning quality of an AI research assistant called Sage.

Your job is NOT to answer the question.

Your job is ONLY to evaluate how well the AI response performs.

---

## CONTEXT

You will be given:

1. USER INPUT (what the user asked)
2. MODEL OUTPUT (Sage's response)
3. EXPECTED BEHAVIOR (what a good response should look like)

---

##  PRIMARY GOAL

Evaluate the reasoning quality, academic usefulness, and correctness of the model output.

Sage is a research copilot. Good answers must be:
- logically structured
- academically sound
- neutral and unbiased
- factually correct or appropriately uncertain
- helpful for research or learning

---

##  SCORING RULES (1-10)

Score EACH category strictly from 1 to 10:

### 1. Reasoning Quality
Does the response show clear logical thinking steps?

### 2. Accuracy
Are the claims correct or appropriately qualified?

### 3. Clarity
Is the explanation easy to understand and well structured?

### 4. Academic Value
Is the response useful for research or learning?

### 5. Ethical & Bias Safety
Is the response neutral, safe, and free from bias or fabrication?

---

##  IMPORTANT RULES

- Do NOT hallucinate missing information
- Do NOT be lenient — be strict and consistent
- Penalize:
  - vague answers
  - unsupported claims
  - fake citations
  - overconfident wrong answers
- Reward:
  - structured reasoning
  - balanced arguments
  - academic tone
  - clear explanations

---

##  OUTPUT FORMAT (STRICT JSON ONLY)

Return ONLY valid JSON:

{
  "reasoning_quality": 1-10,
  "accuracy": 1-10,
  "clarity": 1-10,
  "academic_value": 1-10,
  "ethical_safety": 1-10,
  "overall_score": 1-10,
  "strengths": "short explanation of what was good",
  "weaknesses": "short explanation of what was wrong",
  "final_judgement": "pass | fail | borderline"
}

---

##  INPUT

USER QUESTION:
{input}

MODEL RESPONSE:
{output}

EXPECTED BEHAVIOR:
{expected_behavior}

---

Now evaluate strictly and fairly.
"""

request = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    temperature = 2,
    max_completion_tokens = 10,
    messages = [{"role":"system","content": EVAL_PROMPT},
                {"role":"user","content":f"evaluate this test cases {test_cases} on this prompt {SAGE_SYSTEM_PROMPT}"}]
)

print(request.choices[0].message.content)