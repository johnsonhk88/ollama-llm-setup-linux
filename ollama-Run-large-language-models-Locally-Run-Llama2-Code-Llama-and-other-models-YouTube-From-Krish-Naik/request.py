import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {"Content-Type": 
          "application/json"}

history = []


def generateResponse(prompt):
    history.append(prompt)
    finalPrompt = "\n".join(history)

    # define model information
    data = {
        "model": "mlguru",
        "prompt": finalPrompt,
        "stream": False
    }
    # send request by POST method
    response =requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        ret = response.text 
        data = json.loads(ret)
        actualResponse = data["response"]
        return actualResponse
    else:
        print("Error: ", response.text)


# create UI interface
interface =gr.Interface(
    fn = generateResponse, # function
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt"),
    outputs="text"
)

interface.launch()