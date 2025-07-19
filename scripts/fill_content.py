import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_FILE = "content/pages/about.md"
prompt = "Write a professional About page for a product studio named Lovable."

with open(INPUT_FILE, "r") as f:
    lines = f.readlines()

if any("ai_generated: true" in line for line in lines):
    print("Content already AI-generated. Skipping.")
else:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    new_content = response['choices'][0]['message']['content']

    with open(INPUT_FILE, "w") as f:
        f.write("---\n")
        f.write("title: \"About Us\"\n")
        f.write("description: \"Auto-filled by AI.\"\n")
        f.write("ai_generated: true\n")
        f.write("---\n\n")
        f.write(new_content)
