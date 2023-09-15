from sqlalchemy.engine.url import URL

# openai_api_key = "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"
openai_api_key = "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"
serp_api_key = "f0494e915c393c63c7980d09f441d6feab2a12bf1945cc7a79553bf2907ba175"

# redshift_url = URL.create(
#     drivername="postgresql+psycopg2",  # "redshift+redshift_connector",  # indicate redshift_connector driver and dialect will be used
#     host="da-rs-01.c9guzayxgh22.us-east-1.redshift.amazonaws.com",  # Amazon Redshift host
#     port=5439,  # Amazon Redshift port
#     database="dev",  # Amazon Redshift database
#     username="airflow_app",  # Amazon Redshift username
#     password="TraN3!2pOT_1",  # Amazon Redshift password
# )

neondb_uri = f"postgresql://mohit.khanwale1:ObAglCa8z7oS@ep-bitter-leaf-43877279.us-east-2.aws.neon.tech/neondb"
