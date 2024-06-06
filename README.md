1. Clone repository
git clone https://github.com/Satish-Kuppan/Movie-Wiki.git

2. Install requirements
pip install -r requirements.txt

3. Generate OMDB api key and replace XXX with your key obtained
api_key = 'XXX' - #YOUR_API_KEY_HERE

4. Create a bot in telegram and add the token in the environment
updater = Updater(token='YYY', use_context=True) - #YOUR_TELEGRAM_BOT_TOKEN_HERE
Refer https://core.telegram.org/bots

5. Start bot
python app.py
