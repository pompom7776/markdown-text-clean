import re

def clean_text(text):
    cleaned_text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    cleaned_text = re.sub(r'__(.*?)__', r'\1', cleaned_text)
    
    cleaned_text = re.sub(r'\*(.*?)\*', r'\1', cleaned_text)
    cleaned_text = re.sub(r'_(.*?)_', r'\1', cleaned_text)
    
    cleaned_text = re.sub(r'`(.*?)`', r'\1', cleaned_text)
    
    cleaned_text = re.sub(r'~~(.*?)~~', r'\1', cleaned_text)
    cleaned_text = re.sub(r'###',"", cleaned_text)
    cleaned_text = cleaned_text.replace(' - ', '・')

    
    return cleaned_text