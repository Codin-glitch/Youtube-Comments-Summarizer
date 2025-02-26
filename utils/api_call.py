import os
from dotenv import load_dotenv
import googleapiclient.discovery
import pandas as pd
import re

api_service_name = "youtube"
api_version = "v3"

load_dotenv()
DEVELOPER_KEY = os.getenv("API_KEY")

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY
)
# Function to get video details including title
def get_video_details(video_id):
    try:
        request = youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()

        if 'items' not in response or len(response['items']) == 0:
            return None, None  # No details found

        video_title = response['items'][0]['snippet']['title']
        video_published_at = response['items'][0]['snippet']['publishedAt']

        return video_title, video_published_at
    except Exception as e:
        print(f"An error occurred while fetching details for video {video_id}: {str(e)}")
        return None, None
    
# Function to get comments
def get_comments(video_id, video_title):
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100
        )

        comments = []
        response = request.execute()

        if 'items' not in response:
            print(f"No comments found for video {video_id}")
            return pd.DataFrame()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            public = item['snippet']['isPublic']
            text = comment['textOriginal']
            comments.append([
                comment['authorDisplayName'],
                comment['publishedAt'],
                comment['likeCount'],
                text,
                video_id,
                public,
                video_title
            ])

        while 'nextPageToken' in response:
            nextPageToken = response['nextPageToken']
            nextRequest = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=nextPageToken
            )
            response = nextRequest.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                public = item['snippet']['isPublic']
                text = comment['textOriginal']
                comments.append([
                    comment['authorDisplayName'],
                    comment['publishedAt'],
                    comment['likeCount'],
                    text,
                    video_id,
                    public,
                    video_title,
                ])

        df2 = pd.DataFrame(comments, columns=['author', 'updated_at', 'like_count', 'text', 'video_id', 'public', 'video_title'])
        return df2

    except Exception as e:
        print(f"An error occurred for video {video_id}: {str(e)}")
        return pd.DataFrame()