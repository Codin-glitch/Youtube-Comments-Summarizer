from flask import Flask, request, jsonify, render_template
from pytube import extract
from utils.api_call import get_comments, get_video_details
from utils.preprocessing import clean_comments, remove_repetitive_sentences
from utils.model_load import *
import pandas as pd

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summary',methods=['POST'])
def summary():
    video_url = request.form['videoUrl']
    video_id=extract.video_id(video_url)
    # Initialize an empty DataFrame to store all comments
    df = pd.DataFrame()

    print(f"Fetching details for video: {video_id}")
    video_title, video_published_at = get_video_details(video_id)

    if video_title:
        print(f"Fetching comments for video: {video_id} (Title: {video_title})")
        df2 = get_comments(video_id, video_title)
        if not df2.empty:
            df = pd.concat([df, df2], ignore_index=True)
        else:
            print(f"No comments found for video {video_id}")
    else:
        print(f"No details found for video {video_id}")

    # Save the DataFrame with comments, titles, and labels to a CSV file
    output_file = f'youtube_comments_{video_id}.csv'
    df.to_csv(output_file, index=False)

    print(f"Data exported to {output_file}")

    result = clean_comments(df)
    summary = summarize_large_text(result)
    summary = remove_repetitive_sentences(summary)


    return render_template('index.html', url = video_title, summary = summary)


if __name__ == '__main__':
    app.run(debug=True)
