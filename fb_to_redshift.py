#!/usr/bin/python
# -*- coding: utf-8 -*-
from fb_tools import create_import_file, upload_to_s3, update_redshift

posts = {}
posts['interval'] = 'month'
posts['import_type'] = 'posts'
posts['filename'] = 'fb_import_posts_Test.csv'
posts['tablename'] = 'facebook.posts_test'
posts['columns'] = ['post_id', 'message', 'created_time', 'likes', 'shares', 'comments', 'total_reach']
posts['primary_key'] = 'post_id'

videos = {}
videos['interval'] = False
videos['import_type'] = 'videos'
videos['filename'] = 'fb_import_videos_test.csv'
videos['tablename'] = 'facebook.videos_test'
videos['columns'] = ['video_id', 'title', 'description', 'created_time', 'video_length', 'likes', 'comments', 'reactions', 'shares', 'reach', 'ms_viewed ', 'total_views', 'unique_viewers', 'views_10sec', 'views_30sec', 'views_95pct', 'avg_completion']
videos['primary_key'] = 'video_id'

video_lab_videos = {}
video_lab_videos['interval'] = False
video_lab_videos['import_type'] = 'video_lab_videos'
video_lab_videos['filename'] = 'fb_import_video_lab_test.csv'
video_lab_videos['tablename'] = 'facebook.video_lab_videos_test'
video_lab_videos['columns'] = ['video_id', 'title', 'description', 'created_time', 'video_length', 'likes', 'comments', 'reactions', 'shares', 'reach', 'ms_viewed ', 'total_views', 'unique_viewers', 'views_10sec', 'views_30sec', 'views_95pct', 'avg_completion']
video_lab_videos['primary_key'] = 'video_id'
video_lab_videos['list_id'] = '1563848167245359'

video_lab_videos_2 = {}
video_lab_videos_2['interval'] = False
video_lab_videos_2['import_type'] = 'video_lab_videos'
video_lab_videos_2['filename'] = 'fb_import_video_lab_2_test.csv'
video_lab_videos_2['tablename'] = 'facebook.video_lab_videos_test'
video_lab_videos_2['columns'] = ['video_id', 'title', 'description', 'created_time', 'video_length', 'likes', 'comments', 'reactions', 'shares', 'reach', 'ms_viewed ', 'total_views', 'unique_viewers', 'views_10sec', 'views_30sec', 'views_95pct', 'avg_completion']
video_lab_videos_2['primary_key'] = 'video_id'
video_lab_videos_2['list_id'] = '1225720367451359'

data_types = [posts, videos, video_lab_videos, video_lab_videos_2]

for item in data_types:
    if 'list_id' in item:
        create_import_file(item.get('interval'), item.get('import_type'), item.get('filename'), item.get('list_id'))
    else:
        create_import_file(item.get('interval'), item.get('import_type'), item.get('filename'))
    print("created " + item.get('filename')) 
    
    upload_to_s3(item.get('filename'))
    print("uploaded " + item.get('filename') + " to s3")
    
    update_redshift(item.get('tablename'), item.get('columns'), item.get('primary_key'), item.get('filename'))
    print("updated redshift table " + item.get('tablename'))