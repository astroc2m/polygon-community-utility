import telebot
from telebot import types



bot = telebot.TeleBot(TOKEN)

# Handler for /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🚀 *Welcome to the ASTROC2M Protocol!* \n\n"
        "You are now part of an institutional-grade ecosystem on Polygon.\n\n"
        "💎 *Quick Links:*\n"
        "• Website: [astroc2m.com](https://astroc2m.com)\n"
        "• Mint App: [app.astroc2m.com](https://app.astroc2m.com)\n"
        "• Documentation: [GitHub Repository](https://github.com/astroc2m/polygon-community-utility)\n\n"
        "Type /utility to learn more about the Genesis NFT benefits."
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown', disable_web_page_preview=True)

# Handler for the /utility command with Interactive Buttons
@bot.message_handler(commands=['utility'])
def send_utility(message):
    # Creating the Inline Keyboard for professional navigation
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Defining buttons with official ecosystem links
    btn_web = types.InlineKeyboardButton("🌐 Visit Website", url="https://astroc2m.com")
    btn_github = types.InlineKeyboardButton("🛠️ View Documentation", url="https://github.com/astroc2m/polygon-community-utility")
    btn_dash = types.InlineKeyboardButton("📊 Access Dashboard", url="https://app.astroc2m.com")
    
    # Adding buttons to the markup
    markup.add(btn_web, btn_github, btn_dash)

    utility_text = (
        "📊 *ASTROC2M Genesis Utility:*\n\n"
        "1. Access to the Holder Insight Dashboard.\n"
        "2. Sustainability through the 80/20 Liquidity Rule.\n"
        "3. Community Patent Evolution (Cadet to Admiral).\n\n"
        "Choose an option below to explore:"
    )
    bot.reply_to(message, utility_text, reply_markup=markup, parse_mode='Markdown')

# Automatic welcome handler for new members joining the group
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_user in message.new_chat_members:
        welcome_msg = (
            f"🛰️ **Welcome to the Bridge, Commander {new_user.first_name}!**\n\n"
            "Official ASTROC2M resources are now live and operational:\n"
            "🌐 **Website**: [astroc2m.com](https://astroc2m.com)\n"
            "🛠️ **Documentation**: [GitHub](https://github.com/astroc2m/polygon-community-utility)\n\n"
            "Use the `/utility` command to see holder benefits."
        )
        bot.send_message(message.chat.id, welcome_msg, parse_mode='Markdown', disable_web_page_preview=True)

# Main entry point to start the bot service
if __name__ == "__main__":
    print("🛰️ ASTROC2M Support Bot is Online...")
    bot.infinity_polling()
