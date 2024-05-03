from functions import get_settings
from MarketBot import MarketBot


def main():
    config = get_settings()
    bot = MarketBot(252490, config)
    bot.start()


if __name__ == "__main__":
    main()
