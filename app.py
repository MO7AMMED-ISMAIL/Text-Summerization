#lib must install:
    # flask 
    # wikipedia 
    # pyarabic 
    # sumy or summa or gesmin || I used sumy 
#----------------------------------------

from flask import Flask ,render_template ,request
import wikipedia
#import summa
#from summa.summarizer import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

wikipedia.set_lang('ar')
app = Flask(__name__)

# summery
def summeryText(text):
    parser = PlaintextParser.from_string(text,Tokenizer("arabic"))
    summarizer_4 = TextRankSummarizer()
    summary =summarizer_4(parser.document , 10)
    text_summary=""
    for sentence in summary:
        text_summary+=str(sentence)
    return text_summary

@app.route("/", methods=["GET" , "POST"])
def index():
    return render_template('index.html')

@app.route("/result", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        title = request.form.get("text")
        text=wikipedia.page(title).content
        finalText = summeryText(text)
        return render_template('content.html',data=text,title=title,summerize=finalText)
    return render_template('content.html')

if __name__ == "__main__":
    app.run(debug=True)

