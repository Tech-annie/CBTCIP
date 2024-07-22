def create_receipt(customer_name, receipt_number, amount, date, items):
    receipt = []
    
    receipt.append("Payment Receipt")
    receipt.append("================")
    receipt.append("")
    
    receipt.append(f"Customer Name: {customer_name}")
    receipt.append(f"Receipt Number: {receipt_number}")
    receipt.append(f"Amount: ${amount:.2f}")
    receipt.append(f"Date: {date}")
    receipt.append("")
    
    receipt.append("Items:")
    for item in items:
        receipt.append(f"- {item}")
    
    receipt.append("")
    receipt.append("Thank you for your purchase!")
    
    return "\n".join(receipt)

# Example usage
customer_name = "John Doe"
receipt_number = "123456"
amount = 250.75
date = "2024-07-22"
items = ["Rice", "Sugar", "Chocolates"]

receipt_output = create_receipt(customer_name, receipt_number, amount, date, items)
print(receipt_output)