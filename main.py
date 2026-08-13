import os

# Simulate a database connection or a data storage mechanism
# In a real application, this would be a DB client, file handler, etc.
DATABASE_MOCK = []

def write_to_database(data: str):
    """
    Simulates writing data to a database.
    This function should be protected from production writes by test suites.
    """
    # --- ARTICLE'S CORE CONCEPT ILLUSTRATION ---
    # Check if the current environment is 'production'.
    # This is a common way to differentiate environments in applications
    # using environment variables, configuration files, or command-line arguments.
    current_env = os.getenv('APP_ENV', 'development') # Default to 'development' if not set

    if current_env == 'production':
        print(f"[ERROR] Attempted to write '{data}' to production environment! Operation blocked.")
        return False
    else:
        DATABASE_MOCK.append(data)
        print(f"[SUCCESS] Data '{data}' written to '{current_env}' environment.")
        return True

def run_test_suite():
    """
    Simulates a test suite that might attempt to write data.
    """
    print("\n--- Running Test Suite ---")
    print("Test: Should save configuration data.")
    write_to_database("config_setting_123")
    print("Test: Should save user preference.")
    write_to_database("user_pref_dark_mode")
    print("--- Test Suite Finished ---")

def main():
    print("--- Application Startup ---")

    # Scenario 1: Running in a 'development' environment
    print("\nSimulating 'development' environment (APP_ENV='development').")
    os.environ['APP_ENV'] = 'development' # Explicitly set for demonstration
    run_test_suite()
    print(f"Database content after dev tests: {DATABASE_MOCK}")
    DATABASE_MOCK.clear() # Clear for next scenario

    # Scenario 2: Running in a 'production' environment
    print("\nSimulating 'production' environment (APP_ENV='production').")
    os.environ['APP_ENV'] = 'production' # Set environment variable for production
    run_test_suite()
    print(f"Database content after prod tests: {DATABASE_MOCK}") # Should be empty

    # Scenario 3: Running in a 'staging' environment
    print("\nSimulating 'staging' environment (APP_ENV='staging').")
    os.environ['APP_ENV'] = 'staging' # Set environment variable for staging
    run_test_suite()
    print(f"Database content after staging tests: {DATABASE_MOCK}")
    DATABASE_MOCK.clear()

    print("\n--- Application Shutdown ---")

if __name__ == "__main__":
    main()
