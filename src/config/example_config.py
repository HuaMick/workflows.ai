"""
This file serves as an example of how to structure configuration for the project.

Configurations are managed as Python dictionaries, allowing for hierarchical
and organized settings. This approach promotes clarity and ease of maintenance.
"""

CONFIG = {
    # Database connection settings
    # Best practice: Load sensitive data like user/password from environment variables or secrets.
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "env_var(DB_PASSWORD)", # Placeholder for loading from environment
        "db_name": "production_db"
    },

    # API configuration
    "api_settings": {
        "base_url": "https://api.example.com/v1",
        "timeout_seconds": 30,
        "max_retries": 3
    },

    # Feature flags to enable or disable parts of the application
    "feature_flags": {
        "enable_new_user_onboarding": True,
        "enable_beta_feature_x": False,
    },

    # Configuration for a list of data processing pipelines
    # Using a list of dictionaries is ideal for repeated, structured items.
    "data_pipelines": [
        {
            "name": "daily_user_aggregation",
            "enabled": True,
            "schedule": "0 1 * * *", # Daily at 1 AM
            "source_table": "raw_events",
            "destination_table": "daily_summary",
            "parameters": {
                "batch_size": 1000,
                "deduplicate": True
            }
        },
        {
            "name": "hourly_metrics_rollup",
            "enabled": False, # This pipeline is currently disabled
            "schedule": "0 * * * *", # Every hour
            "source_table": "live_metrics",
            "destination_table": "hourly_rollup",
            "parameters": {
                "batch_size": 500,
                "deduplicate": False
            }
        }
    ]
}

def get_config():
    """
    A helper function to access the configuration.
    In a real application, this could be extended to load environment-specific overrides.
    """
    return CONFIG 