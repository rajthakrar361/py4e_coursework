# Example 2, nested list -
import json
data = {
    "id": "a4302189d72f48bca605b4c173e69f16",
    "pdfs": [
        "{\"all_emails\": [\"test@test.com\"], \"all_indian_phone_numbers\": [], \"invoice_sender\": [\"DEMO - Sliced Invoices\"], \"invoice_reciever\": [\"Test Business\"], \"invoice_number\": [\"3337\"], \"invoice_order_number\": [\"12345\"], \"invoice_date\": [\"January 25, 2016\"], \"invoice_duedate\": [\"January 31, 2016\"], \"invoice_total\": [\"Total Due $93.50\", \"Total $93.50\"], \"invoice_subtotal\": [], \"invoice_sales_tax\": [\"Tax $8.50\"], \"invoice_bill_to\": []}"
    ]
}
# creating a list of dict named info.
info = json.dumps(data, indent = 4)
print('User Count: ', len(info))
# iterating through the list info. each item is a dictionary
data1 = data["pdfs"][0]

info1 = json.dumps(data1, indent = 4)
print(info1)
