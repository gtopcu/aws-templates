
# curl "http://localhost:5000/greeting?name=John"
# curl -X POST -H "Content-Type: application/json" -d '{"email":"john@example.com"}' http://localhost:5000/customer/john
# curl -X PUT -H "Content-Type: application/json" -d '{"email":"john.updated@example.com"}' http://localhost:5000/customer/john

from flask import Flask, request, jsonify, redirect, url_for, abort
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

# In-memory storage for demonstration
customers = {}

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request", "message": str(error)}), 400

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# accepts query parameter "name"
@app.route('/greeting', methods=['GET'])
def get_greeting():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({"message": "Hello, stranger!"})
        return jsonify({"message": f"Hello, {name}!"})
    except Exception as e:
        app.logger.error(f"Error in get_greeting: {str(e)}")
        return jsonify({"error": "Failed to process request"}), 500

@app.route('/customer/<customer>', methods=['PUT'])
def update_customer(customer):
    try:
        if not request.is_json:
            raise BadRequest("Content-Type must be application/json")
        
        data = request.get_json()
        if not data:
            raise BadRequest("No data provided")
        
        # Update customer data
        customers[customer] = data
        
        # Redirect to a GET endpoint to see the updated customer
        if request.headers.get('Accept') == 'text/html':
            return redirect(url_for('get_greeting', name=customer))
            
        return jsonify({
            "message": "Customer updated successfully",
            "customer": customer,
            "data": data
        }), 200
    
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Error in update_customer: {str(e)}")
        return jsonify({"error": "Failed to update customer"}), 500

@app.route('/customer/<customer>', methods=['POST'])
def create_customer(customer):
    try:
        if not request.is_json:
            raise BadRequest("Content-Type must be application/json")
        
        if customer in customers:
            abort(409, description="Customer already exists")
            
        data = request.get_json()
        if not data:
            raise BadRequest("No data provided")
        
        # Create new customer
        customers[customer] = data
        
        return jsonify({
            "message": "Customer created successfully",
            "customer": customer,
            "data": data
        }), 201
        
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Error in create_customer: {str(e)}")
        return jsonify({"error": "Failed to create customer"}), 500

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True, load_dotenv = True,)