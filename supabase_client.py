from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv(".env")
# Initialize the Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_user(email):
    """
    Adds a new user to the 'users' table.
    :param email: Email address of the user
    """
    data = {"email": email}
    response = supabase.table("users").insert(data).execute()
    return response.data

def create_post(user_id, topic_name, topic_desc):
    """
    Adds a new post to the 'posts' table.
    :param user_id: ID of the user creating the post
    :param topic_name: Name of the topic
    :param topic_desc: Description of the topic
    """
    data = {"user_id": user_id, "topic_name": topic_name, "topic_desc": topic_desc}
    response = supabase.table("posts").insert(data).execute()
    return response.data

def change_status(post_id, new_status):
    """
    Changes the status of a post in the 'posts' table.
    :param post_id: ID of the post to be updated
    :param new_status: New status value
    """
    data = {"status": new_status}
    response = supabase.table("posts").update(data).eq("id", post_id).execute()
    return response.data

def create_beef(topic_id, user_id_1, user_id_2):
    """
    Adds a new row to the 'beefs' table.
    :param topic_id: ID of the topic associated with the beef
    :param user_id_1: ID of the first user in the beef
    :param user_id_2: ID of the second user in the beef
    """
    data = {"topic_id": topic_id, "user_id_1": user_id_1, "user_id_2": user_id_2}
    response = supabase.table("beefs").insert(data).execute()
    return response.data

def fetch_posts():
    """
    Fetches all rows from the 'posts' table.
    """
    response = supabase.table("posts").select("*").execute()
    return response.data

def fetch_beefs():
    """
    Fetches all rows from the 'beefs' table.
    """
    response = supabase.table("beefs").select("*").execute()
    return response.data

if __name__ == "__main__":
    # Example usage
    print("Supabase Client Loaded")
    change_status(1, "progress")