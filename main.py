from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.accounting import record_income, record_payout

def main():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("income", record_income))
    app.add_handler(CommandHandler("payout", record_payout))


    app.run_polling()

if __name__ == "__main__":
    main()
