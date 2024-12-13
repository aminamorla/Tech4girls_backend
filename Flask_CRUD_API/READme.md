### How to test the API using Postman

# Flask Laptop API
This API allows you to manage a collection of laptops. You can add, update, retrieve, and delete laptops.

1. **Start the Flask Application**
- Open a terminal, navigate to the directory where your 'app.py' is located, and run:
- The app will run on http://localhost:5000.

2. *Test the API Endpoints Using Postman*  
   - Open Postman.
   - For each of the endpoints listed above, set the correct HTTP method (GET, POST, PUT, DELETE) and provide the corresponding URL and JSON body (if required).

   Example for adding a laptop:
   - Set method to POST.
   - Set URL to http://localhost:5000/laptops/add.
   - In the Body tab, choose raw and JSON format, then paste the sample request body:
     json
     {
       "name": "Dell XPS 13",
       "laptop_number": "12345",
       "specifications": "Intel i7, 16GB RAM, 512GB SSD"
     }
     

3. *Verify the Responses*  
   - After sending the request, verify the expected response in the Postman output. Ensure that the status code matches the expected one, and that the response body contains the correct data.

---

With these files and instructions, you can now implement, test, and use the Flask API for managing laptops using Postman.

