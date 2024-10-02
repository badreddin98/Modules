def mood_response(mood):
    
    mood = mood.lower()
    responses = {
         "happy": "I'm glad to hear that you're feeling happy!",
         "sad": "I'm sorry you're feeling down.",
         "angry": "Take a deep breath.",
         "tired": "You deserve a break. Make sure to rest and recharge.",
         "bored": "Why not try something new? Maybe a hobby or a quick exercise!"       
    }
    
    return responses.get(mood, "I'm not sure how to respond to that mood, but I hope you feel better soon!")