

# Stripe -> EventBridge / local webhooks



"""
Step 1: Set Up a Stripe Account and Install the Library
Sign up for a Stripe account at https://stripe.com if you don't already have one
Get your API keys from the Stripe Dashboard
Install the Stripe Python library:
pip install stripe

Step 2: Set Up the Basic Configuration
import stripe

# Replace with your Stripe API key
stripe.api_key = "sk_test_your_test_key"

Step 3: Implement the Core Payment Functionality
Let's create a simple Flask application to handle payments:

from flask import Flask, request, jsonify, render_template, redirect, url_for
import stripe
import os

app = Flask(__name__)

# Replace with your Stripe API keys
stripe.api_key = "sk_test_your_test_key"
webhook_secret = "whsec_your_webhook_secret"

# Product/price information
PRICE_ID = "price_your_price_id"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': PRICE_ID,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.host_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.host_url + 'cancel',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/success')
def success():
    session_id = request.args.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    customer = stripe.Customer.retrieve(session.customer)
    
    # Here you would typically update your database, send confirmation emails, etc.
    
    return render_template('success.html', customer=customer)

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return 'Invalid signature', 400

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Fulfill the purchase...
        handle_checkout_completed(session)

    return 'Success', 200

def handle_checkout_completed(session):
    # Fulfill the purchase...
    # For example, update a user's membership status in your database
    print(f"Payment for session {session.id} was successful!")
    # Update your database, send confirmation emails, etc.

# Payment Intents API - useful for custom payment flows
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        data = request.get_json()
        amount = data.get('amount', 1000)  # Default amount is 1000 (10 USD)
        
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
            metadata={'integration_check': 'accept_a_payment'},
        )
        return jsonify({
            'clientSecret': intent.client_secret
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

# Subscription example
@app.route('/create-subscription', methods=['POST'])
def create_subscription():
    try:
        data = request.get_json()
        customer_id = data.get('customer_id')
        price_id = data.get('price_id')
        
        # Create the subscription
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'price': price_id,
                },
            ],
            payment_behavior='default_incomplete',
            expand=['latest_invoice.payment_intent'],
        )
        
        return jsonify({
            'subscriptionId': subscription.id,
            'clientSecret': subscription.latest_invoice.payment_intent.client_secret,
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(port=4242, debug=True)

#Step 4: Create the HTML Templates
Let's create the necessary HTML templates for our Flask app:index.html

<!DOCTYPE html>
<html>
<head>
    <title>Stripe Payment Example</title>
    <script src="https://js.stripe.com/v3/"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        .container {
            width: 400px;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        button {
            background-color: #635BFF;
            color: white;
            border: none;
            padding: 10px 15px;
            width: 100%;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #524ee0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Stripe Payment Example</h1>
        <p>Click the button below to pay with Stripe:</p>
        <button id="checkout-button">Checkout</button>
    </div>

    <script>
        var stripe = Stripe('pk_test_your_publishable_key');
        var checkoutButton = document.getElementById('checkout-button');

        checkoutButton.addEventListener('click', function() {
            // Create a checkout session when the button is clicked
            fetch('/create-checkout-session', {
                method: 'POST',
            })
            .then(function(response) {
                return response.json();
            })
            .then(function(session) {
                return stripe.redirectToCheckout({ sessionId: session.id });
            })
            .then(function(result) {
                if (result.error) {
                    alert(result.error.message);
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>


success.html
<!DOCTYPE html>
<html>
<head>
    <title>Payment Success</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        .container {
            width: 400px;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #32CD32;
        }
        p {
            margin: 20px 0;
        }
        a {
            color: #635BFF;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Payment Successful!</h1>
        <p>Thank you for your purchase.</p>
        <p>Your transaction has been completed successfully.</p>
        {% if customer %}
            <p>Customer ID: {{ customer.id }}</p>
            <p>Email: {{ customer.email }}</p>
        {% endif %}
        <p><a href="/">Return to Home</a></p>
    </div>
</body>
</html>


cancel.html
<!DOCTYPE html>
<html>
<head>
    <title>Payment Cancelled</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        .container {
            width: 400px;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #FF6347;
        }
        p {
            margin: 20px 0;
        }
        a {
            color: #635BFF;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Payment Cancelled</h1>
        <p>Your payment was cancelled.</p>
        <p><a href="/">Return to Home</a></p>
    </div>
</body>
</html>


Step 5: Advanced Integration - Customer Management
Here's how to implement customer management:

import stripe

# Replace with your Stripe API key
stripe.api_key = "sk_test_your_test_key"

def create_customer(email, name=None, description=None):
    ""Create a new customer in Stripe""
    try:
        customer = stripe.Customer.create(
            email=email,
            name=name,
            description=description
        )
        print(f"Created customer with ID: {customer.id}")
        return customer
    except stripe.error.StripeError as e:
        print(f"Error creating customer: {e}")
        return None

def retrieve_customer(customer_id):
    ""Retrieve a customer from Stripe by ID""
    try:
        customer = stripe.Customer.retrieve(customer_id)
        return customer
    except stripe.error.StripeError as e:
        print(f"Error retrieving customer: {e}")
        return None

def update_customer(customer_id, **kwargs):
    ""Update a customer in Stripe""
    try:
        customer = stripe.Customer.modify(
            customer_id,
            **kwargs
        )
        print(f"Updated customer: {customer.id}")
        return customer
    except stripe.error.StripeError as e:
        print(f"Error updating customer: {e}")
        return None

def delete_customer(customer_id):
    ""Delete a customer from Stripe""
    try:
        deletion = stripe.Customer.delete(customer_id)
        print(f"Deleted customer: {customer_id}")
        return deletion
    except stripe.error.StripeError as e:
        print(f"Error deleting customer: {e}")
        return None

def list_customers(limit=10, email=None):
    ""List customers in Stripe""
    try:
        params = {
            "limit": limit
        }
        if email:
            params["email"] = email
            
        customers = stripe.Customer.list(**params)
        return customers
    except stripe.error.StripeError as e:
        print(f"Error listing customers: {e}")
        return None

def add_payment_method_to_customer(customer_id, payment_method_id, set_as_default=True):
    ""Attach a payment method to a customer""
    try:
        payment_method = stripe.PaymentMethod.attach(
            payment_method_id,
            customer=customer_id
        )
        
        if set_as_default:
            stripe.Customer.modify(
                customer_id,
                invoice_settings={"default_payment_method": payment_method_id}
            )
            
        print(f"Added payment method {payment_method_id} to customer {customer_id}")
        return payment_method
    except stripe.error.StripeError as e:
        print(f"Error adding payment method: {e}")
        return None

def get_payment_methods(customer_id, type="card"):
    ""List all payment methods for a customer""
    try:
        payment_methods = stripe.PaymentMethod.list(
            customer=customer_id,
            type=type
        )
        return payment_methods
    except stripe.error.StripeError as e:
        print(f"Error getting payment methods: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a customer
    customer = create_customer(
        email="customer@example.com",
        name="John Doe",
        description="Test customer"
    )
    
    if customer:
        customer_id = customer.id
        
        # Update the customer
        updated_customer = update_customer(
            customer_id,
            name="John Smith",
            metadata={"user_id": "123456"}
        )
        
        # Retrieve customer
        retrieved_customer = retrieve_customer(customer_id)
        if retrieved_customer:
            print(f"Customer name: {retrieved_customer.name}")
            print(f"Customer email: {retrieved_customer.email}")
            
        # List customers
        customers = list_customers(limit=5)
        if customers:
            print(f"Found {len(customers.data)} customers")
            
        # Clean up - delete the customer
        # Note: In production, you typically wouldn't delete customers
        # delete_customer(customer_id)


        
Step 6: Implementing Subscriptions

import stripe
from datetime import datetime

# Replace with your Stripe API key
stripe.api_key = "sk_test_your_test_key"

def create_product(name, description=None):
    ""Create a new product in Stripe""
    try:
        product = stripe.Product.create(
            name=name,
            description=description
        )
        print(f"Created product with ID: {product.id}")
        return product
    except stripe.error.StripeError as e:
        print(f"Error creating product: {e}")
        return None
        
def create_price(product_id, unit_amount, currency="usd", recurring=None):
    ""
    Create a new price for a product
    
    recurring example: {"interval": "month"}
    ""
    try:
        price_data = {
            "product": product_id,
            "unit_amount": unit_amount,  # in cents
            "currency": currency,
        }
        
        if recurring:
            price_data["recurring"] = recurring
            
        price = stripe.Price.create(**price_data)
        print(f"Created price with ID: {price.id}")
        return price
    except stripe.error.StripeError as e:
        print(f"Error creating price: {e}")
        return None

def create_subscription(customer_id, price_id, trial_days=None):
    ""Create a new subscription for a customer""
    try:
        subscription_data = {
            "customer": customer_id,
            "items": [
                {"price": price_id},
            ],
        }
        
        if trial_days:
            subscription_data["trial_period_days"] = trial_days
            
        subscription = stripe.Subscription.create(**subscription_data)
        print(f"Created subscription with ID: {subscription.id}")
        return subscription
    except stripe.error.StripeError as e:
        print(f"Error creating subscription: {e}")
        return None

def retrieve_subscription(subscription_id):
    ""Retrieve a subscription from Stripe by ID""
    try:
        subscription = stripe.Subscription.retrieve(subscription_id)
        return subscription
    except stripe.error.StripeError as e:
        print(f"Error retrieving subscription: {e}")
        return None

def cancel_subscription(subscription_id, at_period_end=True):
    ""
    Cancel a subscription
    
    at_period_end: If true, will cancel at the end of the current billing period
    ""
    try:
        subscription = stripe.Subscription.modify(
            subscription_id,
            cancel_at_period_end=at_period_end
        )
        print(f"Subscription {subscription_id} will be cancelled {'at period end' if at_period_end else 'immediately'}")
        return subscription
    except stripe.error.StripeError as e:
        print(f"Error cancelling subscription: {e}")
        return None

def update_subscription_items(subscription_id, items):
    ""
    Update subscription items
    
    items example: [
        {
            "id": "si_existing_item",
            "price": "price_new_price"
        }
    ]
    ""
    try:
        subscription = stripe.Subscription.modify(
            subscription_id,
            items=items
        )
        print(f"Updated subscription items for {subscription_id}")
        return subscription
    except stripe.error.StripeError as e:
        print(f"Error updating subscription items: {e}")
        return None

def list_subscriptions(customer_id=None, limit=10, status=None):
    ""List subscriptions in Stripe""
    try:
        params = {"limit": limit}
        
        if customer_id:
            params["customer"] = customer_id
            
        if status:
            params["status"] = status
            
        subscriptions = stripe.Subscription.list(**params)
        return subscriptions
    except stripe.error.StripeError as e:
        print(f"Error listing subscriptions: {e}")
        return None

def create_subscription_checkout_session(price_id, success_url, cancel_url, customer_email=None, customer_id=None):
    ""Create a Checkout Session for subscription payments""
    try:
        session_data = {
            "payment_method_types": ["card"],
            "line_items": [
                {
                    "price": price_id,
                    "quantity": 1,
                },
            ],
            "mode": "subscription",
            "success_url": success_url,
            "cancel_url": cancel_url,
        }
        
        if customer_id:
            session_data["customer"] = customer_id
        elif customer_email:
            session_data["customer_email"] = customer_email
            
        checkout_session = stripe.checkout.Session.create(**session_data)
        return checkout_session
    except stripe.error.StripeError as e:
        print(f"Error creating checkout session: {e}")
        return None

def format_subscription_details(subscription):
    ""Format subscription details in a human-readable way""
    if not subscription:
        return None
        
    current_period_start = datetime.fromtimestamp(subscription.current_period_start)
    current_period_end = datetime.fromtimestamp(subscription.current_period_end)
    
    details = {
        "id": subscription.id,
        "status": subscription.status,
        "current_period": {
            "start": current_period_start.strftime("%Y-%m-%d %H:%M:%S"),
            "end": current_period_end.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "cancel_at_period_end": subscription.cancel_at_period_end,
        "items": []
    }
    
    for item in subscription.items.data:
        details["items"].append({
            "id": item.id,
            "price_id": item.price.id,
            "product_id": item.price.product,
            "unit_amount": item.price.unit_amount / 100,  # convert from cents
            "currency": item.price.currency,
            "interval": item.price.recurring.interval if hasattr(item.price, 'recurring') else None,
            "interval_count": item.price.recurring.interval_count if hasattr(item.price, 'recurring') else None,
        })
        
    return details

# Example usage
if __name__ == "__main__":
    # Create a product
    product = create_product(
        name="Premium Plan",
        description="Monthly subscription for premium features"
    )
    
    if product:
        # Create a price for the product (monthly subscription)
        price = create_price(
            product_id=product.id,
            unit_amount=1999,  # $19.99
            currency="usd",
            recurring={"interval": "month"}
        )
        
        # Create a customer
        customer = stripe.Customer.create(
            email="subscriber@example.com",
            name="Jane Smith"
        )
        
        if price and customer:
            # Create a subscription with a 14-day trial
            subscription = create_subscription(
                customer_id=customer.id,
                price_id=price.id,
                trial_days=14
            )
            
            if subscription:
                # Retrieve and format subscription details
                details = format_subscription_details(subscription)
                print(details)
                
                # Example: Cancel the subscription at the end of the period
                # cancel_subscription(subscription.id, at_period_end=True)


Step 7 - Error Handling

import stripe
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('stripe_utils')

class StripeErrorHandler:
    @staticmethod
    def handle_error(error, operation="Stripe operation"):
        ""
        Handle different types of Stripe errors and provide appropriate responses
        
        Args:
            error: A stripe.error.StripeError instance
            operation: Description of the operation being performed
            
        Returns:
            dict: A dictionary with error details
        ""
        error_data = {
            "success": False,
            "operation": operation,
            "error_type": type(error).__name__,
            "error_message": str(error),
            "code": None,
            "param": None,
            "status_code": None,
        }
        
        # Log the error with appropriate severity
        if isinstance(error, stripe.error.CardError):
            # Card errors are common and expected, log as INFO
            logger.info(f"Card error during {operation}: {error}")
            error_data["code"] = error.code
            error_data["param"] = error.param
            error_data["decline_code"] = getattr(error, 'decline_code', None)
            error_data["status_code"] = error.http_status
            error_data["user_message"] = "Your card was declined. Please check your card details and try again."
            
        elif isinstance(error, stripe.error.RateLimitError):
            # Rate limit errors indicate we're making too many requests
            logger.warning(f"Rate limit error during {operation}: {error}")
            error_data["status_code"] = error.http_status
            error_data["user_message"] = "Our payment system is experiencing high volume. Please try again in a few moments."
            
        elif isinstance(error, stripe.error.InvalidRequestError):
            # Invalid request errors are likely due to developer error
            logger.error(f"Invalid request error during {operation}: {error}")
            error_data["param"] = error.param
            error_data["status_code"] = error.http_status
            error_data["user_message"] = "There was a problem with your request. Please contact support."
            
        elif isinstance(error, stripe.error.AuthenticationError):
            # Authentication errors indicate API key issues
            logger.critical(f"Authentication error during {operation}: {error}")
            error_data["status_code"] = error.http_status
            error_data["user_message"] = "Payment system authentication failed. Please contact support immediately."
            
        elif isinstance(error, stripe.error.APIConnectionError):
            # API connection errors indicate network issues
            logger.error(f"API connection error during {operation}: {error}")
            error_data["user_message"] = "We're having trouble connecting to our payment provider. Please try again."
            
        elif isinstance(error, stripe.error.StripeError):
            # Generic Stripe errors
            logger.error(f"Stripe error during {operation}: {error}")
            error_data["status_code"] = getattr(error, 'http_status', None)
            error_data["user_message"] = "An unexpected error occurred with our payment system. Please try again or contact support."
            
        else:
            # Non-Stripe errors (shouldn't happen in this context but just in case)
            logger.critical(f"Unexpected error during {operation}: {error}")
            error_data["error_type"] = "UnexpectedError"
            error_data["user_message"] = "An unexpected error occurred. Please try again or contact support."
        
        return error_data

def safe_stripe_operation(operation_name):
    ""
    Decorator for safely executing Stripe operations with proper error handling
    
    Args:
        operation_name: Description of the operation being performed
        
    Returns:
        Function decorator
    ""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return {
                    "success": True, 
                    "data": func(*args, **kwargs)
                }
            except stripe.error.StripeError as e:
                return StripeErrorHandler.handle_error(e, operation_name)
            except Exception as e:
                logger.critical(f"Unexpected error in {operation_name}: {e}")
                return {
                    "success": False,
                    "operation": operation_name,
                    "error_type": "UnexpectedError",
                    "error_message": str(e),
                    "user_message": "An unexpected error occurred. Please try again or contact support."
                }
        return wrapper
    return decorator

# Example usage
@safe_stripe_operation("create customer")
def create_customer_safely(email, name=None):
    return stripe.Customer.create(
        email=email,
        name=name
    )

@safe_stripe_operation("create payment intent")
def create_payment_intent_safely(amount, currency="usd", customer=None):
    params = {
        "amount": amount,
        "currency": currency
    }
    
    if customer:
        params["customer"] = customer
        
    return stripe.PaymentIntent.create(**params)

# Example of using the decorated functions
if __name__ == "__main__":
    # Set your API key
    stripe.api_key = "sk_test_your_test_key"
    
    # Example 1: Successful operation
    result = create_customer_safely(email="test@example.com", name="Test User")
    if result["success"]:
        print(f"Customer created successfully: {result['data'].id}")
    else:
        print(f"Error: {result['user_message']}")
    
    # Example 2: Operation that might fail (using invalid card)
    try:
        # This will fail with a card error
        card_token = stripe.Token.create(
            card={
                "number": "4000000000000002",  # This card number always fails
                "exp_month": 12,
                "exp_year": 2025,
                "cvc": "123"
            }
        )
        
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "token": card_token.id
            }
        )
        
        # This should fail with a card error
        @safe_stripe_operation("process payment")
        def process_payment():
            return stripe.PaymentIntent.create(
                amount=2000,
                currency="usd",
                payment_method=payment_method.id,
                confirm=True
            )
            
        result = process_payment()
        if result["success"]:
            print("Payment processed successfully")
        else:
            print(f"Error: {result['user_message']}")
    except Exception as e:
        print(f"Unexpected error: {e}")

"""
