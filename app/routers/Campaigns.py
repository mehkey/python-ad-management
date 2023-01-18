from fastapi import FastAPI, HTTPException
from fastapi import APIRouter, Depends
from pydantic import BaseModel
import psycopg2

router = APIRouter(
    tags=['Matches'],
    responses={404: {'description': 'Not Found'}}
)

#app = FastAPI()

def get_database_connection():
    # Get the environment from the environment variables
    env = "dev" #os.environ.get("ENV", "dev")
    if env == "dev":
        # Development environment
        return psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="password"
        )
    elif env == "qa":
        # Staging environment
        return psycopg2.connect(
            host="staging.example.com",
            database="mydatabase_qa",
            user="myuser",
            password="mypassword"
        )
    elif env == "prod":
        # Production environment
        return psycopg2.connect(
            host="prod.example.com",
            database="mydatabase_prod",
            user="myuser",
            password="mypassword"
        )
    else:
        raise ValueError("Invalid environment")

'''
# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
'''

def create_table_if_not_exists(conn, table_name):
    cursor = conn.cursor()
    # Check if the table exists
    cursor.execute(f"SELECT to_regclass('{table_name}')")
    if cursor.fetchone()[0] is None:
        # The table does not exist, so create it
        cursor.execute(f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, name TEXT, goal TEXT, budget REAL)")
    # Close the cursor and connection
    cursor.close()
    conn.commit()

# Connect to the database
conn = get_database_connection()

# Create the table if it does not exist
create_table_if_not_exists(conn, "campaigns")

# Close the connection
conn.close()

# Create a cursor
#cur = conn.cursor()

class Campaign(BaseModel):
    name: str
    goal: str
    budget: float

@router.post("/campaigns", status_code=201)
def create_campaign(campaign: Campaign):
    # Insert the campaign into the database
    conn = get_database_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO campaigns (name, goal, budget) VALUES (%s, %s, %s)",
        (campaign.name, campaign.goal, campaign.budget)
    )
    # Commit the changes to the database
    conn.commit()
    # Return the campaign ID
    return {"id": cur.lastrowid}