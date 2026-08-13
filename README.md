# prevent-test-writes-production-environment
This example demonstrates how to prevent test suites or any non-production code from writing data to a production environment. It uses an environment variable (`APP_ENV`) to differentiate between environments and conditionally blocks write operations when in 'production' mode. This pattern helps maintain data integrity and security.
