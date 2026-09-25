def classify_email_content(subject: str, body: str):
    text = (subject + " " + body).lower()
    
    if any(w in text for w in ["viagra", "lottery", "crypto profit", "claim inheritance", "nigerian prince"]):
        return "SPAM", 0.99, "Junk_Spam"
    elif any(w in text for w in ["security alert", "password reset", "unauthorized login", "2fa"]):
        return "SECURITY", 0.96, "Security_Alerts"
    elif any(w in text for w in ["invoice", "receipt", "order confirmation", "payment received"]):
        return "TRANSACTIONAL", 0.94, "Receipts_Finance"
    elif any(w in text for w in ["50% off", "limited deal", "discount", "sale ends", "black friday"]):
        return "PROMOTIONAL", 0.91, "Promotions"
    elif any(w in text for w in ["help", "bug", "broken", "assistance", "support"]):
        return "SUPPORT", 0.92, "Customer_Support"
    else:
        return "INBOX", 0.85, "Inbox"
