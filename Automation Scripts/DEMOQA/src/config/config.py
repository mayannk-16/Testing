class TestConfig:
    # Base URLs
    BASE_URL = "https://demoqa.com"
    
    # Browser Settings
    BROWSER = "chrome"
    HEADLESS = False
    IMPLICIT_WAIT = 20  # Increased for DemoQA's dynamic loading
    
    # Test Data
    TEST_USER = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": "30",
        "salary": "50000",
        "department": "QA",
        "current_address": "123 Test Street, City",
        "permanent_address": "456 Permanent Ave, Town"
    }
    
    FORM_DATA = {
        "mobile": "1234567890",
        "subjects": ["Computer Science", "English"],
        "hobbies": ["Sports", "Reading", "Music"],
        "state": "NCR",
        "city": "Delhi"
    }