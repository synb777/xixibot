from telegram import Update
from telegram.ext import ContextTypes

async def record_income(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("已记录入账（示例功能）")

async def record_payout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("已记录下发（示例功能）")
