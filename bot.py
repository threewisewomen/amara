from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# Options for Utility Pants
UTILITY_PANTS_OPTIONS = {
    "exploration": [
        "Trail – Basic yet reliable, perfect for everyday use.",
        "Adventure – Enhanced features for outdoor enthusiasts.",
        "Expedition – Maximum utility for extreme conditions and exploration.",
    ],
    "sleek": [
        "Core – Simple, essential design.",
        "Edge – Adding an extra layer of utility.",
        "Apex – The pinnacle of functionality and design.",
    ],
    "military": [
        "Scout – Lightweight and nimble, for essential needs.",
        "Ranger – Versatile and dependable, with added utility.",
        "Operator – Heavy-duty, with ultimate functionality and secret compartments.",
    ],
    "customize": ["Customize your pant."],
}

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Welcome message
    welcome_text = (
        "Welcome to Amara! 👗✨\n\n"
        "We specialize in durable and stylish homewear. Right now, you can shop for our amazing "
        "utility pants designed for comfort and durability at home. 👖🏡\n\n"
        "What would you like to do?"
    )

    # Options for the user
    keyboard = [
        [InlineKeyboardButton("Shop Utility Pants", callback_data="shop_pants")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the welcome message with options
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Define a handler to display pant options
async def shop_pants(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Prepare the keyboard for options
    keyboard = [
        [InlineKeyboardButton("Inspired by Exploration", callback_data="exploration")],
        [InlineKeyboardButton("Sleek Utility-Focused", callback_data="sleek")],
        [InlineKeyboardButton("Inspired by Military/Utility Aesthetics", callback_data="military")],
        [InlineKeyboardButton("Customize your pant", callback_data="customize")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Respond with options
    await query.edit_message_text(
        text="Choose your style of utility pants:",
        reply_markup=reply_markup,
    )

# Define handlers for each category
async def show_options(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Get the options based on the callback data
    category = query.data
    if category in UTILITY_PANTS_OPTIONS:
        options = UTILITY_PANTS_OPTIONS[category]

        # Create buttons for each option
        keyboard = [[InlineKeyboardButton(option, callback_data=f"{category}_{index}")] for index, option in enumerate(options)]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send the message with the buttons
        await query.edit_message_text(
            text=f"Here are the options for {category.capitalize()}:",
            reply_markup=reply_markup,
        )
    else:
        await query.edit_message_text(text="Invalid option. Please try again.")

def main():
    # Replace 'YOUR_API_TOKEN' with the token from BotFather
    application = Application.builder().token("7904044893:AAFEkbKqkcI4Ek6pVhXiyEDKbNNd77DsgqI").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(shop_pants, pattern="^shop_pants$"))
    application.add_handler(CallbackQueryHandler(show_options, pattern="^(exploration|sleek|military|customize)$"))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
