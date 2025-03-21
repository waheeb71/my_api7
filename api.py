from fastapi import FastAPI
import os  # ✅ إصلاح الخطأ بإضافة الاستيراد

app = FastAPI()

# مسار رئيسي يعيد رسالة ترحيبية
@app.get("/")
def home():
    return {"message": "مرحبًا بك في API الخاص بي!"}

# مسار يُرجع معلومات المستخدم
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Wahib", "age": 25}

# مسار لإضافة مستخدم جديد
@app.post("/user/")
def create_user(name: str, age: int):
    return {"message": f"تم إنشاء المستخدم {name} وعمره {age}"}

# مسار جديد لطباعة معلوماتك الشخصية
@app.get("/myinfo/")
def my_info():
    return {
        "message": "هذا هو API الخاص بي!",
        "my_info": {
            "name": "Wahib",
            "age": 25,
            "hobbies": ["البرمجة", "القراءة", "السباحة"]
        }
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))  # ✅ استخدم PORT من البيئة أو 8080 افتراضيًا
    uvicorn.run(app, host="0.0.0.0", port=port)
