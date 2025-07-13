from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime
import random

app = Flask(__name__)

# Skin analysis data and recommendations
SKIN_TYPES = {
    'normal': {
        'characteristics': ['balanced oil and moisture', 'few imperfections', 'barely visible pores'],
        'concerns': ['maintaining balance', 'anti-aging prevention'],
        'recommendations': ['gentle cleanser', 'lightweight moisturizer', 'broad-spectrum SPF']
    },
    'dry': {
        'characteristics': ['tight feeling', 'flaky skin', 'dull appearance'],
        'concerns': ['dehydration', 'premature aging', 'sensitivity'],
        'recommendations': ['hydrating cleanser', 'rich moisturizer', 'hyaluronic acid serum']
    },
    'oily': {
        'characteristics': ['shiny appearance', 'enlarged pores', 'prone to blackheads'],
        'concerns': ['excess sebum', 'acne', 'enlarged pores'],
        'recommendations': ['salicylic acid cleanser', 'oil-free moisturizer', 'niacinamide serum']
    },
    'combination': {
        'characteristics': ['oily T-zone', 'dry cheeks', 'varied texture'],
        'concerns': ['balancing different areas', 'targeted treatment'],
        'recommendations': ['gentle cleanser', 'lightweight moisturizer', 'targeted serums']
    },
    'sensitive': {
        'characteristics': ['easily irritated', 'redness', 'burning sensation'],
        'concerns': ['irritation', 'inflammation', 'barrier repair'],
        'recommendations': ['fragrance-free cleanser', 'barrier repair moisturizer', 'mineral sunscreen']
    }
}

PRODUCT_CATALOG = {
    'cleansers': [
        {'name': 'Derma-Pure Gentle Cleanser', 'type': 'gentle', 'ingredients': ['ceramides', 'hyaluronic acid'], 'price': 24.99, 'stock':0},
        {'name': 'Clarifying Foam Cleanser', 'type': 'oily', 'ingredients': ['salicylic acid', 'tea tree'], 'price': 28.99, 'stock':0},
        {'name': 'Hydrating Cream Cleanser', 'type': 'dry', 'ingredients': ['glycerin', 'squalane'], 'price': 26.99, 'stock':0},
        {'name': 'Sensitive Skin Cleanser', 'type': 'sensitive', 'ingredients': ['oat extract', 'allantoin'], 'price': 29.99, 'stock':0}
    ],
    'moisturizers': [
        {'name': 'Barrier Repair Moisturizer', 'type': 'dry', 'ingredients': ['ceramides', 'niacinamide'], 'price': 34.99, 'stock':0},
        {'name': 'Oil-Free Hydrating Gel', 'type': 'oily', 'ingredients': ['hyaluronic acid', 'zinc'], 'price': 32.99, 'stock':0},
        {'name': 'Daily Balance Moisturizer', 'type': 'normal', 'ingredients': ['peptides', 'vitamin E'], 'price': 30.99, 'stock':0},
        {'name': 'Ultra-Gentle Moisturizer', 'type': 'sensitive', 'ingredients': ['colloidal oatmeal', 'shea butter'], 'price': 36.99, 'stock':0}
    ],
    'serums': [
        {'name': 'Vitamin C Brightening Serum', 'type': 'all', 'ingredients': ['L-ascorbic acid', 'vitamin E'], 'price': 45.99, 'stock':0},
        {'name': 'Niacinamide Pore Refining Serum', 'type': 'oily', 'ingredients': ['niacinamide', 'zinc oxide'], 'price': 38.99, 'stock': 0},
        {'name': 'Hyaluronic Acid Plumping Serum', 'type': 'dry', 'ingredients': ['hyaluronic acid', 'peptides'], 'price': 42.99, 'stock':0},
        {'name': 'Retinol Renewal Serum', 'type': 'normal', 'ingredients': ['retinol', 'squalane'], 'price': 48.99, 'stock':0}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCT_CATALOG)

@app.route('/api/analyze-skin', methods=['POST'])
def analyze_skin():
    data = request.json
    
    # Simple AI-like analysis based on user inputs
    concerns = data.get('concerns', [])
    skin_feel = data.get('skin_feel', '')
    breakouts = data.get('breakouts', '')
    sensitivity = data.get('sensitivity', '')
    
    # Determine skin type based on inputs
    skin_type = 'normal'
    
    if 'oily' in skin_feel.lower() or 'shiny' in skin_feel.lower():
        skin_type = 'oily'
    elif 'dry' in skin_feel.lower() or 'tight' in skin_feel.lower():
        skin_type = 'dry'
    elif 'combination' in skin_feel.lower() or 'mixed' in skin_feel.lower():
        skin_type = 'combination'
    elif sensitivity.lower() == 'high' or 'sensitive' in concerns:
        skin_type = 'sensitive'
    
    # Get skin type info
    skin_info = SKIN_TYPES.get(skin_type, SKIN_TYPES['normal'])
    
    # Generate personalized recommendations
    recommendations = []
    
    # Add cleanser recommendation
    cleanser_options = [p for p in PRODUCT_CATALOG['cleansers'] if p['type'] == skin_type or p['type'] == 'all']
    if cleanser_options:
        recommendations.append(random.choice(cleanser_options))
    
    # Add moisturizer recommendation
    moisturizer_options = [p for p in PRODUCT_CATALOG['moisturizers'] if p['type'] == skin_type or p['type'] == 'all']
    if moisturizer_options:
        recommendations.append(random.choice(moisturizer_options))
    
    # Add serum recommendation
    serum_options = [p for p in PRODUCT_CATALOG['serums'] if p['type'] == skin_type or p['type'] == 'all']
    if serum_options:
        recommendations.append(random.choice(serum_options))
    
    # Generate routine
    routine = {
        'morning': [
            'Gentle cleanser',
            'Vitamin C serum (if recommended)',
            'Moisturizer',
            'Broad-spectrum SPF 30+'
        ],
        'evening': [
            'Cleanser',
            'Treatment serum',
            'Moisturizer',
            'Overnight treatment (if needed)'
        ]
    }
    
    return jsonify({
        'skin_type': skin_type,
        'characteristics': skin_info['characteristics'],
        'concerns': skin_info['concerns'],
        'recommendations': recommendations,
        'routine': routine,
        'analysis_id': f"ANALYSIS_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    })

@app.route('/api/get-recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    skin_type = data.get('skin_type', 'normal')
    budget = data.get('budget', 100)
    
    # Filter products based on skin type and budget
    filtered_products = []
    total_cost = 0
    
    for category in PRODUCT_CATALOG:
        suitable_products = [p for p in PRODUCT_CATALOG[category] 
                           if p['type'] == skin_type or p['type'] == 'all']
        if suitable_products:
            product = min(suitable_products, key=lambda x: x['price'])
            if total_cost + product['price'] <= budget:
                filtered_products.append({**product, 'category': category})
                total_cost += product['price']
    
    return jsonify({
        'recommended_products': filtered_products,
        'total_cost': total_cost,
        'remaining_budget': budget - total_cost
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
