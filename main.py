from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from scipy.special import softmax
# from pydantic import BaseModel, typing
# from pyabsa import ATEPCCheckpointManager

# load model
# berty = "cardiffnlp/twitter-roberta-base-sentiment"
# model = AutoModelForSequenceClassification.from_pretrained(berty)
# tokenizer = AutoTokenizer.from_pretrained(berty)
# print(tokenizer.model_max_length)
# labels = ["Negative", "Neutral", "Positive"]



# aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='english', auto_device=True)

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Item(BaseModel):
#     input_text: str

# class AspectItems(BaseModel):
#     comments: list[str]


# class BulkItem(BaseModel):
#     data: list[str]
#     x: typing.Any

# def find_highest_number(dictionary):
#     max_pair = max(dictionary.items(), key=lambda x: x[1])
#     return max_pair

@app.get("/")
def index():
    return {"details": "Hello!"}


# @app.post("/analyze/tweet")
# def generate(item: Item):
#     input_text = item.input_text


#     encoded_tweet = tokenizer(input_text, return_tensors="pt")
#     output = model(**encoded_tweet)

#     scores = output[0][0].detach().numpy()

#     scores = softmax(scores)

#     response = {}
#     for i in range(len(scores)):
#         key = labels[i]
#         value = str(scores[i])
#         response[key] = value
#     print(response)
#     return response


# @app.post("/analyze/tweet-bulk")
# def generate(item: BulkItem):

#     for comment in item.x:
#         print(comment)
#         trimmed_text =  comment.get("comment")[0:512]

#         encoded_tweet = tokenizer(trimmed_text, return_tensors="pt")
#         output = model(**encoded_tweet)
#         scores = output[0][0].detach().numpy()
#         scores = softmax(scores)
                
#         current_sentiment = {}
            
#         for i in range(len(scores)):
#             key = labels[i]
#             value = str(scores[i])
#             current_sentiment[key] = value


#         (sentiment, value) = find_highest_number(current_sentiment)
#         comment["sentiment"] = sentiment

#         inference_source = [trimmed_text]
#         atepc_result = aspect_extractor.extract_aspect(inference_source=inference_source, pred_sentiment=True)
        


#         aspects = atepc_result[0].get('aspect')
#         sentiment = atepc_result[0].get('sentiment')
      
#         mappedSentiment = {}

#         for i in range(len(sentiment)):
#             key = aspects[i]
#             value = sentiment[i]
#             mappedSentiment[key] = value

#         comment["aspects"] = mappedSentiment

#         if comment.get("replies") is not None and len(comment.get("replies")) >= 1:
#             for reply in comment.get("replies"):
#                 trimmed_text =  comment.get("comment")[0:512]
#                 encoded_tweet = tokenizer(trimmed_text, return_tensors="pt")
#                 output = model(**encoded_tweet)
#                 scores = output[0][0].detach().numpy()
#                 scores = softmax(scores)
                
#                 current_sentiment = {}
            
#                 for i in range(len(scores)):
#                     key = labels[i]
#                     value = str(scores[i])
#                     current_sentiment[key] = value


#                 (sentiment, value) = find_highest_number(current_sentiment)
#                 reply["sentiment"] = sentiment
  
#     return item.x



# @app.post("/analyze/aspect-based-sentiment")
# def generate(item: AspectItems):

#     aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='english', auto_device=True)

#     response = []
#     for comment in item.comments:
#         example_text = comment
#         inference_source = [example_text]
#         atepc_result = aspect_extractor.extract_aspect(inference_source=inference_source, pred_sentiment=True)


#         aspects = atepc_result[0].get('aspect')
#         sentiment = atepc_result[0].get('sentiment')
#         sentence = atepc_result[0].get('sentence')
#         mappedSentiment = {}

#         for i in range(len(sentiment)):
#             key = aspects[i]
#             value = sentiment[i]
#             mappedSentiment[key] = value
        
#         response.append({
#             "sentence": sentence,
#             "sentiment": mappedSentiment
#         })
#         print(atepc_result[0].get('aspect'))
  
#     return response