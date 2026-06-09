from flask import Flask, render_template,request,jsonify
import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat',methods=['POST'])
def chat():
    data = request.get_json()
    print(data)
    user_message = data.get("message","")

    response = client.chat.completions.create(
        model = "gpt-5.4-mini",
        messages=[
            {"role":"system","content":"""you are a helpful assistant , 
                and you have to answer clients questions in arabic even if they ask in english
                if they asks you to answer in english say "انا مساعد ذكي و اجيد التحدث بالعربية فقط"
             """},
                {"role":"user",'content':user_message}
        ]
    )
    print(response)

    reply = response.choices[0].message.content

    return jsonify({"reply":reply})



if __name__ == '__main__':
    app.run(debug=True)