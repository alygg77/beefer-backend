from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize the Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_user(email):
    data = {"email": email}
    response = supabase.table("users").insert(data).execute()
    return response.data

def create_beef(user_id, topic_name, topic_desc, nsfw=False, status="draft"):
    data = {
        "user_id": user_id,
        "nsfw": nsfw,
        "topic_name": topic_name,
        "topic_desc": topic_desc,
    }
    response = supabase.table("beefs").insert(data).execute()
    return response.data

def change_beef_status(beef_id, new_status):
    data = {"status": new_status}
    response = supabase.table("beefs").update(data).eq("id", beef_id).execute()
    return response.data

def fetch_beefs():
    response = supabase.table("beefs").select("*").execute()
    return response.data

def ban(user_id):
    data = {"is_banned": True}
    response = supabase.table("users").update(data).eq("id", user_id).execute()
    return response.data

def check_is_banned(user_id):
    response = supabase.table("users").select("is_banned").eq("id", user_id).execute()
    return response.data[0] if response.data else {"is_banned": None}

def add_penalty(user_id):
    user = supabase.table("users").select("penalties").eq("id", user_id).execute()
    if user.data:
        penalties = user.data[0].get("penalties", 0) + 1
        response = supabase.table("users").update({"penalties": penalties}).eq("id", user_id).execute()
        return response.data
    return {"error": "User not found"}

def check_penalties(user_id):
    response = supabase.table("users").select("penalties").eq("id", user_id).execute()
    return response.data[0] if response.data else {"penalties": None}

def user_metadata(user_id):
    response = supabase.table("users").select("email, alias, points, amount_debated, wins, penalties, is_banned").eq("id", user_id).execute()
    return response.data[0] if response.data else {"error": "User not found"}

response = create_beef(1, "test", False)
print(response)