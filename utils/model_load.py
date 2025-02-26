import torch
import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from accelerate import Accelerator

# Initialize Accelerator
accelerator = Accelerator()

# Load model and tokenizer
model_checkpoint = r"D:\Projects\Summarizer\fine_tuned_t5_review"  # Update with your model path
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
model = torch.compile(model)


start = time.time()
# Move model to accelerator
model = accelerator.prepare(model)


# Function to split text using a sliding window
def sliding_window_split(text, window_size=450, overlap=150):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + window_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += (window_size - overlap)  # Move window forward with overlap

    return chunks

# Summarization function
def summarize_large_text(text, window_size=450, overlap=150, batch_size=4):
    start = time.time()
    chunks = sliding_window_split(text, window_size, overlap)
    summaries = []
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        inputs = tokenizer(batch, return_tensors="pt", truncation=True, padding=True)
        inputs = accelerator.prepare(inputs)
        inputs = {k: v.to(accelerator.device) for k, v in inputs.items()}
        
        with torch.no_grad():
            output_ids = model.generate(
                **inputs, 
                max_length=150, 
                num_beams=5, 
                repetition_penalty=2.0,
                no_repeat_ngram_size=3
            )
        
        summaries.extend(tokenizer.batch_decode(output_ids, skip_special_tokens=True))
    
    final_summary = " ".join(summaries)
    


    # Optional: Summarize again for a more concise version
    final_inputs = tokenizer(f"Summarize: {final_summary}", return_tensors="pt", truncation=True, padding=True)
    final_inputs = {k: v.to(accelerator.device) for k, v in final_inputs.items()}

    with torch.no_grad():
        output_ids = model.generate(
            **final_inputs, 
            max_length=150, 
            num_beams=5, 
            repetition_penalty=2.0
        )
    compressed_summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    end = time.time()
    total = end - start
    print("Time taken: ",total)

    return compressed_summary

# Example usage
large_text =  """ actually coming from the c++ and js bg .... it took me a week concidering i was only giving 1.5 hrs a day to complete this and grasp the concepts ... the way u teach .. IT actually made me feel that i everthing is doable if u have a right mentor by ur side .. and here i got one MR navin my java mentor .... ALot of respect and appreciation from myside .. count me in ur student from pakistan
IDK why  If simply writing class doesn't work, use public class  Class till Variable ---> 48:11  Type casting --> 1:16:08 Hello sir when I am trying to do the code i.e javac --version in vs code I am getting trouble like name is mistake I don't know if anyone noticed, but at 4:48:41 an unintentional error appeared (probably because the description: "Immutable string" was underlined).
 I guess you meant to say that: both StringBuffer and StringBuilder provide the way to build a mutable strings Finally I have Successfully finished this course The best java course available on the internet Gained more knowledge missed method reference concept i think I am just 14 and I have been doing c and now I am doing java I am understanding this very easily thank u sir for making this Great Video so far but static method part has something missing .Please check and update .
Appreciate the good work navin Thank you for sharing your knowledge with us!
Your explanations are truly remarkable. Throughout my programming career, there have been concepts
I never fully understood, yet I managed to write a lot of code. However, this course has made those concepts much clearer and easier to understand.
Your effort is greatly appreciated! I loved that John Cena part ...by the way very well explained, my mind is in sync with yours.
I mean the moment question appears in my mind you instantly say that and boom it is cleared. Sir please kindly speak slower
Thank you sir i got to understand completely about the java programming language by watching your video before this i had a no knowledge about java...
I salute for your work  Congrats Navin! Straight to the point, no non necessary info, by far the best Java tutorial I have seen! Your explanation is very simple and easy understandable. You are a good teacher  Naveen, sir, I salute you. The explanation is really good and I understand half of the things you teach in this course. This is my first time learning Java, with some small experience in front-end skills.
Thank you, sir. Hello world ,I have completed half of this course and really gained confidence, if any one have learned java and also learning other technologies such as web or freelancing or using java in there startup or etc please consider me your junior,and guide me what should I learn or do after completing this course  if i want to call myself and computer science engineer and do Little earning side by side of college or any guidance you can as a senior will be really helpful
3:35:41 In Heap and stack section you said that Every method has its own stack but it is not true; the true statement is that each thread has its own stack and every method share this stack as making separate frames in that stack. super is John Cena , really great course, well organized and step by step explained, simple to understand  The course is very structured, step by step, simple to understand, and I like how you delve into specific use cases which lets us explore the topic in detail.
Great course! Big thanks to Navin Reddy for his amazing tutorials!

"""
final_summary = summarize_large_text(large_text)

#print("Final Summary:", final_summary)

end = time.time()
total = end - start
print("Time taken: ",total)
