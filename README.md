# OpenAI Flask

## Quickstart

1. Install dependencies

    ```shell
    pip install -r requirements.txt
    ```

1. Create `.env` file with the following keys

    ```dotenv
    FLASK_APP=app.main
    FLASK_DEBUG=1
    FLASK_RUN_HOST=localhost
    FLASK_RUN_PORT=80
    API_KEY=
    ORGANIZATION_ID=
    ```

    - Find your API key at https://beta.openai.com/account/api-keys.
    - Find your organization ID at https://beta.openai.com/account/org-settings.

1. Serve

    ```shell
    flask run 
    ```
