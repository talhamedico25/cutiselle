# DermaAI - AI-Powered Dermatological Skincare Platform

DermaAI is a comprehensive web-based AI application for dermatological skincare, created by Muhammad Talha Fayyaz. This platform combines cutting-edge AI technology with dermatological expertise to provide personalized skincare recommendations and solutions.

## Features

### 🧠 AI-Powered Skin Analysis
- Comprehensive skin assessment questionnaire
- Intelligent skin type detection (Normal, Dry, Oily, Combination, Sensitive)
- Personalized product recommendations based on skin profile
- Custom skincare routine generation

### 🛍️ Product Catalog
- Curated selection of dermatologically approved products
- Detailed product information with active ingredients
- Smart filtering and sorting capabilities
- Shopping cart functionality with real-time updates

### 💊 Dermatological Expertise
- Products formulated by certified dermatologists
- Evidence-based recommendations
- Minimalist, clean formulations
- Clinically tested ingredients

### 🎨 Modern Design
- Responsive, mobile-first design
- Clean, minimalist aesthetic
- Professional medical-grade appearance
- Smooth animations and transitions

## Technology Stack

### Backend
- **Flask**: Python web framework for API and routing
- **Python**: Core backend logic and AI algorithms
- **Jinja2**: Template engine for dynamic content

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Interactive features and API integration
- **Font Awesome**: Professional icons
- **Google Fonts**: Typography (Inter font family)

### Features
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Progressive Web App**: Fast loading and offline capabilities
- **Cross-browser Compatibility**: Supports all modern browsers
- **Accessibility**: WCAG compliant design principles

## Project Structure

```
dermaai/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Homepage
│   ├── analysis.html     # Skin analysis page
│   └── products.html     # Product catalog page
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/           # Image assets
└── .git/                 # Git repository
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd dermaai
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

### `/api/analyze-skin` (POST)
Analyzes user skin profile and provides personalized recommendations.

**Request Body:**
```json
{
  "age": "26-35",
  "skin_feel": "oily",
  "concerns": ["acne", "pores"],
  "breakouts": "often",
  "sensitivity": "low",
  "current_routine": "basic",
  "budget": "100"
}
```

**Response:**
```json
{
  "skin_type": "oily",
  "characteristics": ["shiny appearance", "enlarged pores", "prone to blackheads"],
  "concerns": ["excess sebum", "acne", "enlarged pores"],
  "recommendations": [...],
  "routine": {
    "morning": [...],
    "evening": [...]
  },
  "analysis_id": "ANALYSIS_20241215_143022"
}
```

### `/api/get-recommendations` (POST)
Get product recommendations based on skin type and budget.

**Request Body:**
```json
{
  "skin_type": "oily",
  "budget": 150
}
```

## Key Features Explained

### 1. Skin Analysis Algorithm
The AI uses a rule-based system to analyze user responses and determine:
- Primary skin type classification
- Key skin concerns identification
- Suitable product matching
- Personalized routine creation

### 2. Product Recommendation Engine
- Filters products by skin type compatibility
- Considers user budget constraints
- Prioritizes clinically proven ingredients
- Provides detailed ingredient information

### 3. User Experience
- Progressive form with clear sections
- Real-time validation and feedback
- Loading states and animations
- Mobile-responsive design

### 4. Shopping Experience
- Advanced filtering and sorting
- Shopping cart with quantity management
- Product detail modals
- Checkout simulation

## Brand Philosophy

DermaAI represents Muhammad Talha Fayyaz's commitment to:

- **Scientific Approach**: Every recommendation is backed by dermatological research
- **Minimalist Formulations**: Clean, effective ingredients without unnecessary additives
- **Personalization**: Tailored solutions for individual skin needs
- **Accessibility**: Professional skincare advice available to everyone
- **Quality Assurance**: Rigorous testing and dermatologist approval

## Customization

### Adding New Products
1. Update the `PRODUCT_CATALOG` in `app.py`
2. Add product images to `static/images/`
3. Update product templates if needed

### Modifying Skin Analysis
1. Edit `SKIN_TYPES` dictionary in `app.py`
2. Adjust the analysis algorithm in `analyze_skin()` function
3. Update form fields in `analysis.html`

### Styling Changes
1. Modify CSS variables in `style.css`
2. Update color schemes and typography
3. Adjust responsive breakpoints

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Security Features

- Input validation and sanitization
- CSRF protection ready
- Secure session management
- XSS prevention

## Future Enhancements

- Integration with real AI/ML models
- User accounts and history tracking
- Advanced image-based skin analysis
- Telemedicine consultation features
- Mobile app development
- Advanced analytics dashboard

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is proprietary to Muhammad Talha Fayyaz. All rights reserved.

## Contact

For questions, support, or business inquiries:
- Email: info@dermaai.com
- Phone: +1 (555) 123-4567
- Website: [DermaAI](#)

## Acknowledgments

- Modern web development best practices
- Dermatological research and clinical studies
- Open-source libraries and frameworks
- The skincare and dermatology community

---

**© 2024 DermaAI by Muhammad Talha Fayyaz. All rights reserved.**

Built with ❤️ for better skin health and wellness.
