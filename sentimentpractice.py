import os
import google.generativeai as genai
os.environ["GOOGLE_API_KEY"]="AIzaSyAF1tmgQLQIIOJ5J-7AcwxvnG04wOfaxNg"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

generation_configur={
    "temperature":0.1,
     "top_p":0.25,
     "top_k":24,
     'response_mime_type':"text/plain",
     'max_output_tokens':8195,
}
safety_settings=[
    {
        "category":"HARM_CATEGORY_HARASSMENT",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category":"HARM_CATEGORY_HATE_SPEECH",
        'threshold':"BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        'category':"HARM_CATEGORY_SEXUALLY_EXPLICIT",
         'threshold':"BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        'category':'HARM_CATEGORY_DANGEROUS_CONTENT',
        'threshold':'BLOCK_MEDIUM_AND_ABOVE',
    }
]
system_instruction="you are a sentiment analyzer, give uor response as happy emoji for postive and cry emoji for negative"

model=genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    safety_settings=safety_settings,
    generation_config=generation_configur,
    #system_instruction="you are a translator and can translate the user input into english, the input language could be any  "
    system_instruction=system_instruction
)
chat_session=model.start_chat(
    history=[
        {
            'role':'user',
            'parts':["der sohn ist sehr nett/n"]
        },
        {
            'role':'model',
             'parts':['positive/n']
        },  
    ]
)
response=chat_session.send_message("die frau und der mann bist sehr klunge")
print(response.text)
