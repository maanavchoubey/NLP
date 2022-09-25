def text_processing(clean_text, whitespace=False, punctuation=False,lower_case=False,remove_number=False,
                   stop_words=False, lemmatize = False, find_mail= False, vocab_correction=False,
                   new_line_remove = False, find_url=False, extra_space=False, remove_emoji=False, remove_mail=False,
                   remove_url=False, non_ascii_removal = False):
    dictionary = {}
    
    if whitespace == True:                                     #REMOVES ALL WHITE SPACES.
        whitespace = string.whitespace
        tableWhitespace = str.maketrans('','',whitespace)
        clean_text = clean_text.translate(tableWhitespace)
    
    
    if punctuation == True:                                    #REMOVES DEFINED PUNCTUATIONS.
        punctuation = "!#$%&\'()*+:;<=>?[\\]^`{|}~ÛÏ¥©"
        tablePunctuation = str.maketrans('','',punctuation)
        clean_text = clean_text.translate(tablePunctuation)
    
    if lower_case == True:                                     #LOWER CASES THE WHOLE TEXT.
        clean_text = clean_text.lower()
    
    if remove_number == True:                                  #REMOVES ALL NUMBERS FROM OUR TEXT.
        clean_text = re.sub(r'\d+', '', clean_text)
        
    if stop_words == True:                                     
        clean_text = " ".join([word for word in str(clean_text).split() if word not in stopwords])
    
    if lemmatize == True:                                      #CONVERT WORDS TO THEIR ROOTS.
        doc = nlp(clean_text)
        clean_text = " ".join([token.lemma_ for token in doc])
    
    if find_mail == True:                                      #FETCHES ALL MAIL ID FROM OUR TEXT.
        doc = nlp(text)
        for token in doc:
            if token.like_email:
                mail = token.text
        dictionary['mail'] = mail
    
    if vocab_correction == True:                               #CORRECTS GRAMMATICAL ERROR.
        words = word_tokenize(text)
        xyz = []
        string = ""
        for i in range(0,len(words)):
            xyz.append(suggest(words[i]))
            string = string+xyz[i][0][0]+" "
        clean_text = string
    
    if new_line_remove == True:                                #REMOVES ALL NEW LINES
        clean_text = clean_text.replace('\n','')
        
    if find_url == True:                                       #EXTRACTS ALL URL's STARTING WITH WWW,HTTPS AND HTTP.
        url = re.findall(r'https?://\S+|www\.\S+',clean_text)
        dictionary['url'] = url
    
    if extra_space == True:                                    #REMOVES MORE THAN ONE WHITE SPACE CHARACTER.
        clean_text = re.sub(r' +',' ',clean_text)
        
    if remove_emoji == True:                                   #ALL EMOJIS ARE REMOVED
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
        clean_text = emoji_pattern.sub(r'', string)
    
    if remove_url == True:
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        clean_text = url_pattern.sub(r'', clean_text)
    
    if remove_mail == True:
        mail_pattern = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
        clean_text = mail_pattern.sub(r'',clean_text)
    
    if non_ascii_removal == True:
        string_with_nonASCII = clean_text
        encoded_string = string_with_nonASCII.encode("ascii", "ignore")
        clean_text = encoded_string.decode()
    
    
    dictionary['clean_text'] = clean_text
    return dictionary