from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -------------------------------------
# Mock In-Memory "Database"
# -------------------------------------
users = [
    {"name": "Ali", "pin": "1111", "bank_balance": 500},
    {"name": "Ahmad", "pin": "2222", "bank_balance": 300}
]


# -------------------------------------
# Request Models
# -------------------------------------
class AuthRequest(BaseModel):
    name: str
    pin_number: str


class DepositRequest(BaseModel):
    name: str
    amount: float


class TransferRequest(BaseModel):
    sender_name: str
    receipents_name: str
    amount: float


# -------------------------------------
# /authenticate
# -------------------------------------
@app.post("/authenticate")
def authenticate(data: AuthRequest):
    user = next((u for u in users if u["name"] == data.name and u["pin"] == data.pin_number), None)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid name or PIN")

    return {
        "message": "Authentication successful",
        "account": {
            "name": user["name"],
            "bank_balance": user["bank_balance"]
        }
    }


# -------------------------------------
# /deposit
# -------------------------------------
@app.post("/deposit")
def deposit(data: DepositRequest):
    user = next((u for u in users if u["name"] == data.name), None)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid deposit amount")

    user["bank_balance"] += data.amount

    return {
        "message": "Deposit successful",
        "new_balance": user["bank_balance"]
    }


# -------------------------------------
# /bank-transfer
# -------------------------------------


class TransferRequest(BaseModel):
    sender_name: str
    recipient_name: str   # <-- FIXED
    amount: float


@app.post("/bank-transfer")
def bank_transfer(data: TransferRequest):
    sender = next((u for u in users if u["name"] == data.sender_name), None)
    receiver = next((u for u in users if u["name"] == data.recipient_name), None)

    if not sender or not receiver:
        raise HTTPException(status_code=404, detail="Sender or receiver not found")

    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid transfer amount")

    if sender["bank_balance"] < data.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    # Deduct & Add
    sender["bank_balance"] -= data.amount
    receiver["bank_balance"] += data.amount

    return {
        "message": "Transfer successful",
        "sender_new_balance": sender["bank_balance"],
        "receiver_new_balance": receiver["bank_balance"]
    }

    
# /balance  
# -------------------------------------
@app.get("/balance")
def get_balance(name: str):
    user = next((u for u in users if u["name"] == name), None)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "name": user["name"],
        "current_balance": user["bank_balance"]
    }