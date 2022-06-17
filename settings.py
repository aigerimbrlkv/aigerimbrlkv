class Settings:
    """A class to store all settings for AirTable."""
    HEADERS: dict = {'Authorization': 'Bearer keyDiFQkGJiJpRn1D', 'Content-Type': 'application/json'} # Your API key. You can get it from https://airtable.com/account/
    TABLE_NAME: str = 'Cars' #Your table name
    BASE_ID: str = 'app58aMzwD44YTDOE' # Your base ID

    LIST_RECORDS_URL: str = f'?maxRecords=3&view=Grid%20view' # Your list records URL
    CREATE_RECORD_URL: str = f'/{BASE_ID}/{TABLE_NAME}'


    @property
    def get_url(self):
        """Returns the URL for the API."""
        return f'https://api.airtable.com/v0/{self.BASE_ID}/{self.TABLE_NAME}'
    


settings = Settings()
# https://api.airtable.com/v0/app58aMzwD44YTDOE/Cars \